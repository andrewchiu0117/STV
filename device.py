from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xpath
import time


class Device:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = 'HTC_X9u'
        # desired_caps['platformVersion'] = '7.1.1'
        # desired_caps['deviceName'] = 'Xperia M4 Aqua(AOSP)'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'Xperia Z3C'
        desired_caps['appPackage'] = 'de.php_tech.piggybudget'
        desired_caps['appActivity'] = 'de.php_tech.piggybudget.MainActivity'
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 20)

    def close(self):
        self.driver.quit()

    def click_expense(self):
        try:
            expense_btn = WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((By.XPATH, xpath.expense_xpath)))
            expense_btn.click()
        except TimeoutError:
            print('wait error, no expense_btn')

    def click_income(self):
        try:
            income_btn = WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((By.XPATH, xpath.income_xpath)))
            income_btn.click()
        except TimeoutError:
            print('wait error, no income_btn')

    def total_budget_text(self):
        vision = EC.visibility_of_element_located(
            (By.XPATH, xpath.total_budget_xpath))
        total_budget = self.wait.until((vision), "wait error, no total_budget")
        return total_budget

    def today_budget_text(self):
        vision = EC.visibility_of_element_located(
            (By.XPATH, xpath.today_budget_xpath))
        today_budget = self.wait.until((vision), "wait error, no today_budget")
        return today_budget

    def btn(self):
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
        el2.click()

    def click_icon1(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_1))
        Icon_1 = self.wait.until((vision), "wait error, no Icon_1")
        # Icon_1 = self.driver.find_element_by_xpath(xpath.Icon_1)
        Icon_1.click()

    def click_icon2(self):
        # vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_2))
        # Icon_2 = self.wait.until((vision),"wait error, no Icon_2")
        Icon_2 = self.driver.find_element_by_xpath(xpath.Icon_2)
        Icon_2.click()

    def click_icon3(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_3))
        Icon_3 = self.wait.until((vision), "wait error, no Icon_3")
        Icon_3.click()

    def click_icon4(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_4))
        Icon_4 = self.wait.until((vision), "wait error, no Icon_4")
        Icon_4.click()

    def click_icon5(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_5))
        Icon_5 = self.wait.until((vision), "wait error, no Icon_5")
        Icon_5.click()

    def click_icon6(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_6))
        Icon_6 = self.wait.until((vision), "wait error, no Icon_6")
        Icon_6.click()

    def click_icon7(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_7))
        Icon_7 = self.wait.until((vision), "wait error, no Icon_7")
        Icon_7.click()

    def click_icon8(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_8))
        Icon_8 = self.wait.until((vision), "wait error, no Icon_8")
        Icon_8.click()

    def click_icon9(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_9))
        Icon_9 = self.wait.until((vision), "wait error, no Icon_9")
        Icon_9.click()

    def click_icon10(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_10))
        Icon_10 = self.wait.until((vision), "wait error, no Icon_10")
        Icon_10.click()

    def click_icon11(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_11))
        Icon_11 = self.wait.until((vision), "wait error, no Icon_11")
        Icon_11.click()

    def click_icon12(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Icon_12))
        Icon_12 = self.wait.until((vision), "wait error, no Icon_12")
        Icon_12.click()

    def enter_numbers(self, txt):
        el3 = self.driver.find_element_by_xpath(xpath.input_number)
        el3.send_keys(txt)

    def submit(self):
        self.driver.press_keycode(66)

    def restart(self):
        # self.driver.close_app()
        self.driver.reset()
        time.sleep(5)
        self.driver.launch_app()

    def end_test_coverage(self):
        return self.driver.end_test_coverage("intent", "path")

    def current_activity(self):
        return self.driver.current_activity

    def crash(self):
        if "Launcher" not in self.driver.current_activity:
            return False
        else:
            return True

    def click_SETTINGS(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.SETTINGS))
        SETTINGS = self.wait.until((vision), "wait error, no SETTINGS")
        SETTINGS.click()

    def click_Currency(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Currency))
        SETTINGS = self.wait.until((vision), "wait error, no Currency")
        SETTINGS.click()

    def click_Currencytype_MexicanPeso(self):
        vision = EC.visibility_of_element_located(
            (By.XPATH, xpath.Currencytype_MexicanPeso))
        SETTINGS = self.wait.until((vision), "wait error, no Currencytype_MexicanPeso")
        SETTINGS.click()

    def Currency_text(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Currency))
        SETTINGS = self.wait.until((vision), "wait error, no Currency_text")
        return SETTINGS

    def click_HISTORY(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HISTORY))
        HISTORY = self.wait.until((vision), "wait error, no HISTORY")
        HISTORY.click()

    def history_data(self):
        vision = EC.visibility_of_element_located(
            (By.XPATH, xpath.HistoryData))
        data = self.wait.until((vision), "wait error, no history data")
        return data

    def click_history_detail(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataDetail))
        HISTORY = self.wait.until((vision), "wait error, no history detail")
        HISTORY.click()

    def click_history_edit(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataEdit))
        HISTORY = self.wait.until((vision), "wait error, no history edit")
        HISTORY.click()

    def click_history_make_expense(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataMakeExpense))
        HISTORY = self.wait.until((vision), "wait error, no history make expense")
        HISTORY.clear()

    def click_history_delete(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataDelete))
        HISTORY = self.wait.until((vision), "wait error, no history delete")
        HISTORY.clear()
    
    def click_history_delete_Yes(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataDeleteYes))
        HISTORY = self.wait.until((vision), "wait error, no history delete yes")
        HISTORY.clear()

    def click_history_delete_No(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.HistoryDataDeleteNo))
        HISTORY = self.wait.until((vision), "wait error, no history delete no")
        HISTORY.clear()


    def clear_input(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.input_number))
        HISTORY = self.wait.until((vision), "wait error, no clear input")
        HISTORY.clear()

    def enter_setting_income(self, txt):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Income))
        Income = self.wait.until((vision), "wait error, no Income")
        Income.send_keys(txt)

    def click_setting_income(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.Income))
        Income = self.wait.until((vision), "wait error, no Income")
        Income.click()

    def click_stats(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats))
        stats = self.wait.until((vision), "wait error, no stats")
        stats.click()

    def click_stats_daily_expenses_week(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_daily_expenses_week))
        stats = self.wait.until((vision), "wait error, no stats_daily_expenses_week")
        stats.click()

    def click_stats_daily_expenses_month(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_daily_expenses_month))
        stats = self.wait.until((vision), "wait error, no stats_daily_expenses_month")
        stats.click()

    def click_stats_daily_income_week(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_daily_income_week))
        stats = self.wait.until((vision), "wait error, no stats_daily_income_week")
        stats.click()

    def click_stats_daily_income_month(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_daily_income_month))
        stats = self.wait.until((vision), "wait error, no stats_stats_daily_income_month")
        stats.click()
        
    def click_stats_distribution_expenses_week(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_distribution_week))
        stats = self.wait.until((vision), "wait error, no stats_distribution_expenses_week")
        stats.click()

    def click_stats_distribution_expenses_month(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_distribution_month))
        stats = self.wait.until((vision), "wait error, no stats_distribution_expenses_month")
        stats.click()

    def click_stats_distribution_expenses_year(self):
        vision = EC.visibility_of_element_located((By.XPATH, xpath.stats_distribution_year))
        stats = self.wait.until((vision), "wait error, no stats_distribution_expenses_year")
        stats.click()

    def back(self):
        self.driver.press_keycode(67)
