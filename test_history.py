import piggy_test_case

class HistoryTest(piggy_test_case.PiggyTestCase):
    
    def test_case_add_and_check(self):
        self.wait(5)
        self.myDevice.click_expense()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        self.myDevice.click_HISTORY()
        self.wait(5)
        self.assertEqual(self.myDevice.history_data().text, "-1000€")
    
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
        #first data
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)
        #second data
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
        #first data
        self.wait(5)
        self.myDevice.click_income()
        self.wait(5)
        self.myDevice.click_icon1()
        self.myDevice.enter_numbers("1000")
        self.myDevice.submit()
        self.wait(5)

        #second data
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

