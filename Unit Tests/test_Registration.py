# pip install Appium-Python-Client

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import Dependencies.elements as elements
import cli_commands
import time
import serial
import threading
import os
import Dependencies.config as config

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:udid"] = config.mobile_dsn
caps["appium:automationName"] = "UiAutomator2"
caps["appium:appPackage"] = config.app_package
caps["appium:appActivity"] = config.app_activity
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
time.sleep(5)

mobile_logs = "Mobile_Logs"

try:
    os.mkdir(mobile_logs)
except:
    pass
mobile_logs += "/" + str(time.asctime()).replace(" ", "_").replace(":", ".")
print("Mobile Logs will be stored @ " + mobile_logs + ".txt")


def start_mobile_logs():
    driver.get_log('logcat') > mobile_logs + ".txt"


t2 = threading.Thread(target=start_mobile_logs)
t2.daemon = True
t2.start()

ser = serial.Serial()
ser.port = config.serialport
ser.baudrate = 115200
ser.open()
logpath = "Thermostat_Logs"
try:
    os.mkdir(logpath)
except:
    pass
logpath += "/" + str(time.asctime()).replace(" ", "_").replace(":", ".")
print("Logs will be stored @ " + logpath + ".txt")


def start_device_log_capture():
    while True:
        buffer_data = ser.readline().decode('utf-8', errors='ignore')
        if buffer_data != "":
            print(buffer_data)
            log_file = open(logpath + ".txt", "a+")
            log_file.write(''.join([x for x in buffer_data if ord(x) < 128]))
            log_file.close()


t1 = threading.Thread(target=start_device_log_capture)
t1.daemon = True
t1.start()

ser.write((cli_commands.CLI_FULL_FACTORY_RESET + "\r\n").encode())

# Devices Tab
driver.find_element(AppiumBy.ID, elements.devices_tab).click()
driver.implicitly_wait(10)

# Add Thermostat
driver.find_element(AppiumBy.XPATH, elements.add_thermostat).click()
driver.implicitly_wait(10)

# Setup Thermostat
driver.find_element(AppiumBy.XPATH, elements.setup_thermostats_button).click()
driver.implicitly_wait(10)

# Brand Selection Screen
driver.find_element(AppiumBy.XPATH, elements.brand_amazon).click()
driver.implicitly_wait(10)

# Has your new thermostat been already installed?
driver.find_element(AppiumBy.XPATH, elements.yes_button).click()
driver.implicitly_wait(10)

# Is your thermostat display on?
driver.find_element(AppiumBy.XPATH, elements.yes_button).click()
driver.implicitly_wait(10)

# Lets connect to Alexa
driver.find_element(AppiumBy.XPATH, elements.next_button).click()
driver.implicitly_wait(10)

# Give App permission
driver.find_element(AppiumBy.XPATH, elements.allow_button).click()
driver.implicitly_wait(10)

# Locate QR
driver.find_element(AppiumBy.XPATH, elements.no_barcode).click()
driver.implicitly_wait(10)

# Connect thermostat
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

# Select Wi-fi
driver.implicitly_wait(120)
driver.find_element(AppiumBy.XPATH, elements.wifi_the_boys).click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

# Device Conntected
driver.implicitly_wait(60)
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

# Group page
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.skip_button).click()

# HVAC Configuration
driver.implicitly_wait(40)
driver.find_element(AppiumBy.XPATH, elements.R).click()
driver.find_element(AppiumBy.XPATH, elements.C).click()
driver.find_element(AppiumBy.XPATH, elements.G).click()
driver.find_element(AppiumBy.XPATH, elements.W).click()
driver.find_element(AppiumBy.XPATH, elements.Y).click()
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

driver.find_element(AppiumBy.XPATH, elements.next_button).click()
driver.implicitly_wait(10)

# Forced Air
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.yes_button).click()

# Select Furnace Page
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.electric_furnace).click()
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

# Test your thermostat
driver.implicitly_wait(40)
driver.find_element(AppiumBy.XPATH, elements.next_button).click()

# Heat On?
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.yes_heat_is_on).click()

# Fan On?
driver.implicitly_wait(20)
driver.find_element(AppiumBy.XPATH, elements.yes_fan_is_on).click()

driver.start_recording_screen()

# Humches or Schedules during OOBE
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.later_button).click()

# Learn about thermostat
driver.implicitly_wait(15)
driver.find_element(AppiumBy.XPATH, elements.next_button).click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, elements.done_button).click()

driver.stop_recording_screen()
driver.quit()
