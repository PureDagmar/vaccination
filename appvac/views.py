from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client
from .forms import CreateNewClient
# Create your views here.


def index(response, id):
    ls = Client.objects.get(id=id)

    if response.method == "POST":
        for vaccine in ls.vaccine_set.all():
            if response.POST.get(vaccine.text)=="clicked":
               vaccine.complete = True
            else:
               vaccine.complete = False
            vaccine.save()

    return render(response, "appvac/client.html", {"ls": ls})


def kids(response):
    clients = Client.objects.all()
    return render(response, "appvac/kids.html", {"clients":clients})


def home(response):
    return render(response, "appvac/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewClient(response.POST)

        if form.is_valid():
                n = form.cleaned_data["name"]
                b = form.cleaned_data["birth_date"]
                g = form.cleaned_data["gender"]
                m = form.cleaned_data["mother_name"]
                p = form.cleaned_data["phone"]
                t = form.cleaned_data["town"]
                o = form.cleaned_data["compound"]
                c = Client(name=n, birth_date=b, gender=g, mother_name=m, phone=p, town=t, compound=o)
                c.save()
                c.vaccine_set.create(text='BCG', complete=False)
                c.vaccine_set.create(text='HepB', complete=False)
                c.vaccine_set.create(text='OPV0', complete=False)
                c.vaccine_set.create(text='OPV1', complete=False)
                c.vaccine_set.create(text='Penta1', complete=False)
                c.vaccine_set.create(text='PCV1', complete=False)
                c.vaccine_set.create(text='Rota1', complete=False)
                c.vaccine_set.create(text='OPV2', complete=False)
                c.vaccine_set.create(text='Penta2', complete=False)
                c.vaccine_set.create(text='PCV2', complete=False)
                c.vaccine_set.create(text='Rota2', complete=False)
                c.vaccine_set.create(text='OPV3', complete=False)
                c.vaccine_set.create(text='Penta3', complete=False)
                c.vaccine_set.create(text='PCV3', complete=False)
                c.vaccine_set.create(text='IPV', complete=False)
                c.vaccine_set.create(text='OPV4', complete=False)
                c.vaccine_set.create(text='MR1', complete=False)
                c.vaccine_set.create(text='YellowFever', complete=False)
                c.vaccine_set.create(text='MenA', complete=False)
                c.vaccine_set.create(text='OPTBooster', complete=False)
                c.vaccine_set.create(text='OPVBooster', complete=False)
                c.vaccine_set.create(text='MR2', complete=False)
                c.vaccine_set.create(text='VitaminA', complete=False)
                c.vaccine_set.create(text='Mebendazole', complete=False)

        return HttpResponseRedirect("/")
    else:
        form = CreateNewClient()
    return render(response, "appvac/create.html", {"form": form})
