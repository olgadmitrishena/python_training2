from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(first_name="test"))
        old_contact_list = app.contact.get_contact_list()
        app.contact.delete_from_contact()
        assert len(old_contact_list) - 1 == app.contact.count()
        new_contact_list = app.contact.get_contact_list()
        old_contact_list[0:1] = []
        assert old_contact_list == new_contact_list










