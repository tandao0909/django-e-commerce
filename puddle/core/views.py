from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from item.models import Item, Category
from .forms import SignUpForm

def index(request: HttpRequest):
    latest_items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", context={
        "items": latest_items,
        "categories": categories,
    })

def contact(request:HttpRequest):
    return render(request, "core/contact.html")

def signup(request:HttpRequest):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {
        "form": form
    })
