from django.http import HttpResponse
from django.http import HttpRequest
from . import models
from django.core import serializers
from .models import User
# Create your views here.


def getAllUser(request:HttpRequest):
    users=serializers.serialize("json", User.objects.all())
    return HttpResponse(
        users,
        content_type="application/json"
    )

