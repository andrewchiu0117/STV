from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import test_history
import unittest
import time


def main():
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromName('test_home.HomeTest'),
        unittest.TestLoader().loadTestsFromName('test_history.HistoryTest'), 
        unittest.TestLoader().loadTestsFromName("test_settings.SettingTest")
        ]
    suite.addTests(tests)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

    time.sleep(5)
    print("testsRun:%s" % test_result.testsRun)
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))


if __name__ == '__main__':
    main()
