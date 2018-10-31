from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .webscrape import defSearch, thesSearch, rhymeSearch
from .forms import SearchForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchWord = form.cleaned_data['word']
            return redirect('wordSearch', word=searchWord)
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form':form})

def wordSearch(request, word):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchWord = form.cleaned_data['word']
            return redirect('wordSearch', word=searchWord)
    else:
        form = SearchForm()
    try:
        pronunc, syllables, definitions = defSearch(word)
        synonyms = thesSearch(word)
        rhymes = rhymeSearch(word)

        return render(request, 'wordsearch.html', {'word': word,
                                                   'pronunc': pronunc,
                                                   'syllables': syllables,
                                                   'definitions': definitions,
                                                   'synonyms': synonyms,
                                                   'rhymes': rhymes,
                                                   'form':form,
            })
    except IndexError:
        return render(request, '404.html', {'word': word,
                                            'form': form})
    # return render(request, 'wordsearch.html', info)
