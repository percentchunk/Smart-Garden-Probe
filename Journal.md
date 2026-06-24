
# Smart Garden Probe Project Journal

## Current Total Time

**6 hours completed**

Assembly and physical testing will be added after the PCB and components arrive.

## Project Planning — 30 minutes

I planned the Smart Garden Probe as a three-button device that also works as a standalone plant monitor. I decided to use a XIAO RP2040, OLED display, capacitive soil sensor, custom PCB, and 3D-printed enclosure.

## Schematic Design — 1 hour

I created the schematic in KiCad and connected the three switches to the XIAO GPIO pins. I also connected the OLED and soil sensor to the shared I2C bus and added headers for both devices.

## PCB Design — 1 hour 30 minutes

I designed and routed a custom two-layer PCB. I placed the XIAO, three MX switches, OLED header, soil-sensor header, and mounting holes, then exported the Gerber and drill files.

## Enclosure CAD — 1 hour 15 minutes

I designed the top plate and bottom enclosure in Onshape. The case includes switch openings, an OLED window, USB-C access, a soil-sensor cable opening, PCB supports, and screw mounting points.

## Firmware and Plant Profiles — 1 hour 15 minutes

I created the firmware structure for the buttons, OLED, soil sensor, automatic updates, and plant-profile cycling. I also created moisture and temperature status logic and a test script that can run before the hardware arrives.

## Repository Documentation — 30 minutes

I organized the GitHub repository and added the README, BOM, firmware files, plant database, PCB files, Gerbers, STEP files, and project renders.

## Future Work

The following work is not included in the current six-hour total as it has not been started yet:

* PCB assembly
* Soldering
* Enclosure assembly
* OLED and sensor testing
* Soil-sensor calibration
* Final plant demonstration
