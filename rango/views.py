from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionay to pass the template engine as its context
    # Note the key boldmessage matches to {{ boldmessage }} ub the template
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier
    # The first parameter is the template that we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
