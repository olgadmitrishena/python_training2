# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
from data.add_contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_max) == sorted(new_contact_list, key=Contact.id_max)












