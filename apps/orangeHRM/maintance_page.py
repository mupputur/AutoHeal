__author__= "Padmavathi (<padmavathi19>)"
from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeleniumHelper


class MaintancePage:

    def __init__(self,driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.naviagte_maintance()
        self.helper = SeleniumHelper(self.driver)

    def navigate_purge_records(self,purge_record_type):
        element = self.helper.identify_element('menu_maintenance_PurgeRecords', 'ID', 'purge records')
        self.helper.click(element)
        if purge_record_type == "Employee Records":
            element = self.helper.identify_element('menu_maintenance_purgeEmployee', 'ID', 'Employee Records')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('menu_maintenance_purgeCandidateData', 'ID', 'Candidate Records')
            self.helper.click(element)
        return element

    def navigate_access_records(self):
        element = self.helper.identify_element('menu_maintenance_accessEmployeeData', 'ID', 'Access Records')
        self.helper.click(element)

if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = MaintancePage(driver_mgr.driver)
    obj.navigate_purge_records("Candidates Records")
    obj.navigate_access_records()