from src.permissions.role import Role
from src.user import User

class Forge:
    __slots__ = ['users', 'roles']
    def __init__(self):
        self.users = []
        self.roles = []

    def add_user(self, user: User):
        self.users.append(user)

    def add_users(self, users: list):
        self.users.extend(users)

    def add_role(self, role: Role):
        self.roles.append(role)

    def add_roles(self, roles: list):
        self.roles.extend(roles)

    def get_user_by_id(self, uid: str):
        for user in self.users:
            if user.get_uid() is uid:
                return user

    def get_user_by_name(self, username: str):
        for user in self.users:
            if user.get_username() is username:
                return user

    def get_users(self):
        return self.users

    def get_role(self, role_name: str):
        for role in self.roles:
            if role.get_role_name() is role_name:
                return role

    def get_roles(self):
        return self.roles