from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        new_user = User.objects.create_user(
            username="test", email="test123@email.com", password="testpass123")
        self.assertEquals(new_user.username, "test")
        self.assertEquals(new_user.email, "test123@email.com")
        self.assertFalse(new_user.is_superuser)
        self.assertFalse(new_user.is_staff)
        self.assertTrue(new_user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        new_superuser = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123")
        self.assertEqual(new_superuser.username, "superadmin")
        self.assertEqual(new_superuser.email, "superadmin@email.com")
        self.assertTrue(new_superuser.is_staff)
        self.assertTrue(new_superuser.is_superuser)
        self.assertTrue(new_superuser.is_active)
