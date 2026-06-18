#Smart Garden Probe Hackapad 
#Board to be used is the Seeed Studio XIAO RP2040
#Post Conditions
# Use three buttons for refresh, mode, and sleep

#read the soil sensor
#display soil moisture and local temperature on OLED
#sw1 refreshes the reading
#sw2 cycles plant proiles 
#sw3 controls sleepdisplay behavior
import time
import board
import digitalio
import busio 

from plants import PLANTS

#OlED imports 
import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306

#Soil Sensor imports
from adafruit_seesaw.seesaw import Seesaw

MAX_PLANTS = 5 
active_plants=PLANTS[:MAX_PLANTS]
current_plant_index=0
display_enabled = True

#Button Setup
refresh_button = digitalio.DigitalInOut(board.D0)
refresh_button.direction = digitalio.Direction.INPUT
refresh_button.pull = digitalio.Pull.UP

mode_button = digitalio.DigitalInOut(board.D1)
mode_button.direction = digitalio.Direction.INPUT
mode_button.pull = digitalio.Pull.UP

sleep_button = digitalio.DigitalInOut(board.D2)
sleep_button.direction = digitalio.Direction.INPUT
sleep_button.pull = digitalio.Pull.UP

#I2C Set up
i2c = busio.I2C(board.SCL, board.SDA)
soil_sensor = Seesaw(i2c, addr=0x36)

#OlED Setup

displayio.release_displays()

display_bus = I2CDisplayBus(i2c,device_address=0X3C)

WIDTH=128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
)
#sonion tis is so much codeeeee
screen = displayio.Group()
display.root_group = screen

line1 = label.Label(terminalio.FONT,text="", x=0,y=10)
line2 = label.Label(terminalio.FONT,text="", x=0, y=25)
line3 = label.Label(terminalio.FONT, text="", x=0, y=40)
line4 = label.Label(terminalio.FONT,text="", x=0, y=55)

screen.append(line1)
screen.append(line2)
screen.append(line3)
screen.append(line4)

#plant logic 

def get_current_plant():
    return active_plants[current_plant_index]

def check_range(value,minimum, maximum):
    if value < minimum:
        return "Too Low"
    if value > maximum:
        return "Too High"
    return "Good"

def check_moisture(moisture_value,plant):
    if moisture_value < plant["moisture_min"]:
        return "Too Dry"
    if moisture_value > plant["moisture_max"]:
        return "Too Wet"
    return "Good"

def check_temperature(temp_c, plant):
    return check_range(temp_c, plant["temp_min_c"], plant["temp_max_c"])

def cycle_plant():
    global current_plant_index
    current_plant_index = (current_plant_index + 1) % len(active_plants)
    return get_current_plant()

def read_sensor():
    moisture = soil_sensor.moisture_read()
    temperature_c = soil_sensor.get_temp()
    return moisture, temperature_c

def update_display(moisture,temperature_c):
    plant = get_current_plant()
    moisture_status = check_moisture(moisture,plant)
    temp_status = check_temperature(temperature_c,plant)

    line1.text = plant["name"]
    line2.text = "M: " +str(moisture) + " " + moisture_status
    line3.text = "T: " + str(temperature_c)+ "C " + temp_status
    line4.text = "SW2 changes plant"
    
    print("Plant:",plant["name"])
    print("Moisture:",moisture,moisture_status)
    print("Temperature:", temperature_c,"C",temp_status)
    print("--------------")

def show_sleep_screen():
    line1.text = "Smart Garden"
    line2.text = "Display off"
    line3.text = "Press SW3"
    line4.text = "to wake"

#placeholder sensor values until the hardware is added
last_refresh_state = True
last_mode_state = True
last_sleep_state = True

last_update_time = 0
update_interval = 10

moisture,temperature_c = read_sensor()
update_display(moisture, temperature_c)

while True:
    refresh_state = refresh_button.value
    mode_state = mode_button.value
    sleep_state = sleep_button.value

    if last_refresh_state and not refresh_state:
        if display_enabled:
            moisture, temperature_c = read_sensor()
            update_display(moisture,temperature_c)
    
    if last_mode_state and not mode_state:
        if display_enabled:
            cycle_plant()
            moisture, temperature_c = read_sensor()
            update_display(moisture, temperature_c)
    
    if last_sleep_state and not sleep_state:
        display_enabled = not display_enabled

        if display_enabled:
            moisture,temperature_c = read_sensor()
            update_display(moisture, temperature_c)
        else: 
            show_sleep_screen()

    if display_enabled and time.monotonic() - last_update_time > update_interval:
        moisture,temperature_c = read_sensor()
        update_display(moisture, temperature_c)
        last_update_time = time.monotonic()

    last_refresh_state = refresh_state
    last_mode_state = mode_state
    last_sleep_state = sleep_state

    time.sleep(0.05)    

