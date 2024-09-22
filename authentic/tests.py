from getpass import getuser
from struct import error

from django.test import TestCase
from django.urls import reverse
from api.models import CustomUser


class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('authentic:signup'),
            data={
                'first_name': 'John',
                'username': 'john',
                'phone_number': '1234567',
                'password1': 'P@ssw0rd2024',
                'password2': 'P@ssw0rd2024',
            }
        )

        # Print the response content to see form errors
        # print(response.content.decode())

        # Check if form submission succeeded (redirects after successful signup)
        self.assertEqual(response.status_code, 302)

        # Check if the user is created
        try:
            user = CustomUser.objects.get(username='john')
        except CustomUser.DoesNotExist:
            self.fail("CustomUser was not created.")

        # Assert that the user's details are correct
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.phone_number, '1234567')
        self.assertTrue(user.check_password('P@ssw0rd2024'))

        # profile page
        # second_response = self.client.get("/profile/admin")
        # self.assertEqual(second_response.status_code, 200)

        # login
        self.client.login(username='john', password='P@ssw0rd2024')

        third_response = self.client.post(
            reverse('authentic:user-edit'),
            data={
                'phone_number': '1234567',
                'tg_username': '@adminka',
            }
        )

        user3 = CustomUser.objects.get(username='john')
        self.assertEqual(user3.phone_number, '1234567')
        self.assertEqual(user3.tg_username, '@adminka')
        self.assertNotEqual(user3.phone_number, None)
        self.assertEqual(third_response.status_code, 302)
