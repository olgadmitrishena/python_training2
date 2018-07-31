from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, middlename=None, title=None, company=None, adress=None,
                       homephone=None, phone2=None, mobile=None, workphone=None, fax=None, email=None, email2=None,
                       email3=None, homepage=None, address2=None, notes=None,
                       homeadress=None, notestwo=None, byear=None, ayear=None, all_phones_from_home_page=None,
                       all_emails_from_home_page=None, all_phones_from_edit_page=None, all_emails_from_edit_page=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.title=title
        self.company=company
        self.adress=adress
        self.homephone=homephone
        self.mobile=mobile
        self.workphone=workphone
        self.phone2=phone2
        self.fax=fax
        self.email=email
        self.email2 = email2
        self.email3 = email3
        self.homepage=homepage
        self.address2=address2
        self.homeadress=homeadress
        self.notestwo=notestwo
        self.byear=byear
        self.ayear=ayear
        self.notes=notes
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.all_phones_from_edit_page = all_phones_from_edit_page
        self.all_emails_from_edit_page = all_emails_from_edit_page
        self.id = id

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize