# Firmware

This folder contains the firmware for the Smart Garden Probe Hackpad.

The firmware will read the soil sensor over I2C, display soil moisture and temperature on the OLED, and handle the three macropad buttons.

Read Soil moisture and temps
Display both values
Use Sw1 to refresh
Use Sw2 to cycle plant profiles
Use SW3 for power options

## Test File

`test_profiles.py` is a simple demo script that tests the plant profile system without needing the physical hardware connected. It uses sample moisture and temperature values and shows whether each saved plant profile would read as too dry, too wet, too cold, too hot, or good.