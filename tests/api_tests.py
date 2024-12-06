import unittest

from src.api import Forge
from src.permissions import Role
from src.user import User


class TestAPI(unittest.TestCase):
    def test_user_get_by_id(self):

        api = Forge()
        user = User('api-user_get_by_id', '2FA')
        api.add_user(user)
        self.assertEqual(api.get_user_by_id('2FA'), user)

    def test_user_get_by_name(self):

        api = Forge()
        user = User('api-user_get_by_name', '2FA')
        api.add_user(user)
        self.assertEqual(api.get_user_by_name('api-user_get_by_name'), user)

    def test_role_get_by_name(self):

        api = Forge()
        role = Role('api-test', {})
        api.add_role(role)
        self.assertEqual(api.get_role('api-test'), role)

    def test_role_get_permissions(self):

        api = Forge()
        role = Role('api-test', {})
        role.add_permission('api-test-permission')
        api.add_role(role)
        self.assertEqual(api.get_role('api-test')
                         .get_permissions(), {'api-test-permission': True})

    def test_role_has_permission(self):

        api = Forge()
        role = Role('api-test', {})
        role.add_permission('api-test-permission')
        api.add_role(role)
        self.assertTrue(api.get_role('api-test')
                        .get_permission('api-test-permission'))


if __name__ == '__main__':
    unittest.main()
