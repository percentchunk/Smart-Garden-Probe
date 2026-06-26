**Smart Garden Probe**

The Smart Garden Probe is a small plant-monitoring device built around the Seeed Studio XIAO RP2040. It uses a soil sensor and OLED display to show soil moisture, temperature, and whether the plant is in a good range.

**Overview**

This project started as a three-key Hackpad, but I wanted it to do something more useful than keyboard shortcuts, and complex enough that it stands on its own.

The device has three buttons, an OLED display, and an I2C soil sensor. The sensor reads soil moisture and temperature, and the screen shows the readings along with a simple status such as Too Dry, Good, or Too Wet.

The firmware also uses plant profiles. Each profile stores the moisture and temperature ranges for a specific plant, you can edit this with the database in the github.

**Features**
Seeed Studio XIAO RP2040
Three MX-style switches
SSD1306 I2C OLED
I2C capacitive soil sensor
Custom two-layer PCB
Custom 3D-printed enclosure
USB-C power
Plant profile system
Moisture and temperature shown together
Gerber, drill, and STEP files included
Project Views
Top View	Front View	PCB View
<img width="300" alt="Top view" src="https://github.com/user-attachments/assets/ac47262c-fc2d-4806-abad-520eaac7ded3" />	<img width="300" alt="Front view" src="https://github.com/user-attachments/assets/1d4f6df5-2260-412c-9aa8-8360e7d5d417" />	<img width="300" alt="PCB view" src="https://github.com/user-attachments/assets/b316d4bf-769f-46a4-bd23-ed93fb88cc1f" />
How It Works

The soil sensor sends moisture and temperature readings to the XIAO RP2040 over I2C.

The firmware compares the readings with the selected plant profile. The OLED then shows the plant name, moisture, temperature, and status.

The three buttons are used to refresh the readings, change the plant profile, and control the display.

**Button Functions**
Button	Function
SW1	Refresh the sensor readings
SW2	Change the plant profile
SW3	Turn the display on or off
Hardware
Part	Details
Microcontroller	Seeed Studio XIAO RP2040
Display	128×64 SSD1306 I2C OLED
Sensor	I2C soil moisture and temperature sensor
Inputs	Three MX-style switches
Power	USB-C
PCB	Custom two-layer KiCad PCB
Enclosure	3D-printed top and bottom case

PCB

The PCB was designed in KiCad and is about 62.5 mm by 62.5 mm.

It includes:

The XIAO RP2040
Three switch footprints
OLED header
Soil sensor header
Four 2.5 mm mounting holes

I ran the KiCad Design Rules Checker and exported the Gerber and drill files.

**Cad**
The pad was designed in Onshape.

I added the PCB model to the CAD assembly so I could check the mounting holes, headers, USB-C port, switches, OLED, and cable opening.

The mounting holes and clearances were corrected after checking the PCB inside the case.

Firmware

The firmware is designed to:

Read the soil sensor
Show moisture and temperature
Compare readings with plant profiles
Show simple status messages
Change profiles with SW2
Refresh readings with SW1
Control the display with SW3
