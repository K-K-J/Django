from django.db import models

class Post(models.Model):
    #each variable below is the column in the table; then we have data types
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
