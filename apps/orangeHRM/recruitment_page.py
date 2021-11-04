__author__= "Padamja (<Padmaja-24>)"
from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeleniumHelper


class RecruitmentPage:
    def __init__(self,driver):
        self.driver = driver
        home_page = HomePage(self.driver)
        home_page.navigate_recruitment()
        self.helper=SeleniumHelper(self.driver)

    def naviagte_candidates(self):
        element = self.helper.identify_element('menu_recruitment_viewCandidates', 'ID', 'Candidates')
        self.helper.click(element)

    def navigate_vacancies(self):
        element = self.helper.identify_element('menu_recruitment_viewJobVacancy', 'ID', 'Vacancies')
        self.helper.click(element)



if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = RecruitmentPage(driver_mgr.driver)
    obj.naviagte_candidates()
    obj.navigate_vacancies()

