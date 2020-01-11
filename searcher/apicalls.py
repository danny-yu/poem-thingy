import requests
import json

def defSearchApi(word):
	r1 = requests.get("https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=")
	word_dict1 = r1.json()[0]
	pronunc = word_dict1['hwi']['prs'][0]['mw']
	syllables = len(pronunc.split("-"))

	def_url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
	headers = {
	    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
	    'x-rapidapi-key': ""
    }

	r2 = requests.request("GET", def_url, headers=headers)
	word_dict2 = r2.json()['definitions']
	definitions = []

	for definition in word_dict2:
		def_group = []
		def_group.append(definition['partOfSpeech'])
		def_group.append(definition['definition'])
		definitions.append(def_group)

	return pronunc, syllables, definitions

def thesSearchApi(word):
	thes_url = "https://wordsapiv1.p.mashape.com/words/" + word + "/synonyms"
	headers = {
		'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
		'x-rapidapi-key': ""
	}
	r = requests.get(thes_url, headers=headers)
	syn_dict = r.json()
	synonyms = syn_dict['synonyms']
	return synonyms
