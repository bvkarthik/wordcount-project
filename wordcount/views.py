from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    InputArea = request.GET['InputArea']

    wordlist  = InputArea.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word]+=1
        else:
            #add word to worddictionary
            worddictionary[word]=1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'InputArea':InputArea, 'count':len(wordlist), 'sortedwords':sortedwords})
