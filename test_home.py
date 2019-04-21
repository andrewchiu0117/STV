import device
import time
import unittest

class HomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #print("processing...")
        self.cal=device.Device()

    @classmethod
    def tearDownClass(self):
        self.cal.close()
        time.sleep(10)
    # def __init__(self,testname):
    #     print("processing...")
    #     self.cal=device.Device()
        

    # def setUp(self):
    #     self.cal.restart()
    
    # def tearDown(self):
    #     self.cal=None
    
    def test_case_1(self):
        time.sleep(5)
        self.cal.click_expense()
        time.sleep(5)
        self.cal.click_icon1()
        self.cal.enter_numbers("1000")
        self.cal.submit()
        time.sleep(5)
        self.assertEqual(self.cal.total_budget_text().text, "-1000€")
        self.assertEqual(self.cal.today_budget_text().text, "-1000€")
    
    def test_case_2(self):
        time.sleep(5)
        self.cal.click_income()
        time.sleep(5)
        self.cal.click_icon2()
        self.cal.enter_numbers("2000")
        self.cal.submit()
        time.sleep(5)
        self.assertEqual(self.cal.total_budget_text().text, "1000€")
        self.assertEqual(self.cal.today_budget_text().text, "1000€")