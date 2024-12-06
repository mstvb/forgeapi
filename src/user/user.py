from src.permissions.permissionmanager import *
from src.permissions.role import *


class User:
    __slots__ = ['username', 'uid', 'perms', 'json']
    def __init__(self, username: str, uid = False):
        self.username = username
        self.uid = uid
        self.perms = PermissionManager({})
        self.json = {'username': username, 'uid': uid, 'perms': self.perms.get_permissions()}

    def set_username(self, username: str):
        self.username = username
        self.json['username'] = username

    def set_uid(self, uid):
        self.uid = uid
        self.json['uid'] = uid

    def add_permission(self, permission: str, active: bool = True):
        self.perms.add_permission(permission, active)
        self.json['perms'][permission] = active

    def set_permission(self, permission: str, active: bool):
        self.perms.set_permission(permission, active)
        self.json['perms'][permission] = active

    def delete_permission(self, permission: str):
        if self.json['perms'][permission]:
            self.perms.delete_permission(permission)
            del self.json['perms']
            return True
        else:
            return False

    def has_permission(self, permission: str):
        return self.perms.has_permission(permission)

    def is_active(self, permission: str):
        return self.perms.is_active(permission)

    def get_permissions(self):
        self.perms.get_permissions()

    def set_role(self, role: Role):
        self.perms.set_role(role)
        self.json['role'] = role

    def get_role(self):
        return self.perms.get_role()

    def get_username(self):
        return self.username

    def get_uid(self):
        return self.uid