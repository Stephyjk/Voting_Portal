from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# APositions = [('Chair','Chair'),('Vice Chair','Vice Chair'),('Secretary General','Secretary General'),('Vice Secretary General','Vice Secretary General'),
# ('Treasurer','Treasurer'),('Public Relations','Public Relations'),('Vice Public Relations','Vice Public Relations'),('Regional Representative','Regional Representative')]
# Create your models here.

class Position(models.Model):
    position=models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.position

class Candidate(models.Model):
    image=models.ImageField(verbose_name='Profile Picture', upload_to='images/')
    title=models.CharField(max_length=255)
    account = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    body=models.TextField(verbose_name='About')
    total_vote = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

class Vresults(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.account} - {self.position} - {self.status}'
