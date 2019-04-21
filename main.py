from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
#import test_home,test_history
import device
# {
#   "deviceName": "HTC_X9u",
#   "udid": "HT63BBK02833",
#   "platformName": "Android",
#   "platformVersion": "6.0",
#   "appPackage": "de.php_tech.piggybudget",
#   "appActivity": "de.php_tech.piggybudget.MainActivity"
# }


def main():
    # cal=device.Device()
    # cal2=device.Device()
    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromName(
        'test_home.HomeTest'), unittest.TestLoader().loadTestsFromName(
        'test_history.HistoryTest')]
    suite.addTests(tests)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    



    time.sleep(5)
    print("testsRun:%s" % test_result.testsRun) 
    print("failures:%s" % len(test_result.failures)) 
    print("errors:%s" % len(test_result.errors)) 
    print("skipped:%s" % len(test_result.skipped))

    # suite = unittest.TestLoader().loadTestsFromTestCase(test_history.HistoryTest)
    # unittest.TextTestRunner().run(suite)
    # unittest.main()

if __name__ == '__main__':
    main()