from django.db import models

# Create your models here.
class Game(models.Model):
    winner_score = models.IntegerField()
    loser_score = models.IntegerField()
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
class Player(models.Model):
    name = models.CharField(max_length=25)
    rating = models.IntegerField(default=500)
    record_wins = models.IntegerField(default=0)
    record_losses = models.IntegerField(default=0)
    id = models.IntegerField()

