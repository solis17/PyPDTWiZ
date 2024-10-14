# PyPDTWiZ
This repository includes a standalone Graphical User Interface (GUI) application designed to control a radiation instrument that comprises WiZ LED bulbs, developed as part of the research for my Bachelor's Dissertation titled "Optimization of an Irradiation Instrument for Photodynamic Therapy".

## Requirements
- Python
- Windows (64 bit if using.exe file)
- pywizlight
- asyncio
- PyQt5

## Irradiation Instrument System
An irradiation instrument (Figure 1 - left) was created for photodynamic therapy studies. The instrument comprises two “WiZ” LED full-colour bulbs (Figure 1 - right) with a wire and a plug to be connected to the electric supply. It also has a light diffusor making the light evenly scattered across  the cell culture plate.
These types of bulbs have several important aspects: colour and intensity control and Wi-Fi connection. It is possible to select from a wide range of colour options and there is the choice to customize the brightness of the light. Another important feature is the use of smart WiFi technology, meaning that a smartphone can control the light bulb once connected to an available Wi-Fi network via the “WiZ” mobile app.  

![image](https://github.com/user-attachments/assets/6aa4bf9c-0b79-42c8-bb25-59605f89403d)
Figure 1. Irradiation Instrument. (Left) System, and (Right) WiZ LED lamp candle B12 E12.

## GUI application
Firstly, we implemented a Python command-line interface (CLI) that emulated the WiZ mobile phone app, using "pywizlight", a Python connector for WiZ. Although being functional, this text-based program was not very intuitive or user-friendly and quite limited regarding the routines defined for the lamp. The solution was to convert it into a GUI with the Python’s library “PyQt5”. This tool allowed us to create a visual representation of the software in which the user could easily interact through clickable icons. 
After designing and achieving a working and user-friendly GUI program, it was crucial to make it optimal for future phototherapy studies. This meant analysing the instrument’s characteristics to find the relation between the levels of brightness and colour of the lamps and the wavelength and energy of the irradiated light, something that is explained in the pdf document of this repository.

![image](https://github.com/user-attachments/assets/9d500e97-f198-4678-ab58-7af259db999d)
Figure 2. Final graphic user interface (GUI) display.

## Usage
1. Download ...
2. Run ...

## License
Free to use, share, and adapt the material, provided proper credit is given.
