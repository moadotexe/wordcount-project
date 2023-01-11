from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hinerds': "I Bench 225 kg"})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()

    wordbank = {}

    for word in wordlist:
        if word in wordbank:
            #up
            wordbank[word] += 1
        else:
            #compile
            wordbank[word] = 1

    SortedWords = sorted(wordbank.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'SortedWords':SortedWords})
   