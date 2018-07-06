
from model.group import Group


def test_modify_group_name(app):
    app.session.Login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()