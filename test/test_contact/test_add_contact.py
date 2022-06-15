# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="имя", middlename="отчество", lastname="фамилия", homephone="111111", homephone2="999999",
                mobile="88005553535", workphone="222222", faxphone="333333",
                mail="intec@io.mail", mail2="intes@ru.sand", mail3="inter@gov.gav")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

