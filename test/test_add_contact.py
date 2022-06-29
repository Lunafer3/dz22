from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_add_contacts_to_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    groups = app.orm.get_group_list()
    group = random.choice(groups)
    old_contacts = app.orm.get_contacts_in_group(group)
    if app.contact.count() == 0:
        new_contact = Contact(firstname="test")
        app.contact.create(new_contact)
    contacts = app.orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        new_contact = Contact(firstname='pure')
        app.contact.create(new_contact)
        contacts = app.orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_to_group(contact, group)
    old_contacts.append(contact)
    new_contacts = app.orm.get_contacts_in_group(group)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)

