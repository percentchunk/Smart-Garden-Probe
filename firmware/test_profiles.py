#Smart Garden Probe Hackpad profile test
#this is a firmware demo to prove the function of the smart garden code

#Run this file on your computer to preview how different plant profiles
#respond to the moisture and temperature readings.
from plants import PLANTS

MAX_PLANTS = 5
active_plants = PLANTS[:MAX_PLANTS]


def check_range(value, minimum, maximum):
    if value < minimum:
        return "Too Low"
    if value > maximum:
        return "Too High"
    return "Good"


def check_moisture(moisture_value, plant):
    if moisture_value < plant["moisture_min"]:
        return "Too Dry"
    if moisture_value > plant["moisture_max"]:
        return "Too Wet"
    return "Good"


def check_temperature(temp_c, plant):
    return check_range(temp_c, plant["temp_min_c"], plant["temp_max_c"])

#sample readings 
test_moisture = 742
test_temperature_c = 23.6

print("Smart Garden Probe Hackpad")
print("Plant Profile Test")
print("=========================")
print("Sample moisture:", test_moisture)
print("Sample temperature:", test_temperature_c,"C")
print()

for plant in active_plants: 
    moisture_status = check_moisture(test_moisture,plant)
    temp_status = check_temperature(test_temperature_c,plant)


    print("Plant:", plant["name"])
    print("Moisture:", test_moisture, "-", moisture_status)
    print("Temperature:", test_temperature_c, "C -", temp_status)
    print("------------------------")
