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
