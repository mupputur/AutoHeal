from libCommon.driver_manager import DriverManager
from apps.orangeHRM.home_page import HomePage


def test_navigate_admin():
    driver_mgr = DriverManager()
    obj = HomePage(driver_mgr.driver)
    assert obj.navigate_admin()