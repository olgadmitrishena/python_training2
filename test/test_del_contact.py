from model.contact import new

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(new(First_name="test"))
    app.contact.delete_first_contact()
