from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    # gets the parameters
    fulltext = request.GET['fulltext']

    # counts the number of words in fulltext
    count = len(fulltext.split())

    # get the word that appeared the most
    # wordcount = {}

    # for i in fulltext.split():
    #     print(i)

    return render(request, 'count.html', {
        "count":count,
        "fulltext":fulltext
        })