from django.db import models
from django.contrib.auth.models import User


class CristoPoll(models.Model):
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(CristoPoll, on_delete=models.CASCADE)  # cache
    user = models.ForeignKey(User)
    reason = models.CharField(max_length=1000)


class Vote(models.Model):
    voter = models.ForeignKey(User)
    poll = models.ForeignKey(CristoPoll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice)
    date = models.DateTimeField('date vote')

    class Meta:
        unique_together = ('voter', 'poll')
