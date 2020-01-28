from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Game, Player
from kungfu.calc import 

def index(request):
    lastFive = Game.objects.order_by('-datetime')[:5]
    template = loader.get_template('entry/index.html')
    context = {
        'lastFive' : lastFive
    }
    return HttpResponse(template.render(context, request))

def gameentry(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        return HttpResponseRedirect("/entrysuccess/")
    else:
        form = GameForm()
    return render(request, gameentry.html, context={'form':form})

def gamedetail(request, game_id):
    game = Game.objects.get(id=game_id)
    loser = game.loser
    winner = game.winner
    loser_name = loser.name
    winner_name = winner.name
    loser_id = loser.id
    winner_id = winner.id
    winner_score = game.winner_score
    loser_score = game.loser_score
    context = {
        'loser_name':loser_name,
        'winner_name':winner_name,
        'loser_id':loser_id,
        'winner_id':winner_id,
        'winner_score':winner_score,
        'loser_score':loser_score
    }
    return render(request, 'entry/gamedetail.html', context)

def playerdetail(request, player_id):
    player = Player.objects.get(id=player_id)
    rating = player.rating
    name = player.name
    wins = player.record_wins
    losses = player.record_losses
    context = {
        'name':name,
        'rating':rating,
        'wins'
    }

def playerentry(request)'

