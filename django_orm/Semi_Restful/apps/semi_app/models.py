from __future__ import unicode_literals
from django.db import models


class addManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if(len(postData['title']) < 2):
            errors['title'] = "Title should be at least 2 characters long"
        if(len(postData['network']) < 3):
            errors['network'] = "Network should be at least 3 characters long"
        if(len(postData['description']) > 1):
            if(len(postData['description']) < 10):
                errors['description'] = "Description should be at least 10 characters long"
        
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField()
    network = models.ForeignKey(Network, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = addManager()

