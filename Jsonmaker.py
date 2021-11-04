import re
from typing import Text
from bs4.element import Stylesheet
import requests
from bs4 import BeautifulSoup
#imports a table of every pokemon and their number from bulbapedia
website = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)"
for item in range (1,2):
    currentpage = requests.get(website)
    pagecontent = BeautifulSoup(currentpage.content,"html.parser")
    #this code searches for the national dex link at the top of the page then scrolls down to the next link
    nextpagelink = pagecontent.find('a', string = 'Pokémon')
    nextpagelink = nextpagelink.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    nextpagelink = nextpagelink.find_all('a')[0]
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

    def get_ability():
        abilitylist = []
        abilitysearch = pagecontent.find("span", string="Abilities")
        if str(abilitysearch) == 'None':
            abilitysearch = pagecontent.find("span", string="Ability")
        parent1 = abilitysearch.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        allabilities = parent3.find_all('td')[0]
        isolatedabilities = allabilities.find_all('a')
        for ability in isolatedabilities:
            abilityrefined = ability.get_text().replace('\xa0','').replace('\n','')
            abilitylist.append(abilityrefined)
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
        #Finds the substring "introduced in" and then returns the next X characters
        #firstparagraph is raw html and not the paragraph itself 
        firstparagraph = pagecontent.find_all('p')[1].get_text()
        Target_text_raw = re.search ('introduced in', str(firstparagraph))
        startmarker = (Target_text_raw.span()[-1]) + 1
        endmarker = startmarker + 14
        clippedparagraph = str(firstparagraph)[startmarker:endmarker]
        generation = clippedparagraph.replace('.','').strip()
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
        print (get_generation())
        print (get_ability())
        print (get_category())
        print (get_height())
        print (get_weight())
        print (get_egg_group())
        print (get_color())
        print('------------------------------')
        
    website = nextpageaddress
    
