import device
import time
import unittest

class HistoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #print("processing2...")
        self.cal=device.Device()

    @classmethod
    def tearDownClass(self):
        self.cal.close()
    # def __init__(self,testname):
    #     print("processing2...")
    #     self.cal=device.Device()

    def setUp(self):
        self.cal.restart()
    
    # def tearDown(self):
    #     self.cal=None
    
    def test_case_1(self):
        #print("test_case_1 processing...")
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
        #print("test_case_2 processing...")
        time.sleep(5)
        self.cal.click_expense()
        time.sleep(5)
        self.cal.click_icon1()
        self.cal.enter_numbers("1000")
        self.cal.submit()
        time.sleep(5)
        self.assertEqual(self.cal.total_budget_text().text, "-2000€")
        self.assertEqual(self.cal.today_budget_text().text, "-2000€")