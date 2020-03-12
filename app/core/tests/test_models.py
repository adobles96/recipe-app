from django.test import TestCase
from django.contrib.auth import get_user_model  # use this to avoid problems when changing usr model


class ModelTest(TestCase):
    
    def test_create_user_with_email_successful(self):
        """ Test that creating a new user with an email is successful. """
        cases = [
            # (email, password)
            ('test@gmail.com', 'apassword')
        ]
        for e, p in cases:
            user = get_user_model().objects.create_user(email=e, password=p)
            self.assertEqual(user.email, e)
            self.assertTrue(user.check_password(p))
            
    def test_new_user_email_normalized(self):
        """ Test that the email for a new user is normalized. """
        cases = [
            # (email, password)
            ('test@GMAIL.CoM', 'pass')
        ]
        for e, p in cases:
            user = get_user_model().objects.create_user(email=e, password=p)
            self.assertEqual(user.email, e.lower())
            
    def test_new_user_invalid_email(self):
        """ Test that user creation fails with invalid email. """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "1223")
    
    def test_create_superuser(self):
        """ Test creating a superuser. """
        user = get_user_model().objects.create_superuser("email@gmail.com", "pass")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
