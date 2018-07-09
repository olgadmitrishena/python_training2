from model.contact import new

def test_modify_contact_firstname(app):
    app.group.modify_first_contact(new(First_name="New First Name"))


def test_modify_contact_middlename(app):
    app.group.modify_first_contact(new(Middle_name="New Middle  Name"))


def test_modify_contact_lastname(app):
    app.group.modify_first_contact(new(Last_name="New Last_name  Name"))
