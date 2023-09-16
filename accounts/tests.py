from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


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


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should not be on this page.")

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
