from django import forms

class GameForm(forms.Form):
    winner_name = forms.CharField(label="Winner Name:", max_length=25)
    winner_id = forms.IntegerField(label="Winner ID:")
    winner_score = forms.IntegerField(label="Winner Score:")
    loser_name = forms.CharField(label="Loser Name:", max_length=25)
    loser_id = forms.IntegerField(label="Loser ID:")
    loser_score = forms.IntegerField(label="Loser Score:")