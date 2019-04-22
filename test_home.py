import piggy_test_case

class HomeTest(piggy_test_case.PiggyTestCase):
    
    def test_case_expense(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-1000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-1000€")
    
    def test_case_income(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("2000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "2000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "2000€")

    def test_case_expense_zero(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("0")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0€")

    def test_case_income_zero(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("0")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0€")


    def test_case_expense_txt(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("ccc")
        self.myDevice.submit()
        self.wait(5)
        # self.assertEqual(self.myDevice.current_activity(),".Launcher") #.Launcher 代表app crash回到主畫面
        self.assertTrue(self.myDevice.crash())

