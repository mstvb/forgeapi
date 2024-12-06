from src.permissions.role import Role


class PermissionManager:
    """
    This Class manage and used for Permission Management

    Attributes:
        permissions (dict): Dictionary
        role (Role): Role for Permissions

    Parameters:
        permissions (dict): Dictionary (str: bool) for Permissions
        role (Role) Role for Permissions

    Methods:
        set_role(role: Role) sets Role for Permissions
        add_permission(permission: str, active: bool) Add Permission
        set_permission(permission: str, active: bool) Sets Permission
        delete_permission(permission: str) Delete a Permission from Permissions
        has_permission(permission: str) Return True Permission exists
        is_active(permission: str) Return True if Active
        get_permissions() Returns all Permissions as Dictionary
        get_role() Returns Role
     """
    __slots__ = ['permissions', 'role']

    def __init__(self, permissions: dict = None, role: Role = None):
        if permissions is None:
            self.permissions = {}
        else:
            self.permissions = permissions
        self.role = role

    def set_role(self, role: Role):
        self.role = role

    def add_permission(self, permission: str, active: bool = True):
        self.permissions[permission] = active

    def set_permission(self, permission: str, active: bool):
        self.permissions[permission] = active

    def delete_permission(self, permission: str):
        del self.permissions[permission]

    def has_permission(self, permission: str):
        return True if permission in self.permissions else False

    def is_active(self, permission: str):
        return True if self.permissions[permission] is True else False

    def get_permissions(self):
        return self.permissions

    def get_role(self):
        return self.role
