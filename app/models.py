from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.

CHO = (
    ('ug', 'UnderGraduate'),
    ('pg', 'PostGraduate'),
    ('phd', 'PhD'),
    ('fac', 'Faculty'),
    ('ind', 'Industrial'),
    ('No', 'None')
)
CHO_diff = (
    ('e','easy'),
    ('m','medium'),
    ('h', 'hard'),
)

class Userpro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime.date.today)
    country = models.CharField(max_length=50, default='')
    qualification = models.CharField(max_length=10, choices=CHO, default='No')
    university = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return str(self.user)


class UserScore(models.Model):
    uid = models.ForeignKey(Userpro, on_delete=models.CASCADE)
    badges = models.CharField(max_length=20)


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    code = models.CharField(max_length=100)
    is_prize = models.BooleanField(default=False)
    is_goodies = models.BooleanField(default=False)
    goofies = models.CharField(max_length=100, default=None)
    first_prize = models.IntegerField(default=0)
    second_prize = models.IntegerField(default=0)
    third_prize = models.IntegerField(default=0)


class QuestionForEvent(models.Model):
    eid = models.ForeignKey(Event, on_delete=models.CASCADE)
    difficulty = models.CharField(choices=CHO_diff, default='e', max_length=10)
    desc = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class UserSubmission(models.Model):
    uid = models.ForeignKey(Userpro, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.uid) + " " + str(self.time)
