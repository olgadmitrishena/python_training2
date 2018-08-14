# -*- coding: utf-8 -*-
from model.contact import Contact

from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name", middlename="Middle name", lastname="Last name", title="Title", company="Company", adress="adress", telephone="Telephone",
                                   mobile="Mobile", work="Work", fax="Fax", email="email", email2="email2", email3="email3", homepage="Homepage", adress2="adress2",
                                   homeadress="Homeadress", notestwo="notes2", ayear="byear", byear="byear"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New First name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)

#def test_modify_contact_last_name(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(last_name="New Last name"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

