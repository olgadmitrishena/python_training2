from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, id=None,
                       middle_name=None, title=None, company=None, adress=None,
                       homephone=None, phone2=None, mobile=None, workphone=None,
                       fax=None, e_mail=None, e_mail2=None, e_mail3=None,mailtwo=None, mailthree=None, homepage=None, address2=None,
                       homeadress=None, notestwo=None, byear=None, ayear=None, all_phones_from_home_page=None,
                       all_emails_from_home_page=None):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.title=title
        self.company=company
        self.adress=adress
        self.homephone=homephone
        self.mobile=mobile
        self.workphone=workphone
        self.phone2=phone2
        self.fax=fax
        self.e_mail=e_mail
        self.e_mail2 = e_mail2
        self.e_mail3 = e_mail3
        self.mailtwo=mailtwo
        self.mailthree=mailthree
        self.homepage=homepage
        self.address2=address2
        self.homeadress=homeadress
        self.notestwo=notestwo
        self.byear=byear
        self.ayear=ayear
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize