class Role:
    """
    Arguments:
        role_name: [str] -> Name of Role as String
        perms: dict[str, bool] -> Permissions of Role as Dict

    Todo:
        - Better Exception Handling
        
    Methods:
        add_perm: (perm: str, active: bool = True) -> Add a Permission to Role
        set_perm: (perm: str, active: bool) -> Set Permission from Role
        delete_perm: (perm: str) -> Delete Permission from Role
        get_perm: (perm: str) -> Returns Permission as Boolean
        get_perms: () -> Returns All Permissions from Role as Dict
        
    """
    __slots__ = ['role_name', 'perms']

    def __init__(self, role_name: str, perms: dict[str, bool]) -> None:
        self.role_name = role_name
        self.perms = perms

    def add_perm(self, perm: str, active: bool = True) -> None:
        self.perms[perm] = active

    def set_perm(self, perm: str, active: bool) -> None:
        self.perms[perm] = active

    def delete_perm(self, perm: str) -> None:
        del self.perms[perm]

    def get_perm(self, perm: str) -> bool:
        return self.perms[perm]

    def get_perms(self) -> dict:
        return self.perms

    def set_role_name(self, role_name: str) -> None:
        self.role_name = role_name

    def get_role_name(self) -> str:
        return self.role_name
