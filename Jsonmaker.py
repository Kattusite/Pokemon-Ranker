from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
import timeit
#imports a table of every pokemon and their number from bulbapedia
website = "https://bulbapedia.bulbagarden.net/wiki/Togetic_(Pok%C3%A9mon)"
for item in range (0,100):
    currentpage = requests.get(website)
    pagecontent = BeautifulSoup(currentpage.content,"html.parser")
    nextpagelink = pagecontent.find_all('a')[86]
    nextpageaddress = "https://bulbapedia.bulbagarden.net/" + str(nextpagelink.get('href'))

    def get_name():
        nameraw = pagecontent.find_all('b')[1]
        name = nameraw.get_text()
        return name

    def get_primary_type():
        typeraw = pagecontent.find_all('b')[4]
        type = typeraw.get_text()
        return type

    def get_secondary_type():
        typeraw = pagecontent.find_all('b')[5]
        type = typeraw.get_text()
        return type

    #returns a list containing main abilities and a list containing hidden abilities
    def getability():
        abilitylist = []
        abilitysearch = pagecontent.find("span", string="Abilities")
        parent1 = abilitysearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        allabilities = parent3.find_all('span')
        for ability in allabilities:
            #is this spaghetti?
            abilityrefine = ability.get_text().replace('Hidden Ability','').strip().replace('\xa0','')
            abilitysplit = abilityrefine.split('or ',1)
            #for some reason there are invisible td tags containing "Cocophony" in every single ability table row
            if abilitysplit != ['Cacophony']:
                abilitylist.append(abilitysplit)
        #This code retrieves all the text in span tags in the row. Since the first span tag will always contain "abilities" the code always deletes the first list item
        del abilitylist [0]
        return (abilitylist)

    def get_category():
        categoryraw = pagecontent.find_all('span')[5]
        category = categoryraw.get_text()
        return category

    def get_height():
        heightsearch = pagecontent.find("span", string="Height")
        parent1 = heightsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        heightraw = parent3.findAll("td")[0]
        height = heightraw.get_text().strip()
        return (height)

    def get_weight():
        weightsearch = pagecontent.find("span", string="Weight")
        parent1 = weightsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        weightraw = parent3.findAll("td")[0]
        weight = weightraw.get_text().strip()
        return (weight)

    def get_color():

        colorsearch = pagecontent.find("span", string="Pokédex color")
        parent1 = colorsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        colorraw = parent3.findAll("td")[0]
        color = colorraw.get_text().strip()
        colorclear = color.replace("Other forms may have other colors.","")
        return(colorclear)

    def get_egg_group():
        egggroups = []
        eggsearch = pagecontent.find("span", string="Egg Groups")
        if str(eggsearch) == 'None':
            eggsearch = pagecontent.find("span", string="Egg Group")
        parent1 = eggsearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        eggraw = parent3.find_all("span")
        for span in eggraw:
            span = span.get_text().strip()
            if (span != "Egg Group") and (span != "Egg Groups"):
                egggroups.append(span)
        return(egggroups)
        
    def get_generation():
        generationraw = pagecontent.find_all('p')[1]
        generationzoom = generationraw.find_all('a')[3]
        generation = generationzoom.get('title')
        return generation

    #easy way for me to parse through all the different tags of a page, for debugging purposes only
    def attributesearch(targettag):
        for item in range (0,30):
            generation = pagecontent.find_all(targettag)[item]
            print ('----------------------------')
            print (item)
            print (generation)

    def getall():
        print (get_name())
        print (get_primary_type()), print (get_secondary_type())
        print (get_category())
        print (get_height())
        print (get_weight())
        print (get_egg_group())
        print('------------------------------')
    
    #generation = pagecontent.find_all('table')[59]
    #print(generation)