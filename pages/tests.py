from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.


class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'I should not be here on this page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
