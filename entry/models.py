from django.db import models

# Create your models here.

class Player(models.Model):
    def __str__(self):
        return self.name
    def validate(self):
        self.isValidated = True
    name = models.CharField(max_length=25)
    rating = models.IntegerField(default=500)
    record_wins = models.IntegerField(default=0)
    record_losses = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)
    isValidated = models.BooleanField(default=False)


class Game(models.Model):
    def __str__(self):
        return winner.name + " def. " + loser.name
    winner_score = models.IntegerField()
    loser_score = models.IntegerField()
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="winner")
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="loser")
    datetime = models.DateTimeField(auto_now=True)