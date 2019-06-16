import piggy_test_case


class StatsTest(piggy_test_case.PiggyTestCase):

    def test_daily_expenses_button_week(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_daily_expenses_week()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_expenses_button_month(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_daily_expenses_month()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_income_button_week(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_daily_income_week()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_income_button_month(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_daily_income_month()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_distribution_button_week(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_distribution_expenses_week()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_distribution_button_month(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_distribution_expenses_month()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())

    def test_daily_distribution_button_year(self):
        self.wait(1)
        self.myDevice.click_stats()
        self.wait(1)
        self.myDevice.click_stats_distribution_expenses_year()
        self.wait(1)
        self.assertFalse(self.myDevice.crash())