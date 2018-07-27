
from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", title="title1", company="company1", adress="adress1", workphone="workphone1",
            mobile="mobile1", fax="fax1", email="email1", email2="email21", email3="email31", homepage="homepage1", address2="address21", homeadress="homeadress1",
            notestwo="notestwo1", byear="byear1", ayear="ayear1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", title="title2", company="company2", adress="adress2", workphone="workphone2",
            mobile="mobile2", fax="fax2", email="email2", email2="email22", email3="email32", homepage="homepage2", address2="address22", homeadress="homeadress2",
            notestwo="notestwo2", byear="byear2", ayear="ayear2")
]



def random_string(prefix, maxlen):
    simbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", title="", company="", adress="", workphone="",
            mobile="", fax="", email="", email2="", email3="", homepage="", address2="", homeadress="",
            notestwo="", byear="", ayear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), title=random_string("title", 10), company=random_string("company", 10), adress=random_string("adress", 10), workphone=random_string("workphone", 10),
            mobile=random_string("mobile", 10), fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10), address2=random_string("address2", 10), homeadress=random_string("homeadress", 10),
            notestwo=random_string("notestwo", 10), byear=random_string("byear", 10), ayear=random_string("ayear", 10))
    for i in range(5)
]
