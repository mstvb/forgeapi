# Python Imports
from uuid import UUID

# Project Package Imports
from src.permissions.permissionmanager import *
from src.permissions.role import *

class User:
    """
    This Class for Users

    Arguments:
        username: [str] -> Username as String
        uid: [UUID] -> User Identification Number
        perms: [PermissionManager] -> PermissionManager Class
        json: [dict] -> Dict for User Information / JSON File Usage

    Todo:
        - Add JSON Support

    Methods:
        set_username: (username: str) -> Set Username of User as String
        set_uid: (uid: UUID) -> Set User Identification Number as UUID
        add_perm: (perm: str) -> Add Permission to User
        set_perm: (perm: str, active: bool) -> Set Permission to User
        delete_perm: (perm: str) -> Delete Permission from User
        has_perm: (perm: str) -> Returns True has Permission else False
        is_active: (perm: str) -> Returns True is Active else False
        get_perms: () -> Returns Permissions as Dict from User
        set_role: (role: Role) -> Set Role from User
        get_role: () -> Returns Role from User
        get_username: () -> Returns Username as String
        get_uid: () -> Returns User Identification Number
    """
    __slots__ = ['username', 'uid', 'perms', 'json']
    def __init__(self, username: str, uid = False):
        self.username = username
        self.uid = uid
        self.perms = PermissionManager({})
        self.json = {'username': username, 'uid': uid, 'perms': self.perms.get_perms()}

    def set_username(self, username: str):
        self.username = username
        self.json['username'] = username

    def set_uid(self, uid: UUID):
        self.uid = uid
        self.json['uid'] = uid

    def add_perm(self, perm: str, active: bool = True):
        self.perms.add_perm(perm, active)
        self.json['perms'][perm] = active

    def set_perm(self, perm: str, active: bool):
        self.perms.set_perm(perm, active)
        self.json['perms'][perm] = active

    def delete_perm(self, perm: str):
        if self.json['perms'][perm]:
            self.perms.delete_perm(perm)
            del self.json['perms']
            return True
        else:
            return False

    def has_perm(self, perm: str):
        return self.perms.has_perm(perm)

    def is_active(self, perm: str):
        return self.perms.is_active(perm)

    def get_perms(self):
        self.perms.get_perms()

    def set_role(self, role: Role):
        self.perms.set_role(role)
        self.json['role'] = role

    def get_role(self):
        return self.perms.get_role()

    def get_username(self):
        return self.username

    def get_uid(self):
        return self.uid
