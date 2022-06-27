from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_del_contact_from_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact("1n", "2n", "3n", "", "Title", "Comp", "address",
                                    "", "", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact0 = random.choice(old_contacts)
    group0 = random.choice(old_groups)
    old_list = db.get_contacts_in_group(group0.id)
    if len(db.get_contacts_in_group(group0.id)) == 0:
        app.contact.add_contact_to_group_by_id(contact0.id, group0.id)
    old_list = db.get_contacts_in_group(group0.id)
    contact0 = random.choice(old_list)
    app.contact.delete_contact_from_group_by_id(contact0.id, group0.id)
    old_list.remove(contact0)
    new_list = db.get_contacts_in_group(group0.id)
    assert old_list == new_list
