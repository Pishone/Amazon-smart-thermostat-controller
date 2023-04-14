from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import Dependencies.elements as elements
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:udid"] = "213a0b7804017ece"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:appPackage"] = "com.amazon.dee.app"
caps["appium:appActivity"] = ".ui.main.MainActivity"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
time.sleep(5)

caps = {}
caps["platformName"] = "Android"
caps["appium:udid"] = "213a0b7804017ece"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:appPackage"] = "com.github.libretube"
caps["appium:appActivity"] = ".ui.activities.MainActivity"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
time.sleep(5)