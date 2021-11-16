import os

from django.shortcuts import render
from django.http import HttpResponse
from simple_salesforce import Salesforce

from .models import Greeting


# Render data from simple_salesforce into a template using a salesforce style sheet
def index(request):

    sf = Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_TOKEN"),
    )
    sf_data = sf.query_all("SELECT Name, Title, Email, Phone FROM Contact")
    return render(request, "table.html", context=sf_data)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
