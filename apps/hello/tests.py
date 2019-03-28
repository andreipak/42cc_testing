from django.test import TestCase
from datetime import date
from apps.hello.models import Profile


profile_defaults = {
    "bio": "Software Developer and\r\nResearcher in a wide variety of" +
    "\r\napplications and tools",
    "first_name": "Andrei",
    "last_name": "Pak",
    "dob": date(1981, 3, 13),
    "other_contacts": "LinkedIn Profile",
    "skype": "pak.andrei",
    "jabber": "andreipak@42cc.co",
    "email": "pak.andrei@gmail.com",
}


def create_profile(**kwargs):
    defaults = profile_defaults.copy()
    defaults.update(kwargs)
    return Profile.objects.create(**defaults)


class HelloIndexViewTests(TestCase):
    def test_values_exists_on_the_page(self):
        "test if index page include text"
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Andrei")
        self.assertContains(response, "Pak")
        self.assertContains(response, "pak.andrei@gmail.com")
        self.assertContains(response, "andreipak@42cc.co")


class ProfileModelTests(TestCase):

    def test_fields(self):
        """
        test if fields stores valid value
        """
        profile = create_profile()

        self.assertEqual(profile.first_name, 'Andrei')
        self.assertEqual(profile.last_name, 'Pak')
        self.assertEqual(profile.dob, date(1981, 3, 13))
        self.assertEqual(
            profile.bio,
            "Software Developer and\r\nResearcher in a wide variety of" +
            "\r\napplications and tools"
        )
        self.assertEqual(profile.skype, 'pak.andrei')
        self.assertEqual(profile.jabber, 'andreipak@42cc.co')
        self.assertEqual(profile.email, 'pak.andrei@gmail.com')
        self.assertEqual(profile.other_contacts, 'LinkedIn Profile')
