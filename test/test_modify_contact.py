# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(first_name="4"))
    old_contact_list = app.contact.get_contact_list()
    new_contact = Contact(first_name="1", middle_name="2", last_name="3")
    new_contact.id = old_contact_list[0].id
    app.contact.modify_first_contact(new_contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = new_contact
    assert sorted(old_contact_list, key=Contact.id_max) == sorted(new_contact_list, key=Contact.id_max)


#def test_modify_contact_last_name(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(last_name="New Last name"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

