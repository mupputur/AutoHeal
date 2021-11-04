__author__= "Anitha (<anitha1996>)"
from libCommon.selenium_helper import SeleniumHelper
from apps.orangeHRM.home_page import HomePage
import time

class DirectoryPage:

    def __init__(self, driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.navigate_directory()
        self.helper = SeleniumHelper(self.driver)

    def search(self, search_text):
        element1 = self.helper.identify_element("searchDirectory_emp_name_empName", "ID", "directory")
        self.helper.send_text(element1, search_text)
        element2 = self.helper.identify_element("searchBtn", "ID", "search")
        self.helper.click(element2)


    def reset(self):
        element = self.helper.identify_element("resetBtn", "ID", "reset")
        self.helper.click(element)


if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    # driver_mgr is the DriverManager class object and driver is the attribute which is defined
    obj = DirectoryPage(driver_mgr.driver)
    obj.search("Kallyani Bhute")
    time.sleep(10)
    obj.reset()

