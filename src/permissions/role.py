class Role:
    __slots__ = ['role_name', 'permissions']

    def __init__(self, role_name: str, permissions: dict[str, bool]):
        self.role_name = role_name
        self.permissions = permissions

    def add_permission(self, permission_name: str, active: bool = True):
        self.permissions[permission_name] = active

    def set_permission(self, permission_name: str, active: bool):
        self.permissions[permission_name] = active

    def delete_permission(self, permission_name: str):
        del self.permissions[permission_name]

    def get_permission(self, permission_name: str):
        return self.permissions[permission_name]

    def get_permissions(self):
        return self.permissions

    def set_role_name(self, role_name: str):
        self.role_name = role_name

    def get_role_name(self):
        return self.role_name
