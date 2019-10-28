from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
import json


def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name))
        })
    else:
        return HttpResponseRedirect("/")
