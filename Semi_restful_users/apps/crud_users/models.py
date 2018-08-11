from __future__ import unicode_literals
from django.db import models
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # Validation for firstname
        if len(postData['first_name']) == 0:
            errors['first_name'] = '*First Name is required'
        elif not postData['first_name'].isalpha():
            errors['first_name'] = '*Alphabet characters only'

        # Validation for lastname
        if len(postData['last_name']) == 0:
            errors['last_name'] = '*Last Name is required'
        elif not postData['last_name'].isalpha():
            errors['last_name'] = '*Alphabet characters only'

        # Validation for email
        if len(postData['email']) == 0:
            errors['email'] = '*Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = '*Invalid email'

        # return errors
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************