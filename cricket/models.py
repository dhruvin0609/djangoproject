from django.db import models

# Create your models here.


class team(models.Model):
    teamname = models.CharField(max_length=40)


class player(models.Model):
    playername = models.CharField(max_length=100)
    team = models.ForeignKey(team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    ball = models.IntegerField(default=0)
    wicket = models.IntegerField(default=0)
    brun = models.IntegerField(default=0)
    overs = models.FloatField(default=0)


class livematch(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE)
    teamname1 = models.CharField(max_length=40)
    teamname2 = models.CharField(max_length=40)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    wicket1 = models.IntegerField(default=0)
    wicket2 = models.IntegerField(default=0)
    over1 = models.FloatField(default=0)
    over2 = models.FloatField(default=0)
    balls = models.IntegerField(default=120)
    win = models.IntegerField(default=0)
    current_ball = models.IntegerField(default=0)


class match_details(models.Model):
    match = models.ForeignKey(livematch, on_delete=models.CASCADE)
    over = models.IntegerField(default=20)
    venue = models.CharField(max_length=100)
