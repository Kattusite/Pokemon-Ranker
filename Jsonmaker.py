from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
import timeit

#imports a table of every pokemon and their number from bulbapedia
index = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
website = requests.get(index)
table = BeautifulSoup(website.content,"html.parser")
indexposition = 552
#retrieves the link to the pokemon's individual page from the table
row = table.find_all('tr')[indexposition]                                                                                                              
rawlink = row.find_all('a')[0]
link = "https://bulbapedia.bulbagarden.net/" + str(rawlink.get('href')) 
#the values containing the pokemon's page  
pokemon = requests.get(link)
attributes = BeautifulSoup(pokemon.content,"html.parser")

#gets the pokemon name if the article uses td formatting
def getname():
    nameraw = attributes.find_all('b')[1]
    name = nameraw.get_text()
    return name

#gets the pokemon's primary type
def gettype1():
    typeraw = attributes.find_all('b')[4]
    type = typeraw.get_text()
    return type

#gets the pokemon's secondary type

def gettype2():
    typeraw = attributes.find_all('b')[5]
    type = typeraw.get_text()
    return type


def getcategory():
    categoryraw = attributes.find_all('span')[5]
    category = categoryraw.get_text()
    return category

#gets the pokemon's generation
def getgeneration():
    generation = attributes.find_all('p')[1]
    generationzoom = generation.find_all('a')[3]
    generation = generationzoom.get('title')
    return generation

#skips the table row if there are no pokemon
def tryname():
    try:
        return getname()
    except:
        pass

#easy way for me to parse through all the different tags of a page, for debugging purposes only
def attributesearch(targettag):
    for item in range (1,100):
        generation = attributes.find_all(targettag)[item]
        print ('----------------------------')
        print (item)
        print (generation)

attributesearch("span")