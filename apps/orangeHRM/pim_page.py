__author__= "Kishore P (krsna-krish)"

from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeliniumHelper

class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.navigate_pim()
        self.helper = SeliniumHelper(self.driver)

    def navigate_configuration(self):
        element = self.helper.identify_element('menu_pim_Configuration', 'ID', 'Configuration')
        self.helper.click(element)

    def navigate_employee_list(self):
        element = self.helper.identify_element('menu_pim_viewEmployeeList', 'ID', 'Employee List')
        self.helper.click(element)

    def navigate_add_employee(self):
        element = self.helper.identify_element('menu_pim_addEmployee', 'ID', 'Add Employee')
        self.helper.click(element)

    def navigate_reports(self):
        element = self.helper.identify_element('menu_core_viewDefinedPredefinedReports', 'ID', 'Add Employee')
        self.helper.click(element)



if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = PIMPage(driver_mgr.driver)
    obj.navigate_configuration()
    obj.navigate_employee_list()
    obj.navigate_add_employee()
    obj.navigate_reports()