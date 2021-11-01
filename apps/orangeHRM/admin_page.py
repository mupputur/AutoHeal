
from home_page import HomePage

class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        obj = HomePage(self.driver)
        obj.navigate_admin()

    def naviagte_usermanagement(self):
        pass

    def naviagte_job(self):
        pass

    def naviagte_qualifications(self):
        pass

    def naviagte_nationalities(self):
        pass

    def naviagte_configuration(self):
        pass

if __name__ == "__main__":

    obj = AdminPage()
    obj.naviagte_usermanagement()