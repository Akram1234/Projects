import operator
from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordfreq = {}
    for word in words:
        if word in wordfreq:
            wordfreq[word]+=1
        else:
            wordfreq[word]=1
    wordfreq = sorted(wordfreq.items(), key=operator.itemgetter(1), reverse= True)

    return render(request, 'count.html', { 'count': len(words), 'fulltext': fulltext, 'wordfreq': wordfreq})