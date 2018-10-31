from bs4 import BeautifulSoup
import lxml
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

# Definitions (pronunc, syllables, defs)

def defSearch(word):
    defUrl = "http://www.dictionary.com/browse/"+word
    defPage = requests.get(defUrl)
    defSoup = BeautifulSoup(defPage.text, 'lxml')
    definitions = []

    pronunc = defSoup.select('span.css-1khtv86')[0].getText()
    syllables = len(pronunc.split(",")[0].split("-"))

    defs = defSoup.select('section.css-1748arg')[0].select('div.expand-container')

    defsGroups = []
    for defBlock in defs:
        definition = []
        defPos = defBlock.select("span.luna-pos")[0].getText()
        definition.append(defPos)
        for i in defBlock.select('span.css-9sn2pa'):
            definition.append(i.getText())

        definitions.append(definition)

    # [pronunc, syllables, [pos, defnitinons, [definition]]

    return(pronunc, syllables, definitions)

# Thesaurus

def thesSearch(word):
    thesUrl = "https://www.merriam-webster.com/thesaurus/"+word
    thesPage = requests.get(thesUrl, headers)
    thesSoup = BeautifulSoup(thesPage.text,'lxml')
    synonyms = []
    syns = thesSoup.select('span.syn-list')
    for syn in syns:
        synlist = syn.select('a')
        for i in synlist:
            synonyms.append(i.getText())
    return(synonyms)

# Rhymes

def rhymeSearch(word):
    rhymeUrl = "https://www.whatrhymeswith.info/"+word
    rhymePage = requests.get(rhymeUrl, headers)
    rhymeSoup = BeautifulSoup(rhymePage.text, 'lxml')
    rhymes = []
    rhms = rhymeSoup.select('p')[0].select('a')
    for rhm in rhms:
        rhymes.append(rhm.getText())
    return(rhymes)
