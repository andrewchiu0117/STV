import piggy_test_case

class HistoryTest(piggy_test_case.PiggyTestCase):
    
    def test_case_1(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-1000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-1000€")
    
    def test_case_2(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-1000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-1000€")