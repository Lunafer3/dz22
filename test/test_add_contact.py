# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(
        Contact(name="имя", middlename="отчество", lastname="фамилия", homephone="111111", homephone2="999999",
                mobile="88005553535", workphone="222222", faxphone="333333",
                mail="intec@io.mail", mail2="intes@ru.sand", mail3="inter@gov.gav", byear="1999"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(
            Contact(name="имя", middlename="отчество", lastname="фамилия", homephone="111111", homephone2="999999",
                    mobile="88005553535", workphone="222222", faxphone="333333",
                    mail="intec@io.mail", mail2="intes@ru.sand", mail3="inter@gov.gav", byear="1999"))
    app.session.logout()