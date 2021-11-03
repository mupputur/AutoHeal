from libCommon.selenium_helper import SeliniumHelper


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeliniumHelper(self.driver)

    def navigate_admin(self):
        element = self.helper.identify_element('menu_admin_viewAdminModule', 'ID', 'Admin')
        self.helper.click(element)

    def navigate_pim(self):
        element = self.helper.identify_element("menu_pim_viewPimModule", 'ID', 'PIM')
        self.helper.click(element)

    def navigate_leave(self):
        element = self.helper.identify_element('//*[@id="menu_leave_viewLeaveModule"]/b', 'XPATH', 'Leave')
        self.helper.click(element)

    def navigate_time(self):
        element = self.helper.identify_element('menu_time_viewTimeModule', 'ID', 'TIME')
        self.helper.click(element)

    def navigate_recruitment(self):
        element = self.helper.identify_element("//b[contains(text(),'Recruitment')]", 'XPATH', 'NAVIGATE RECRUITMENT')
        self.helper.click(element)

    def navigate_myinfo(self):
        element = self.helper.identify_element("//b[contains(text(),'My Info')]", 'XPATH', 'MY INFO')
        self.helper.click(element)

    def navigate_performance(self):
        element = self.helper.identify_element("//b[contains(text(),'Performance')]", 'XPATH', 'PERFORMANCE')
        self.helper.click(element)

    def naviagte_dashboard(self):
        element = self.helper.identify_element("//b[contains(text(),'Dashboard')]", 'XPATH', 'DASHBOARD')
        self.helper.click(element)

    def navigate_directory(self):
        element = self.helper.identify_element('menu_directory_viewDirectory', 'ID', 'Directory')
        self.helper.click(element)

    def naviagte_maintance(self):
        element = self.helper.identify_element('menu_maintenance_purgeEmployee', 'ID', 'Maintainance')
        self.helper.click(element)

    def naviagte_buzz(self):
        element = self.helper.identify_element('menu_buzz_viewBuzz', 'ID', 'Buzz')
        self.helper.click(element)

if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()

    obj = HomePage(driver_mgr.driver)

    obj.navigate_admin()
    obj.naviagte_pim()
    obj.navigate_leave()
    obj.navigate_time()
    obj.navigate_recruitment()
    obj.navigate_myinfo()
    obj.navigate_performance()
    obj.naviagte_dashboard()
    obj.navigate_directory()
    obj.naviagte_maintance()
    obj.naviagte_buzz()