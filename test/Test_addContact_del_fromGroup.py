
from fixture import contact
from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture
import random

database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", id="test", title="test", company="test",
                    address="test",
                    home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test",
                    homepage="test", byear="test", address2="test", phone2="test", notes="test"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    group = random.choice(groups)
    index = randrange(len(contacts))
    contact_to_group = database.get_contacts_in_group(group)
    if len(contact_to_group) == len(contacts):
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", id="test", title="test", company="test",
                    address="test",
                    home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test",
                    homepage="test", byear="test", address2="test", phone2="test", notes="test"))
    app.contact.add_contact_to_group(index, group.id)
    new_contacts = db.get_contact_list()
    assert len(contacts) == len(new_contacts)
    assert sorted(contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)


def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", id="test", title="test", company="test",
                    address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test",
                    homepage="test", byear="test", address2="test", phone2="test", notes="test"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    contact = db.get_contact_list()
    groups = db.get_group_list()
    group = random.choice(groups)
    index = randrange(len(contact))
    contact_to_group = database.get_contacts_in_group(group)
    if len(contact_to_group) == 0:
        app.contact.add_contact_to_group(index, group.id)
    app.contact.del_contact_from_group(index, group.id)
    new_contacts = db.get_contact_list()
    assert isinstance(new_contacts, group.id)
    assert len(contact)-1 == len(new_contacts)
    contact.remove(index)
    assert contact == new_contacts

