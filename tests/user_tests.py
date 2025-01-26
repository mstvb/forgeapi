import unittest
from src.user.user import User


class TestUser(unittest.TestCase):

    def test_set_uid(self):

        user = User('set-uid')
        user.set_uid('0')
        self.assertNotEqual(user.get_uid(), False)

    def test_set_username(self):

        user = User('set-username')
        user.set_username('other')
        self.assertEqual(user.get_username(), 'other')


class TestPermissions(unittest.TestCase):
    def test_add_permission(self):

        user = User('add-user')
        user.add_permission('add-permission', True)
        self.assertTrue(user.has_permission('add-permission'))

    def test_remove_permission(self):

        user = User('remove-user')
        user.add_permission('remove-permission', True)
        self.assertTrue(user.has_permission('remove-permission'))
        user.delete_permission('remove-permission')
        self.assertFalse(user.has_permission('remove-permission'))

    def test_set_permission(self):

        user = User('set-user')
        user.add_permission('set-permission', True)
        user.set_permission('set-permission', False)
        self.assertFalse(user.is_active('set-permission'))


if __name__ == '__main__':
    unittest.main()
