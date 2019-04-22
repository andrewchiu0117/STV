import piggy_test_case


class SettingTest(piggy_test_case.PiggyTestCase):

    def test_changecurrencytoMexicanPeso(self):
        self.wait(1)
        self.myDevice.click_SETTINGS()
        self.wait(1)
        self.myDevice.click_Currency()
        self.wait(1)
        self.myDevice.click_Currencytype_MexicanPeso()
        self.assertEqual(
            self.myDevice.Currency_text().text, "Mexican Peso")

    def test_checkCurrency(self):
        self.wait(1)
        self.myDevice.click_SETTINGS()
        self.wait(1)
        self.assertEqual(
            self.myDevice.Currency_text().text, "Euro")

    def test_income(self):
        self.wait(2)
        self.myDevice.click_SETTINGS()
        self.wait(2)
        self.myDevice.click_setting_income()
        self.myDevice.back()
        self.wait(2)
        self.assertEqual(self.myDevice.current_activity(),".Launcher") #.Launcher 代表app crash回到主畫面
