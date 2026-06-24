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
<img width="2560" height="1080" alt="Screenshot 2026-06-17 at 11 50 49 AM (2) 2" src="https://github.com/user-attachments/assets/dc390feb-ba15-479b-a764-b257aa296e33" />
<img width="1440" height="900" alt="Screenshot 2026-06-17 at 11 51 11 AM 2" src="https://github.com/user-attachments/assets/5b12f051-d2ea-48e9-9ceb-a7ecf77c323d" />

## Enclosure CAD — 1 hour 15 minutes

I designed the top plate and bottom enclosure in Onshape. The case includes switch openings, an OLED window, USB-C access, a soil-sensor cable opening, PCB supports, and screw mounting points.
<img width="1440" height="900" alt="Screenshot 2026-06-17 at 11 44 27 AM 2" src="https://github.com/user-attachments/assets/3867f6c6-ad6c-499c-9611-6b00ef03e50a" />

## Firmware and Plant Profiles — 1 hour 15 minutes

I created the firmware structure for the buttons, OLED, soil sensor, automatic updates, and plant-profile cycling. I also created moisture and temperature status logic and a test script that can run before the hardware arrives.
<img width="2560" height="1080" alt="610020152-e79e22c7-d8fa-47d8-90f6-0c1a537301cb" src="https://github.com/user-attachments/assets/825b9f82-8d3c-4291-b13a-ff6e21121424" />

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
