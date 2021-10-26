from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
import timeit

#imports a table of every pokemon and their number from bulbapedia
index = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
website = requests.get(index)
table = BeautifulSoup(website.content,"html.parser")
indexposition = 6
# I need to loop through many pokemon to test them. I made the program a 1 round loop in order to avoid indenting everything whenever I need to put the code in a loop.
for item in range (1,2):
    #retrieves the link to the pokemon's individual page from the table
    row = table.find_all('tr')[indexposition]                                                                                                              
    rawlink = row.find_all('a')[0]
    link = "https://bulbapedia.bulbagarden.net/" + str(rawlink.get('href')) 
    #the values containing the pokemon's page  
    pokemon = requests.get(link)
    attributes = BeautifulSoup(pokemon.content,"html.parser")

    def getname():
        nameraw = attributes.find_all('b')[1]
        name = nameraw.get_text()
        return name

    def gettype1():
        typeraw = attributes.find_all('b')[4]
        type = typeraw.get_text()
        return type

    def gettype2():
        typeraw = attributes.find_all('b')[5]
        type = typeraw.get_text()
        return type

    def getcategory():
        categoryraw = attributes.find_all('span')[5]
        category = categoryraw.get_text()
        return category

    def getheight():
        heightsearch = attributes.find("span", string="Height")
        parent1 = heightsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        heightraw = parent3.findAll("td")[0]
        height = heightraw.get_text()
        return (height)

    def getweight():
        weightsearch = attributes.find("span", string="Weight")
        parent1 = weightsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        weightraw = parent3.findAll("td")[0]
        weight = weightraw.get_text()
        return (weight)

    def getgeneration():
        generationraw = attributes.find_all('p')[1]
        generationzoom = generationraw.find_all('a')[3]
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

    def getall():
        print (getname())
        print (gettype1()), print (gettype2())
        print (getcategory())
        print (getheight())
        print (getweight())

    


