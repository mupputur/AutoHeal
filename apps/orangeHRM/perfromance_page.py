__author__= "Rakesh (<git user name>)"
# class PerfromancePage:
#
#     def __init__(self):
#         pass
#
#     def naviagte_configure(self):
#         pass
#
#     def naviagte_my_trackers(self):
#         pass
#
#     def navigate_employee_trackers(self):
#         pass
#
#     def manage_reviews(self):
#         pass
#
#
# if __name__ == "__main__":
#     obj = PerfromancePage()
#     obj.navigate_employee_trackers()
from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeliniumHelper


class PerformancePage:

    def __init__(self,driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.navigate_performance()
        self.helper = SeliniumHelper(self.driver)
        self.driver.implicitly_wait(3)

    def navigate_configure(self,configure):
        element = self.helper.identify_element('//*[@id="menu_performance_Configure"]','XPATH','configure')
        self.helper.click(element)

        if  configure == "kips":
            element = self.helper.identify_element('//*[@id="menu_performance_searchKpi"]','XPATH','kips')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('//*[@id="menu_performance_addPerformanceTracker"]','XPATH','mytrackers')
            self.helper.click(element)
        return element


    def naviagte_manage_reviews(self,manage_reviews):
        element = self.helper.identify_element('//*[@id="menu_performance_ManageReviews"]','XPATH','manage_reviews')
        self.helper.click(element)

        if manage_reviews == "manage_reviews":
            element = self.helper.identify_element('//*[@id="menu_performance_searchPerformancReview"]','XPATH','manage_reviews')
            self.helper.click(element)
        elif manage_reviews == "my_reviews":
            element = self.helper.identify_element('//*[@id="menu_performance_myPerformanceReview"]','XPATH','my_reviews')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('//*[@id="menu_performance_searchEvaluatePerformancReview"]','XPATH','review_list')
            self.helper.click(element)

    def navigate_my_trackers(self):
        element = self.helper.identify_element('//*[@id="menu_performance_viewMyPerformanceTrackerList"]','XPATH','mytrackers')
        self.helper.click(element)
    def empolyee_trackers(self):
        element = self.helper.identify_element('//*[@id="menu_performance_viewEmployeePerformanceTrackerList"]','XPATH','empolyee_trackers')
        self.helper.click(element)


if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = PerformancePage(driver_mgr.driver)
    obj.navigate_configure('kips')
    obj.naviagte_manage_reviews('manage_reviews')
    obj.navigate_my_trackers()
    obj.empolyee_trackers()
