from model.contact import Contact
import random

def test_delete_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(first_name="test"))
        old_contact_list = db.get_contact_list()
        contact = random.choice(old_contact_list)
        app.contact.delete_contact_by_id(contact.id)
        assert len(old_contact_list) - 1 == app.contact.count()
        new_contact_list = db.get_contact_list()
        old_contact_list.remove(contact)
        assert old_contact_list == new_contact_list










