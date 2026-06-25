# Smart Garden Probe

A custom XIAO RP2040-powered control pad with an OLED display and I2C soil sensor for smart garden monitoring.

## Overview

The Smart Garden Probe is a custom three-key control pad that also works as a small plant-monitoring device. It uses a Seeed Studio XIAO RP2040, an OLED display, and an I2C capacitive soil sensor to show soil moisture and local temperature readings.

The idea behind this project was to create a Hackpad with a real hardware purpose beyond keyboard shortcuts. The buttons allow the user to interact with the device, while the OLED provides clear feedback from the garden probe.

Instead of only showing raw sensor values, the firmware uses plant profiles. Each profile contains its own target moisture and temperature ranges, allowing the device to display simple messages such as `Too Dry`, `Good`, or `Too Wet`.

## Specifications

* Three MX-style mechanical switch inputs
* SSD1306 I2C OLED display
* I2C capacitive soil sensor connection
* Soil moisture and local temperature shown together
* Saved plant-profile system with multiple plants available
* Mode button cycles through saved plant profiles
* USB-C powered through the XIAO RP2040
* Custom two-layer PCB
* 3D-printable sandwich-style enclosure
* Exported Gerber and drill files
* Exported STEP enclosure files
* Supports up to five active plant profiles for simple operation

## Use Cases

### Plant Monitoring

The main use case is quickly checking whether a plant's soil is too dry, too wet, or within a healthy range. The soil sensor provides a moisture reading, and the firmware compares it with the selected plant profile.

### Desk Garden Setup

The device is designed to sit near a small indoor plant, planter, or desktop garden. The OLED provides useful feedback without requiring a computer, phone application, or serial monitor.

### Custom Plant Profiles

Different plants require different moisture and temperature ranges. The mode button cycles between saved plant profiles, allowing the same device to be used for plants such as basil, pothos, snake plants, and other common houseplants.

### Open-Source Hardware Learning

This project is also intended to be a complete open-source hardware build. It includes a custom PCB, enclosure CAD, firmware, a plant-profile database, a bill of materials, and manufacturing exports so others can understand, build, or modify the design.

## Motivation

I wanted this project to be more than a normal macropad because of my previous hardware experience. A basic macropad is useful, but I wanted this one to feel like a small standalone device with a clear purpose.

The garden-probe idea made the project more interesting because it combines physical buttons, sensor readings, display output, custom PCB design, firmware, and a 3D-printed enclosure. The enclosure also turned out better than my previous hardware project, which made the complete design feel much more polished.

The goal was to create something that would be useful in my daily life because I have many plants at home.

## Project Views

| Top View                                                                                                                                                     | Front View                                                                                                                                                     | PCB View                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="300" alt="Top view of the Smart Garden Probe enclosure" src="https://github.com/user-attachments/assets/ac47262c-fc2d-4806-abad-520eaac7ded3" /> | <img width="300" alt="Front view of the Smart Garden Probe enclosure" src="https://github.com/user-attachments/assets/1d4f6df5-2260-412c-9aa8-8360e7d5d417" /> | <img width="300" alt="Smart Garden Probe PCB" src="https://github.com/user-attachments/assets/b316d4bf-769f-46a4-bd23-ed93fb88cc1f" /> |

## Hardware Overview

The XIAO RP2040 controls the switches, OLED display, and soil sensor. The device is powered through the XIAO's USB-C port. The OLED and soil sensor are powered from the XIAO's 3.3-volt output.

The three switches are wired directly between GPIO pins and ground. The firmware uses the XIAO RP2040's internal pull-up resistors, so the button circuit does not require additional external resistors.

The OLED display and soil sensor share the same I2C bus through the SDA and SCL connections.

| Part            | Details                                             |
| --------------- | --------------------------------------------------- |
| Microcontroller | Seeed Studio XIAO RP2040                            |
| Display         | 128×64 SSD1306 I2C OLED                             |
| Sensor          | I2C capacitive soil-moisture and temperature sensor |
| Inputs          | Three MX-style mechanical switches                  |
| Power           | USB-C through the XIAO RP2040                       |
| PCB             | Custom two-layer KiCad PCB                          |
| Enclosure       | Custom 3D-printable top plate and bottom shell      |

## Button Functions

| Button | Function                                           |
| ------ | -------------------------------------------------- |
| SW1    | Refresh the sensor readings                        |
| SW2    | Cycle through saved plant profiles                 |
| SW3    | Toggle the display between active and sleep states |

## PCB Design

The custom PCB was designed in KiCad and measures approximately 62.5 mm by 62.5 mm. It includes the XIAO RP2040, three switch footprints, OLED and soil-sensor headers, and four 2.5 mm mounting holes.

The PCB was checked using KiCad's Design Rules Checker before the Gerber and drill files were exported.

## Enclosure Design

The enclosure was designed around the final PCB rather than treating the PCB and case as separate parts. The PCB model was placed inside the CAD assembly to check:

* Mounting-hole alignment
* Header clearance
* XIAO and USB-C clearance
* Switch positioning
* OLED positioning
* Soil-sensor cable access
* Wall and standoff collisions

The header and mounting-hole locations were corrected after checking the PCB inside the enclosure. The final design includes a top plate, bottom shell, PCB supports, USB-C opening, soil-sensor cable opening, and mounting hardware.

## Firmware

The firmware is designed to:

* Read moisture and temperature from the soil sensor
* Display both measurements at the same time
* Compare readings against the selected plant profile
* Show status messages such as `Too Dry`, `Good`, and `Too Wet`
* Cycle through saved plant profiles
* Refresh readings manually or automatically
* Control the OLED sleep state

The repository also includes a test script that allows the plant-profile logic to be checked before the physical hardware is assembled.

## Repository Structure

| File or Folder      | Purpose                                         |
| ------------------- | ----------------------------------------------- |
| `README.md`         | Main project overview                           |
| `BOM.md`            | Parts, prices, and product links                |
| `JOURNAL.md`        | Project development log                         |
| `plant_database.md` | Available plant profiles                        |
| `pcb/`              | KiCad source files, schematic, PCB, and Gerbers |
| `case/`             | Enclosure CAD and STEP files                    |
| `firmware/`         | Main firmware, plant profiles, and test scripts |
| `images/`           | PCB, CAD, and project images                    |

## Project Status

| Area                         | Status               |
| ---------------------------- | -------------------- |
| Project planning             | Complete             |
| Schematic                    | Complete             |
| PCB layout                   | Complete             |
| PCB mounting holes           | Corrected            |
| Design-rules check           | Passed               |
| Gerber and drill exports     | Complete             |
| Enclosure CAD                | Complete             |
| PCB-to-enclosure fit check   | Complete             |
| STEP exports                 | Complete             |
| Firmware structure           | Complete             |
| Plant-profile logic          | Complete             |
| Physical assembly            | Waiting for parts    |
| Sensor calibration           | Waiting for parts    |
| Final hardware demonstration | Waiting for assembly |
