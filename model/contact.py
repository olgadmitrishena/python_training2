from sys import maxsize

class Contact:

    id_or_max = 'id_max'


    def __init__(self, firstname=None, lastname=None, id=None, middlename=None, title=None, company=None, address=None,
                 home=None, phone2=None, mobile=None, work=None, fax=None, email=None, email2=None,
                       email3=None, homepage=None, address2=None, notes=None,
                       homeadress=None, notestwo=None, byear=None, ayear=None, all_phones_from_homepage=None,
                       all_emails_from_homepage=None, all_phones_from_editpage=None, all_emails_from_editpage=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
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
        self.all_phones_from_homepage=all_phones_from_homepage
        self.all_emails_from_homepage=all_emails_from_homepage
        self.all_phones_from_editpage = all_phones_from_editpage
        self.all_emails_from_editpage = all_emails_from_editpage
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