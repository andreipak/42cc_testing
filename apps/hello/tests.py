from django.test import TestCase


class HelloIndexViewTests(TestCase):
    def test_values_exists_on_the_page(self):
        "test if index page include text"
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Andrei")
        self.assertContains(response, "Pak")
        self.assertContains(response, "pak.andrei@gmail.com")
        self.assertContains(response, "andreipak@42cc.co")
