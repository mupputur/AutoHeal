from libCommon.driver_manager import DriverManager
from admin_page import AdminPage
import os

class UserManagementPage():

    def __init__(self, driver):
        self.driver = driver
        obj = AdminPage(self.driver)
        obj.naviagte_usermanagement()

    def add_user(self):
        pass

    def delete_user(self):
        pass

    def reset_user(self):
        pass

    def search_user(self):
        pass

if __name__ == "__main__":
    driver_mgr = DriverManager()
    obj = UserManagementPage(driver_mgr.driver)
    obj.add_user()