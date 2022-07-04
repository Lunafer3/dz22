# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_group(app, db, check_ui, json_groups):
    group0 = json_groups
    old_groups = db.get_group_list()
    app.group.create(group0)
    new_groups = db.get_group_list()
    old_groups.append(group0)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_groups, key=Group.id_or_max) == \
            sorted(app.group.get_groups_list(), key=Group.id_or_max)


