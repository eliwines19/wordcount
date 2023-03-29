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

    # first count the number of occurrences of each for
    wordcount = {}
    for i in fulltext.split():
        if i in wordcount:
            wordcount[i] += 1
        else:
            wordcount[i] = 1

    # get the word with the highest number of occurrences
    highest_word = ""
    highest_count = 0
    for word in wordcount:
        if wordcount[word] > highest_count:
            highest_word = word
            highest_count = wordcount[word]
    
    print(highest_word)
    

    return render(request, 'count.html', {
        "count":count,
        "fulltext":fulltext,
        "highest_word":highest_word,
        "wordcount":wordcount.items()
        })