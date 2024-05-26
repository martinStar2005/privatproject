from django.db import models


class Personals(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.TextField()
    email = models.EmailField()
    position = models.CharField(max_length=400)
    image = models.ImageField(upload_to='personals/')

    datetime_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
