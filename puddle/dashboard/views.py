from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.request import HttpRequest

from item.models import Item

@login_required
def index(request:HttpRequest):
    items = Item.objects.filter(created_by=request.user)

    return render(request, "dashboard/index.html", {
        "items": items
    })
