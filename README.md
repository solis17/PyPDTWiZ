# PyPDTWiZ
This repository includes a standalone Graphical User Interface (GUI) application designed to control a radiation instrument that comprises WiZ LED bulbs, developed as part of the research for my Bachelor's Dissertation titled "Optimization of an Irradiation Instrument for Photodynamic Therapy".

## Requirements
- Python
- Windows (64 bit if using.exe file)
- pywizlight
- asyncio
- PyQt5

## Irradiation Instrument System
An irradiation instrument (Figure 1 - left) was created for photodynamic therapy studies. The instrument comprises two “WiZ” LED full colour bulbs (Figure 1 - right) with a wire and a plug so that it can be connected to the electric supply. It also has a light diffusor making the light to be evenly scattered across  the cell culture plate.

![image](https://github.com/user-attachments/assets/6aa4bf9c-0b79-42c8-bb25-59605f89403d)
Figure 1. Irradiation Instrument. (Left) System, and (Right) WiZ LED lamp candle B12 E12.



## GUI application
Firstly, we implemented a Python command-line interface (CLI) that emulated the WiZ mobile phone app, using "pywizlight", a Python connector for WiZ. Although being functional, this text-based program was not much intuitive or user-friendly and quite limited regarding the routines defined for the lamp. The solution was to convert it into a GUI with the Python’s library “PyQt5”. This tool allowed us to create a visual representation of the software in which the user could easily interact through clickable icons 


The application can be used as the software to any instrument that comprises WiZ LED bulbs, offering the user the possibility to customize the irradiated light in terms of wavelength, energy and time.


![image](https://github.com/user-attachments/assets/4acac1c7-e6f0-488c-b2f8-c03aa0895517)


## Usage
1. Download ...
2. Run ...

## License
Free to use, share, and adapt the material, provided proper credit is given.
