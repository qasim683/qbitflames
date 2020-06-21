from django.db import models



class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_description = models.CharField(max_length=999)
    blog_image = models.ImageField(upload_to='frontend/static/images/upload_images/', default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.blog_title
