from django.db import models

# Create your models here.


class Leaders(models.Model):

    #id = models.IntegerField(null=False, primary_key=True)
    player_name = models.TextField(null=False)
    age = models.IntegerField(null=False)
    money = models.IntegerField(null=False)
    max_health = models.IntegerField(null=True)
    friends_alive = models.IntegerField(null=True)