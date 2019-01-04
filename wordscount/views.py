from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"home.html")

def count(request):

    data = request.GET["fulltextarea"]
    word_list = data.split()
    list_length = len(word_list)

    wordDictionary = {}

    for word in word_list:
        if word in wordDictionary:
            wordDictionary[word]+=1
        else:
            wordDictionary[word]=1

    sorted_list = sorted(wordDictionary.items(),key = operator.itemgetter(1),reverse=True)

    return render(request,"count.html",{"fulltext":data,"words":list_length,"wordDictionary":sorted_list})
    #return render(request,"count.html",{"fulltext":data,"words":list_length})