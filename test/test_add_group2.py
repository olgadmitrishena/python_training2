# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_groups(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="gvgc", header="dsfdsfsfvzsd", footer="szdvfdxvzfdvd"))
    app.logout()

def test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

