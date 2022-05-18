
# app/Blog/models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

