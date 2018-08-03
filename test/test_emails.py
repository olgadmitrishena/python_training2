import re
from random import randrange
from model.contact import Contact
from fixture.orm import ORMFixture

dat = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_emails_on_homepage(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def test_emails_on_homepage_all(app, db):
    old_contacts = db.get_contact_list()
    contact_from_homepage = app.contact.get_contact_list()
    list1 = sorted(old_contacts, key=Contact.id_max)
    list2 = sorted(contact_from_homepage, key=Contact.id_max)
    for i in range(0, len(old_contacts)):
        assert merge_emails_like_on_homepage(list1[i]) == list2[i].all_emails_from_homepage


def test_emails_on_viewpage(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_viewpage = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_viewpage.email == contact_from_edit_page.email
    assert contact_from_viewpage.email2 == contact_from_edit_page.email2
    assert contact_from_viewpage.email3 == contact_from_edit_page.email3



def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))