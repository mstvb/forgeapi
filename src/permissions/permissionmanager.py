from src.permissions.role import Role


class PermissionManager:
    """
    This Class manage and used for Permission Management

    Attributes:
        perms: dict[str, bool] -> Dict for Permissions
        role: [type] -> Role Class for Permissions

    Parameters:
        perms (dict): Dictionary (str: bool) for Permissions
        role (Role) Role for Permissions

    Methods:
        set_role: (role: Role) -> sets Role for Permissions
        add_perm: (perm: str, active: bool) -> Add Permission
        set_perm: (perm: str, active: bool) -> Sets Permission
        delete_perm: (perm: str) -> Delete a Permission from Permissions
        has_perm: (perm: str) -> Return True Permission exists
        is_active: (perm: str) -> Return True if Active
        get_perms: () -> Returns all Permissions as Dictionary
        get_role: () -> Returns Role
        
     """
    __slots__ = ['perms', 'role']

    def __init__(self, perms: dict = dict[str, bool], role: Role = None):
        self.perms = perms
        self.role = role

    def set_role(self, role: Role) -> None:
        self.role = role

    def add_perm(self, perm: str, active: bool = True) -> None:
        self.perms[perm] = active

    def set_perm(self, perm: str, active: bool) -> None:
        self.perms[perm] = active

    def delete_perm(self, perm: str) -> None:
        del self.perms[perm]

    def has_perm(self, perm: str) -> bool:
        return True if perm in self.perms else False

    def is_active(self, perm: str) -> bool:
        return True if self.perms[perm] is True else False

    def get_perms(self) -> dict:
        return self.perms

    def get_role(self) -> type:
        return self.role
