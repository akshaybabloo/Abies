import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    article = models.TextField()
    date = models.DateTimeField('Date Published', default= timezone.now, blank=True)
    tags = models.CharField(max_length=500)
    makePrivate = models.BooleanField(default=True)

    def __str__(self):
        return self.article

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
