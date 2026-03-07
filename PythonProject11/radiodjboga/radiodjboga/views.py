from django.shortcuts import render

def player_page(request):
    return render(request, 'player.html')