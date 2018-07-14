from model.contact import new

def test_delete_first_contact(app):
    if app.group.count() == 0:
        app.group.create_contact(new(First_name="test"))
    app.group.delete_first_contact()
