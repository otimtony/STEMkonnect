from django.test import TestCase

# Create your tests here.

from rest_framework import status

from rest_framework.test import APITestCase
from remitapi import settings as test_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Add these imports at the top
from rest_framework.test import APIClient

class SmileTests(TestCase):

	def setUp(self):

			 # Set up user
	    self.user = User(email="foo@bar.com") # NB: You could also use a factory for this
	    password = 'some_password'
	    self.user.set_password(password)
	    self.user.save()

	    # Authenticate client with user
	    self.client = APIClient()
	    self.client.login(email=self.user.email, password=password)

	    self.client = APIClient()
	    self.bucketlist_data = {}

	    self.response = self.client.post(
            reverse('smile_bal'),
            self.bucketlist_data,
            headers = {'Authorization':'Token  00c8c53615e10905506e05f2ebac23de1ce8b8db', 'Content-Type': 'application/x-www-form-urlencoded'})


	def test_query_bal(self):
		self.assertEqual(self.response.status_code, status.HTTP_200_OK)

        

     

