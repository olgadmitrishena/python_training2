# -*- coding: utf-8 -*-
from model.group import Group


def test_add_groups(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="gvgc", header="dsfdsfsfvzsd", footer="szdvfdxvzfdvd"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

