import piggy_test_case


class HistoryTest(piggy_test_case.PiggyTestCase):

    def test_case_add_and_check_income(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "1000€")

    def test_case_add_and_check_expense_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "-100000000000000000000€")

    def test_case_add_and_check_expense_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "100000000000000000000€")

    def test_case_add_and_check_expense_decimal_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "100000000000000000000.5€")

    def test_case_add_and_check_expense_decimal_bigger20(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "-100000000000000000000.5€")

    def test_case_add_and_check_expense_negative(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-1000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "1000€")

    def test_case_add_and_check_expense_decimal_negative(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("-0.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "0.5€")

    def test_case_add_and_check_expense_decimal(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("0.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "-0.5€")

    def test_case_add_and_check_income_decimal_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "-100000000000000000000.5€")

    def test_case_add_and_check_income_decimal_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("100000000000000000000.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "100000000000000000000.5€")

    def test_case_add_and_check_income_negative_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "-100000000000000000000€")

    def test_case_add_and_check_income_bigger20(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("100000000000000000000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text,
                         "100000000000000000000€")

    def test_case_add_and_check_income_decimal_negative(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-0.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "-0.5€")

    def test_case_add_and_check_income_decimal(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("0.5")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "0.5€")

    def test_case_add_and_check_income_negative(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon2()
        self.myDevice.enter_numbers("-2000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "-2000€")

    def test_case_edit_history(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.myDevice.click_history_detail()
        self.wait(5)
        self.myDevice.click_history_edit()
        self.wait(5)
        self.myDevice.clear_input()
        self.wait(5)
        self.myDevice.enter_numbers(666)
        self.wait(5)
        self.myDevice.submit()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "666€")

    def test_case_make_expense(self):
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.myDevice.click_history_detail()
        self.wait(5)
        self.myDevice.click_history_make_expense()
        self.wait(5)

        self.assertEqual(self.myDevice.history_data().text, "-1000€")

    def test_case_delete(self):
        # first data
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        # second data
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("999")
        self.myDevice.submit()
        self.wait(5)

        self.myDevice.click_HISTORY()
        self.wait(5)
        self.myDevice.click_history_detail()
        self.wait(5)
        self.myDevice.click_history_delete()
        self.wait(5)
        self.myDevice.click_history_delete_Yes()
        self.wait(5)

        self.assertEqual(self.myDevice.history_data().text, "1000€")

    def test_case_no_delete(self):
        # first data
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)

        # second data
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("999")
        self.myDevice.submit()
        self.wait(5)

        self.myDevice.click_HISTORY()
        self.wait(5)
        self.myDevice.click_history_detail()
        self.wait(5)
        self.myDevice.click_history_delete()
        self.wait(5)
        self.myDevice.click_history_delete_No()
        self.wait(5)

        self.assertEqual(self.myDevice.history_data().text, "-999€")
