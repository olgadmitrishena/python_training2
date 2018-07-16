# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(first_name="New First name"))

def test_modify_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(middle_name="New Middle name"))
