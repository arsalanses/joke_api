from django.db import models


class Joke(models.Model):
    type = models.CharField(max_length=200)
    setup = models.TextField()
    punchline = models.TextField()

    def __str__(self):
        return self.type
