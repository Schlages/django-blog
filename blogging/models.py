from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=1150, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_field = models.DateField(auto_now_add=True)
    modified_field = models.DateField(auto_now=True)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

