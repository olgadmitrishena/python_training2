# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import new
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_new_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(new(Ferst_name="sadasd", Middle_name="dsadad", Last_name="adfdzf", Nickname="sdfdc", Title="dvfv", Company="sfdsef", Address="sdffsd", Home="sdvsd", Mobile="cdscvsd", Work="svsvc", Fax="svscsc", E_mail="svsfc", E_mail2="svsc", E_mail3="svvs", Homepage="svsvcs", Secondotory_Address="svsvs", Secondotory_Home="svsvs", Notes="svsvsv"))
        self.app.logout()

    def test_add_new_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(new(Ferst_name="", Middle_name="", Last_name="", Nickname="", Title="", Company="", Address="", Home="", Mobile="", Work="", Fax="", E_mail="", E_mail2="", E_mail3="", Homepage="", Secondotory_Address="", Secondotory_Home="", Notes=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
