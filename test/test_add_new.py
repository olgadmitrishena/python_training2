# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact_list = Contact(first_name="q", middle_name="w", last_name="e", title="r", company="t", adress="y", telephone="u", mobile="i", work="o",
                       fax="p", e_mail="a", mailtwo="s", mailthree="d", homepage="f", adress2="g", homeadress="h", notestwo="j", byear="k", ayear="l")
    app.contact.create(contact_list)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact_list)
    assert sorted(old_contact_list, key=Contact.id_max) == sorted(new_contact_list, key=Contact.id_max)





#def test_add_empty_contact(app):
#    old_contact_list = app.contact.get_contact_list()
#    new_contact = Contact(first_name="", middle_name="", last_name="")
#    app.contact.create(new_contact)
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) + 1 == len(new_contact_list)
#    old_contact_list.append(new_contact)
#    assert sorted(old_contact_list, key=Contact.id_max) == sorted(new_contact_list, key=Contact.id_max)







