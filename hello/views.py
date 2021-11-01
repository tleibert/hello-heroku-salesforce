import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from simple_salesforce import Salesforce

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    sf = Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_TOKEN"),
    )
    sf_data = sf.query_all("SELECT Name FROM Contact")
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    resp = "<h>My Salesforce Contacts</h>"
    return HttpResponse(resp)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
