from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def count(request):
    Fulltext = request.GET['fulltext']
    wordlist = Fulltext.split()     #split is a function that can split a strint into words

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
    #         Increase
            worddictionary[word] += 1
        else:
    #         add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=False)
    return render(request,'count.html', {'fulltext': Fulltext, 'count':len(wordlist),'sortedwords':sortedwords })