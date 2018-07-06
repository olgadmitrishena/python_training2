# -*- coding: utf-8 -*-
from model.contact import new

def test_add_new_contact(app):
    app.session.Login(username="admin", password="secret")
    app.group.create_contact(new(First_name="sadasd", Middle_name="dsadad", Last_name="adfdzf", Nickname="sdfdc", Title="dvfv", Company="sfdsef", Address="sdffsd", Home="sdvsd", Mobile="cdscvsd", Work="svsvc", Fax="svscsc", E_mail="svsfc", E_mail2="svsc", E_mail3="svvs", Homepage="svsvcs", Secondotory_Address="svsvs", Secondotory_Home="svsvs", Notes="svsvsv"))
    app.session.logout()

def test_add_new_empty_contact(app):
    app.session.Login(username="admin", password="secret")
    app.group.create_contact(new(First_name="", Middle_name="", Last_name="", Nickname="", Title="", Company="", Address="", Home="", Mobile="", Work="", Fax="", E_mail="", E_mail2="", E_mail3="", Homepage="", Secondotory_Address="", Secondotory_Home="", Notes=""))
    app.session.logout()


