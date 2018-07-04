from django.shortcuts import render

from gamification.models import Participant


def index(request):
    participants = Participant.objects.all()
    args = {'participants': participants}
    return render(request, 'gamification.html', args)
