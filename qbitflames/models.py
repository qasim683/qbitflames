from django.db import models



class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


