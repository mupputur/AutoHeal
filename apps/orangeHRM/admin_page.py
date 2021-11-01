__author__ = "Suryateja K (Surya9856)"

from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeliniumHelper


class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        obj = HomePage(self.driver)
        obj.navigate_admin()
        self.helper = SeliniumHelper(self.driver)

    def navigate_user_management(self):
        element = self.helper.identify_element('menu_admin_UserManagement', 'ID', 'USER MANAGEMENT')
        self.helper.click(element)

    def navigate_job(self):
        element = self.helper.identify_element('menu_admin_Job', 'ID', 'JOB')
        self.helper.click(element)

    def navigate_organisations(self):
        element = self.helper.identify_element('menu_admin_Organization', 'ID', 'ADMIN ORGANISATION')
        self.helper.click(element)

    def navigate_qualifications(self):
        element = self.helper.identify_element('menu_admin_Qualifications', 'ID', 'QUALIFICATIONS')
        self.helper.click(element)

    def navigate_nationalities(self):
        element = self.helper.identify_element('menu_admin_nationality', 'ID', 'NATIONALITIES')
        self.helper.click(element)

    def navigate_configuration(self):
        element = self.helper.identify_element('menu_admin_Configuration', 'ID', 'CONFIGURATION')
        self.helper.click(element)


if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = AdminPage(driver_mgr.driver)
    obj.navigate_user_management()
    obj.navigate_job()
