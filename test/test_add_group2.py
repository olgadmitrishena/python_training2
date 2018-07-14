# -*- coding: utf-8 -*-
from model.group import Group


def test_add_groups(app):
    app.group.create(Group(name="gvgc", header="dsfdsfsfvzsd", footer="szdvfdxvzfdvd"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))