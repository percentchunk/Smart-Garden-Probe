# Smart-Garden-Probe
A customized XIAO RP2040-powered macropad with an OLED display and I2C soil sensor for smart garden monitoring.  
**Overview**

The control pad is a custom 3-key macropad that also works as a small plant-monitoring device. It uses a Seed Studio IXAO RP2040, and OLED dispaly, and an I2C capactivite soil sensor to show the soil moisture, and local temperature readings.

The idea behind this project is to make a HackPad that has a real hardware purpose beyond keyboard shortcuts. The buttonsl et the user interact with the device, while the OLED gives the correct feedbac, from the graden probe.

Instead of only showing raw sensor values, the firmwar is designed around plant profiles Each plant profule has its own target mositure, and temperature range, so the device can show simple messages like Too Dry, good, or too wet

**Specificatiosn** 

1.3 MX-Style Mechanical switch inputs
2.OLED display for sensor readings, and plant status
3.I2C capacititve soil sensor connection
4.Soil moisture and local temperature shown together. 
Saved plant profile system, with a large vareitiy of plants to choose from. 
Mode button cycles through saved plant profles 
ISB-C powered through the XIAO RP2040
3D-printable sandwhich - style enclourse
Exported Gerber files and STEP case files
Supports up to 5 saved plant profiles(can take more way more, but for easier use).

**Use Cases**

  **Plant Montitoring**

  The main use case is quickly checking whether a plant's soil is too dry, too wet, or in a good range. The soil sensor gives a moisture reading, and based off that, the firmware takes those readings and compares it to the selected plant profile.

  **Desk Garden Setup**

  The device is designed to sit near a small indoor, planter or desktop garden. The OLED gives correct feedback without needing to open a desktop,computer or a phone. 

  **Custom Plant Profiles**

  Differnt plants need different moisture, and temperature ranges. The mode button cycles between saved plant profiels, so that the same device can be used for plants like basil, photos, snake plant, or other common houseplants

  **Open Source Hardware Learning**
  This project is also meant to be a compelte open source hardware build. It includes a custom PCB, case CAD, firmware files, plant profile database, BOM, and manufacturing exports so that other peoples  can build this as well.

  **Motivation**

  I wanted this project to be more then a normal macropad due to my past expierence. A basic macropad is usefull dont get me wrong, but I wanted this one to feel liek a small standalone with a good purpose. It feels nice because a small project can be turned into a a complex piece of art(kinda lol). 

  The garden probe idae made the project more interestign because it combiens physcial buttons, sensor readings, display outout, custon PCB design, firmware, and a 3D printed enclourese, which btw turned out way better then my last hardware project. Also the goal was to build something usefull to my daliy life, cause I have a LOT of plants at home.

| View | Image |
|---|---|
| Top | <img width="1440" height="900" alt="Screenshot 2026-06-17 at 11 44 27 AM 2" src="https://github.com/user-attachments/assets/ac47262c-fc2d-4806-abad-520eaac7ded3" />
 
| Front | <img width="1440" height="900" alt="Screenshot 2026-06-17 at 11 44 25 AM 2" src="https://github.com/user-attachments/assets/1d4f6df5-2260-412c-9aa8-8360e7d5d417" />
 
| PCB | <img width="1440" height="900" alt="Screenshot 2026-06-17 at 11 51 18 AM 2" src="https://github.com/user-attachments/assets/b316d4bf-769f-46a4-bd23-ed93fb88cc1f" />
 

**Hardware Overview**

The RP2040 controls the switches, OLED dispaly, and soil sensor. The board is powered through the USB-C port. The OlED, and Soil sensor are powered from the XIAOS 3V3 pin. 

The three switches are wired directly from GPIO pins to ground. the firmware uses the resistors inside I believe, so that there is no need for extra wiriing. 


 | Part | Details |
|---|---|
| MCU | Seeed Studio XIAO RP2040 |
| Display | SSD1306 I2C OLED |
| Sensor | I2C capacitive soil sensor |
| Power | USB-C through the XIAO RP2040 |










