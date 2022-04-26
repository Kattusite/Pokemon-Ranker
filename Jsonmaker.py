import re
from typing import Text
from bs4.element import Stylesheet
import requests
import json
from bs4 import BeautifulSoup

def jsonmake():
    list = {}
    space = " "
    #imports a table of every pokemon and their number from bulbapedia
    website = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)"
    print ("Downloading Pokemon Data")
    dexnumber = 1
    while space == " ":
        currentpage = requests.get(website)
        pagecontent = BeautifulSoup(currentpage.content,"html.parser")
        nextpagelink = pagecontent.find('a', string = 'Pokémon')
        nextpagelink = nextpagelink.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        nextpagelink = nextpagelink.find_all('a')[0]
        nextpageaddress = "https://bulbapedia.bulbagarden.net/" + str(nextpagelink.get('href'))
        
        def get_name():
            nameraw = pagecontent.find_all('p')[0]
            nametext = nameraw.get_text()
            name = nametext.split(space, 1)[0]
            return name

        def get_primary_type():
            typeraw = pagecontent.find_all('b')[5]
            type = typeraw.get_text()
            return type

        def get_secondary_type():
            typeraw = pagecontent.find_all('b')[6]
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
            height = heightraw.get_text().strip().replace('\\','')
            return str(height)

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
            #finds the first paragraph on the page
            firstparagraph = pagecontent.find_all('p')[0].get_text()
            #finds the string "introduced in" in the first paragraph
            Target_text_raw = re.search ('introduced in', str(firstparagraph))
            #isolates the "introduced in" substring
            startmarker = (Target_text_raw.span()[-1]) + 1
            #adds the next 14 characters (the data we want) to the isolated "introduced in"
            endmarker = startmarker + 14
            #removes the "introduced in" from the combined string
            clippedparagraph = str(firstparagraph)[startmarker:endmarker]
            generation = clippedparagraph.replace('.','').strip()
            return generation

        pokedict = {
            "Name" : get_name(),
            "National Dex Number" : dexnumber,
            "Primary Type" : get_primary_type(),
            "Secondary Type" : get_secondary_type(),
            "Generation" : get_generation(),
            "Ability" : get_ability(),
            "Category" : get_category(),
            "Height" : get_height(),
            "Weight" : get_weight(),
            "Egg Group" : get_egg_group(),
            "Color" : get_color(),
        }
        #adds the current pokemon to the list dictionary
        list[dexnumber] = pokedict
        website = nextpageaddress
        dexnumber += 1

        if nextpageaddress == "https://bulbapedia.bulbagarden.net//wiki/Bulbasaur_(Pok%C3%A9mon)":
            break
    #turns the list dictionary into a json file
    print (list)
    with open('list.json', 'w', encoding='utf8') as f:
        json.dump (list, f, indent=1)
    print ('Done')
