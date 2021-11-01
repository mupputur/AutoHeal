from libCommon.driver_manager import DriverManager
from apps.orangeHRM.user_management_page import UserManagementPage


def test_create_user():
    driver_mgr = DriverManager()
    obj = UserManagementPage(driver_mgr.driver)
    obj.add_user()