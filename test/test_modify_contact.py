from model.contact import new

def test_modify_contact_firstname(app):
    if app.group.count() == 0:
        app.group.create_contact(new(First_name="test"))
    app.group.modify_first_contact(new(First_name="New First Name"))


def test_modify_contact_middlename(app):
    app.group.modify_first_contact(new(Middle_name="New Middle  Name"))


def test_modify_contact_lastname(app):
    app.group.modify_first_contact(new(Last_name="New Last_name  Name"))