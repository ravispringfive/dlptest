from django.db import models


class TestUser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.firstname
