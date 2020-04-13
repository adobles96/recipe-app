from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser(email='email@gmail.com',
                                                               password='pass')
        self.client.force_login(self.admin)
        self.user = get_user_model().objects.create_user(
            email='user@gmail.com',
            password='pass',
            name='Julio Cortazar'
        )
        
    def test_users_listed(self):
        """ Tests that users are listed in the admin page. """
        url = reverse('admin:core_user_changelist')  # So that we can change the url easily.
        response = self.client.get(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
        
    def test_user_change_page(self):
        """ Test that the user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
        
    def test_create_user_page(self):
        """ Test that the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)

