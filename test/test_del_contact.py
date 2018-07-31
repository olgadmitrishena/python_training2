from model.contact import Contact
import random

def test_del_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create1(Contact(firstname="test", middlename="test", lastname="test", id="test", title="test", company="test", adress="test",homephone="test", mobile="test", workphone="test", fax="test", email="test", email2="test", email3="test", homepage="test",byear="test", address2="test", phone2="test", notes="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_max) == sorted(app.contact.get_contact_list(), key=Contact.id_max)












