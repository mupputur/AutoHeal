__author__= "Deepika (<deepikakummari>)"

import time

from apps.orangeHRM.home_page import HomePage
from libCommon.selenium_helper import SeliniumHelper


class TimePage:

    def __init__(self,driver):
        self.driver = driver
        obj = HomePage(self.driver)
        obj.navigate_time()
        self.helper = SeliniumHelper(self.driver)

    def naviagte_time_sheet(self, mytime_sheets):
        self.my_timesheets=mytime_sheets
        element = self.helper.identify_element('menu_time_Timesheets', 'ID', 'time_sheets')
        self.helper.click(element)
        if mytime_sheets == "My TimeSheets":
            element = self.helper.identify_element('menu_time_viewMyTimesheet', 'ID', 'my_sheets')
            self.helper.click(element)
            time.sleep(3)
        else :
            element = self.helper.identify_element('menu_time_viewEmployeeTimesheet', 'ID', 'my_employe')
            self.helper.click(element)
            time.sleep(3)

    def navigate_attendance(self, attendence):
        element = self.helper.identify_element('menu_attendance_Attendance', 'ID', 'menu_atten')
        self.helper.click(element)
        if attendence == "My Records":
            element = self.helper.identify_element('menu_attendance_viewMyAttendanceRecord','ID','menu_record')
            self.helper.click(element)
        elif attendence == "Punch In/Out":
            element = self.helper.identify_element('menu_attendance_punchIn', 'ID', 'menu_punch')
            self.helper.click(element)
        elif attendence == "Employee Records":
            element = self.helper.identify_element('menu_attendance_viewAttendanceRecord', 'ID', 'menu_record')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('menu_attendance_configure', 'ID', 'menu_record')
            self.helper.click(element)

    def navigate_reports(self,reports):
        self.my_reports=reports
        element = self.helper.identify_element('menu_time_Reports', 'ID', 'menu_reports')
        self.helper.click(element)
        if reports == "Project Reports":
            element = self.helper.identify_element('menu_time_displayProjectReportCriteria', 'ID', 'menu_preports')
            self.helper.click(element)
        elif reports == "Employee Reports":
            element = self.helper.identify_element('menu_time_displayEmployeeReportCriteria', 'ID', 'menu_ereports')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('menu_time_displayAttendanceSummaryReportCriteria', 'ID', 'menu_ereports')
            self.helper.click(element)

    def navigate_project_info(self, project_info):
        self.My_project=project_info
        element = self.helper.identify_element('menu_admin_ProjectInfo', 'ID', 'menu_proj')
        self.helper.click(element)
        if project_info == "Customers":
            element = self.helper.identify_element('menu_admin_viewCustomers', 'ID', 'menu_cust')
            self.helper.click(element)
        else:
            element = self.helper.identify_element('menu_admin_viewProjects', 'ID', 'menu_pro')
            self.helper.click(element)

if __name__ == "__main__":
    from libCommon.driver_manager import DriverManager
    driver_mgr = DriverManager()
    obj = TimePage(driver_mgr.driver)
    #obj.navigate_time_sheet("Employee TimeSheets")
    #obj.navigate_attendance("Employee Records")
    #obj.navigate_reports("Employee Reports")
    obj.navigate_project_info("Projects")