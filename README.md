# Amazon-Smart-thermostat-controller
Script to automate Amazon Smart Thermostat with Amazon Alexa App using Python and Appium

![image](https://user-images.githubusercontent.com/89649425/231803924-dd1b46a4-719c-4c53-9797-ab419f91970e.png)

Amazon Smart thermostat is a cheap yet good and comfortable thermostat for personal use. You can read Tom's review of ther thermostat [here](https://fijars.blogspot.com/2021/11/amazon-smart-thermostat-review-toms.html).

This project is my atempt at learning automation of mobile apps using Python-Appium and PyTest. Full automation is not possible, a manual part is necessary for scenario such as changing location on map or reading an image and processing data given in the image. Keeping this in mind, I automated scenarios that takes up a lot of time to test.

### Hardwares needed
- Amazon Smart thermostat (Obviously)
- Debug board (has power supply and serial port outlet)
- UART cable (USB TTY FTDI cable to communicate with thermostat)
- Step Down Transforer

Fix the thermostat in debug board. Connect UART cable to PC and serial port in the debug board. Power on the dubug board using a step down transformer. (Thermostat can't handle heavy loads)

### Libraries / Modules used:

