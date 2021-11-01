from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeliniumHelper


class LeavePage:

    def __init__(self, driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.navigate_leave()
        self.helper = SeliniumHelper(self.driver)


    def navigate_apply(self):
        element = self.helper.identify_element('//*[@id="menu_leave_applyLeave"]', 'XPATH', 'Apply')
        self.helper.click(element)


    def naviagte_my_leave(self):
        element = self.helper.identify_element('//*[@id="menu_leave_viewMyLeaveList"]', 'XPATH', 'My Leave')
        self.helper.click(element)


if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = LeavePage(driver_mgr.driver)
    obj.navigate_apply()

