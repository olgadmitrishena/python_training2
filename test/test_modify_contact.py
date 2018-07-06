from model.contact import new

def test_modify_contact_firstname(app):
    app.session.Login(username="admin", password="secret")
    app.group.modify_first_contact(new(First_name="New First Name"))
    app.session.logout()