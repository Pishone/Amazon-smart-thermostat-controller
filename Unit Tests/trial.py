from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import Dependencies.elements as elements
import time
import pytest
import Dependencies.config as config

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Test_Snyder():

    @pytest.fixture
    def bootup(self):
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
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
        time.sleep(5)
        yield
        self.driver.quit()

    def test_terminal_select_deselect(self, bootup):
        
        # Devices Tab
        self.driver.find_element(AppiumBy.ID, elements.devices_tab).click()
        self.driver.implicitly_wait(10)

        # Add Thermostat
        self.driver.find_element(AppiumBy.XPATH, elements.add_thermostat).click()
        self.driver.implicitly_wait(10)

        # Setup Thermostat
        self.driver.find_element(AppiumBy.XPATH, elements.setup_thermostats_button).click()
        self.driver.implicitly_wait(10)

        # Brand Selection Screen
        self.driver.find_element(AppiumBy.XPATH, elements.brand_amazon).click()
        self.driver.implicitly_wait(10)

        # Has your new thermostat been already installed?
        self.driver.find_element(AppiumBy.XPATH, elements.no_button).click()
        self.driver.implicitly_wait(10)

        # Install your Amazon Smart Thermostat
        self.driver.find_element(AppiumBy.XPATH, elements.next_button).click()
        self.driver.implicitly_wait(10)

        # Let's check your wiring
        self.driver.find_element(AppiumBy.XPATH, elements.next_button).click()
        self.driver.implicitly_wait(10)

        # Turn off power
        self.driver.find_element(AppiumBy.XPATH, elements.next_button).click()
        self.driver.implicitly_wait(10)

        # Carefully remove Old thermostat
        self.driver.find_element(AppiumBy.XPATH, elements.next_button).click()
        self.driver.implicitly_wait(10)

        # Check for High voltage
        self.driver.find_element(AppiumBy.XPATH, elements.no_high_voltage_button).click()
        self.driver.implicitly_wait(10)

        # Take photo of old wiring
        self.driver.find_element(AppiumBy.XPATH, elements.skip_button).click()
        self.driver.implicitly_wait(10)

        # HVAC Config
        
        #Scroll
        actions = ActionChains(self.driver)
        actions(self.driver).press(x=930, y=1350).move_to_location(x=930, y=930).release().perform()
        self.driver.implicitly_wait(10)

        self.driver.find_element(AppiumBy.XPATH, elements.R).click()
        self.driver.find_element(AppiumBy.XPATH, elements.C).click()
        self.driver.find_element(AppiumBy.XPATH, elements.G).click()
        self.driver.find_element(AppiumBy.XPATH, elements.W).click()
        self.driver.find_element(AppiumBy.XPATH, elements.Y).click()
        self.driver.find_element(AppiumBy.XPATH, elements.next_button).click()


        
