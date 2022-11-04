from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room


@login_required
def room(request):
    room = Room.objects.first()
    return render(request, 'room/room.html', {'room': room})
