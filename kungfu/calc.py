from entry.models import Game, Player

@staticmethod
def calcNewElo(winner_id, loser_id, winner_score, loser_score):
    winner = Player.objects.get(id=winner_id)
    loser = Player.objects.get(id=loser_id)

    