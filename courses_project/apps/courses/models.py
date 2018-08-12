from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def basic_validator(selft, postData):
        errors = {}
        #validation for name
        if len(postData['name']) < 6:
            errors['name'] = "Name required at least 5 characters"
        
        #validation for the description
        if len(postData['desc']) < 16:
            errors['desc'] = "desc required at least 15 characters"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()


class Description(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.OneToOneField(Course, related_name="description")

