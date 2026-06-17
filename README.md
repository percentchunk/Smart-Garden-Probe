# Smart-Garden-Probe
A customized XIAO RP2040-powered macropad with an OLED display and I2C soil sensor for smart garden monitoring. 





**Hardware Overview**

The XIAO RP2040 controls the switches, OLED display, and soil sensor. The board is powered through the XIAO’s USB-C port, and the OLED and soil sensor are powered from the XIAO’s 3V3 pin.

The three switches are wired directly from GPIO pins to ground. The firmware uses internal pull-up resistors, so the button circuit stays simple and does not need external resistors or diodes.

Part	Purpose
XIAO RP2040	Main controller
3 MX switches	User input
OLED display	Shows sensor readings
I2C soil sensor	Measures soil moisture and local temperature
Custom PCB	Connects all electronics
3D-printed case	Holds the PCB, OLED, and switches
