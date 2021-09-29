from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
import timeit

#imports a table of every pokemon and their number from bulbapedia
index = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
website = requests.get(index)
table = BeautifulSoup(website.content,"html.parser")
indexposition = 123
#for number in range (1,1000):
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
    name = nameraw
    return name

#gets the pokemon's types
def gettype():
    typeraw = attributes.find_all('tr')[16]
    typezoom = typeraw.find_all('b')
    type = str(typezoom).replace("[",'').replace("]",'').replace("<",'').replace(">",'').replace("b",'').replace("/",'')
    return type

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