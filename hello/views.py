import os

from django.shortcuts import render
from django.http import HttpResponse
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
    sf_data = sf.query_all("SELECT Name, Phone FROM Contact")
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)

    rows = [
        f"""<tr>
    <td>
    {entry['Name']}
    </td>
    <td>
    {entry['Phone']}
    </td>
    </tr>
    """
        for entry in sf_data["records"]
    ]
    resp = """<h>Trevor's Salesforce Contacts</h>
    <p>This data is pulled straight from salesforce through simple_salesforce!</p>
    <p>It's rendered through python f-strings right now, until I get the hang of django templating.</p>
    </br>
    <table>
    <tr>
        <th>Name</th>
        <th>Phone</th>
    </tr>
    {rows}
    </table>
    """.format(
        rows="\n".join(rows)
    )

    return HttpResponse(resp)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
