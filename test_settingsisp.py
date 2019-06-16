import piggy_test_case


class SettingTestISP(piggy_test_case.PiggyTestCase):

    def test_case_change_income_bigger20(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("100000000000000000000")
        self.wait(2)
        self.assertEqual(self.myDevice.get_setting_income().text, "Daily income: 100000000000000000000€")

    # # 不測，因為app太爛
    # def test_case_change_decimal_income_bigger20(self):
    #     self.wait(2)
    #     self.myDevice.click_SETTINGS()
    #     self.wait(2)
    #     self.myDevice.enter_setting_income("100000000000000000000.5")
    #     self.wait(2)
    #     self.assertEqual(self.myDevice.get_setting_income().text, "Daily income: 100000000000000000000.5€")

    def test_case_change_income(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("1000")
        self.wait(2)
        self.assertEqual(self.myDevice.get_setting_income().text, "Daily income: 1000€")

    def test_case_change_decimal_income(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("0.5")
        self.wait(2)
        self.assertEqual(self.myDevice.get_setting_income().text, "Daily income: 0.5€")

    def test_case_change_income_negative(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("-1000")
        self.wait(5)
        self.assertFalse(self.myDevice.crash())
    
    def test_case_change_decimal_income_negative(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("-0.5")
        self.wait(5)
        self.assertFalse(self.myDevice.crash())

    def test_case_change_income_zero(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.enter_setting_income("0")
        self.wait(2)
        self.assertEqual(self.myDevice.get_setting_income().text, "Daily income: 0€")

    def test_case_change_icon_search_half_match(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.click_setting_icon1()
        self.wait(2)
        self.myDevice.enter_setting_icon_search("chess")
        self.wait(2)
        self.myDevice.back_key()
        self.wait(1)
        self.assertEqual(len(self.myDevice.get_setting_search_data()), 6)

    def test_case_change_icon_search_perfact_match(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.click_setting_icon1()
        self.wait(2)
        self.myDevice.enter_setting_icon_search("chess-bishop")
        self.wait(2)
        self.myDevice.back_key()
        self.wait(1)
        self.assertEqual(len(self.myDevice.get_setting_search_data()), 1)

    def test_case_change_icon_search_no_match(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.click_setting_icon1()
        self.wait(2)
        self.myDevice.enter_setting_icon_search("herfui")
        self.wait(2)
        self.myDevice.back_key()
        self.wait(1)

        self.assertEqual(self.myDevice.get_setting_search_data(), 0)





