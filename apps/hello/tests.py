from django.test import TestCase
from datetime import date
from django.contrib.auth.models import User

from apps.hello.models import Profile

import logging
logger = logging.getLogger(__name__)


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


class InitialDataTest(TestCase):
    '''
    Check if data preloaded from fixtures
    '''

    def test_adminuser(self):
        """
        check if initial superuser exists and has default credentials
        """

        default_credentials = 'admin:admin'
        username, password = default_credentials.split(':')

        u = User.objects.get(pk=1)
        self.assertEqual(u.is_superuser, True)
        self.assertEqual(u.username == username, True)
        self.assertEqual(u.check_password(password), True)

    def test_person_model_default_field_values(self):
        '''
        check if initial profile data was loaded
        '''
        initial_profile = Profile.objects.get(pk=1)

        for field_name in initial_profile._meta.get_all_field_names():
            logger.debug(
                'test_person_model_default_field_values: field: {0}'
                .format(field_name))

            # skip object-id which should differ
            if field_name == 'id':
                continue

            self.assertEquals(getattr(initial_profile, field_name),
                              profile_defaults[field_name])
