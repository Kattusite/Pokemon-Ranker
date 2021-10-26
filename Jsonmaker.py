from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
import timeit

#imports a table of every pokemon and their number from bulbapedia
index = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
website = requests.get(index)
table = BeautifulSoup(website.content,"html.parser")
indexposition = 231
# I need to loop through many pokemon to test them. I made the program a 1 round loop in order to avoid indenting everything whenever I need to put the code in a loop.
for item in range (1,2):
    #retrieves the link to the pokemon's individual page from the table
    row = table.find_all('tr')[indexposition]
    #skips the table rows of regional dividers
    try:
        rowtester()
    except:
        indexposition +=1
        row = table.find_all('tr')[indexposition]
        pass                                                                                                            
    rawlink = row.find_all('a')[0]
    link = "https://bulbapedia.bulbagarden.net/" + str(rawlink.get('href'))
    #the values containing the pokemon's page  
    pokemon = requests.get(link)
    attributes = BeautifulSoup(pokemon.content,"html.parser")

    def rowtester():
        regionalnumber = row.find_all("a")[1]
        return regionalnumber

    def getname():
        nameraw = attributes.find_all('b')[1]
        name = nameraw.get_text()
        return name

    def getnumber():
        numberraw = row.find_all("td")[1]
        number = numberraw.get_text().strip('#').strip()
        return number

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
        height = heightraw.get_text().strip()
        return (height)

    def getweight():
        weightsearch = attributes.find("span", string="Weight")
        parent1 = weightsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        weightraw = parent3.findAll("td")[0]
        weight = weightraw.get_text().strip()
        return (weight)

    def getcolor():

        colorsearch = attributes.find("span", string="Pokédex color")
        parent1 = colorsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        colorraw = parent3.findAll("td")[0]
        color = colorraw.get_text().strip()
        colorclear = color.replace("Other forms may have other colors.","")
        return(colorclear)

    def getgeneration():
        generationraw = attributes.find_all('p')[1]
        generationzoom = generationraw.find_all('a')[3]
        generation = generationzoom.get('title')
        return generation

    #easy way for me to parse through all the different tags of a page, for debugging purposes only
    def attributesearch(targettag):
        for item in range (1,100):
            generation = attributes.find_all(targettag)[item]
            print ('----------------------------')
            print (item)
            print (generation)

    def getall():
        print (getnumber())
        print (getname())
        print (gettype1()), print (gettype2())
        print (getcategory())
        print (getheight())
        print (getweight())
        print('------------------------------')

    #attributesearch("a")
    #getall()
    #indexposition+=1

    abilitysearch = attributes.find("span", string="Abilities")
    parent1 = abilitysearch.parent
    parent2 = parent1.parent
    parent3 = parent2.parent
    allabilities = parent3.find_all('td')
    for ability in allabilities:
        ability = ability.get_text()
        if ability != "Cacophony":
            print (ability)