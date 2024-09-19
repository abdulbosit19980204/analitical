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
