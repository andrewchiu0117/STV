import piggy_test_case


class HomeTestISP(piggy_test_case.PiggyTestCase):

    def test_case_expense_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "-100000000000000000000€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "-100000000000000000000€")

    def test_case_expense_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "100000000000000000000€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "100000000000000000000€")

    def test_case_expense_decimal_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "100000000000000000000.5€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "100000000000000000000.5€")

    def test_case_expense_decimal_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "-100000000000000000000.5€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "-100000000000000000000.5€")

    def test_case_expense_negative(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-1000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "1000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "1000€")

    def test_case_expense_decimal_negative(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-0.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0.5€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0.5€")

    def test_case_expense_decimal(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("0.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-0.5€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-0.5€")

    def test_case_income_decimal_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "-100000000000000000000.5€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "-100000000000000000000.5€")

    def test_case_income_decimal_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "100000000000000000000.5€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "0100000000000000000000.5€")

    def test_case_income_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "-100000000000000000000€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "-100000000000000000000€")

    def test_case_income_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text,
                         "100000000000000000000€")
        self.assertEqual(self.myDevice.today_budget_text().text,
                         "100000000000000000000€")

    def test_case_income_decimal_negative(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-0.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-0.5€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-0.5€")

    def test_case_income_decimal(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("0.5")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0.5€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0.5€")

    def test_case_income_negative(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-2000")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "-2000€")
        self.assertEqual(self.myDevice.today_budget_text().text, "-2000€")

    def test_case_expense_zero_decimal(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("0.0")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0€")

    def test_case_expense_zero_decimal_1(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers(".0")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0€")

    def test_case_income_zero_decimal(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("0.0")
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.total_budget_text().text, "0€")
        self.assertEqual(self.myDevice.today_budget_text().text, "0€")

    def test_case_income_zero_decimal_1(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers(".0")
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
