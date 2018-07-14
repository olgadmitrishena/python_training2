

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, groups):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(groups)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, groups):
        wd = self.app.wd
        self.change_field_value("group_name", groups.name)
        self.change_field_value("group_header", groups.header)
        self.change_field_value("group_footer", groups.footer)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def create_contact(self, group):
        wd = self.app.wd
        self.open_add_new_page()
        # init new contact creation
        self.fill_contact_form(group)
        # submit new contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, group):
        wd = self.app.wd
        self.change_contact_field_value("firstname", group.First_name)
        self.change_contact_field_value("middlename", group.Middle_name)
        self.change_contact_field_value("lastname", group.Last_name)
        self.change_contact_field_value("nickname", group.Nickname)
        self.change_contact_field_value("title", group.Title)
        self.change_contact_field_value("company", group.Company)
        self.change_contact_field_value("address", group.Address)
        self.change_contact_field_value("home", group.Home)
        self.change_contact_field_value("mobile", group.Mobile)
        self.change_contact_field_value("work", group.Work)
        self.change_contact_field_value("fax", group.Fax)
        self.change_contact_field_value("email", group.E_mail)
        self.change_contact_field_value("email2", group.E_mail2)
        self.change_contact_field_value("email3", group.E_mail3)
        self.change_contact_field_value("homepage", group.Homepage)
        self.change_contact_field_value("address2", group.Secondotory_Address)
        self.change_contact_field_value("home", group.Secondotory_Home)
        self.change_contact_field_value("notes", group.Notes)

    def change_contact_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def open_add_new_page(self):
        wd = self.app.wd
        # add new
        wd.find_element_by_link_text("add new").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_group_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()