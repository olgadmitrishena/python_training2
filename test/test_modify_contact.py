from model.contact import new

def test_modify_contact_firstname(app):
    app.session.Login(username="admin", password="secret")
    app.group.modify_first_contact(new(First_name="New First Name"))
    app.session.logout()

def test_modify_contact_middlename(app):
    app.session.Login(username="admin", password="secret")
    app.group.modify_first_contact(new(Middle_name="New Middle  Name"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.Login(username="admin", password="secret")
    app.group.modify_first_contact(new(Last_name="New Last_name  Name"))
    app.session.logout()