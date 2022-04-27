from importlib.resources import path
from pickle import TRUE
import csv
import re
import ast
import os.path
from os import path
import json
import jsonmaker

rankedlist=[]
listholder = {}
#Python uses this list to denote the field names in the correct order
fieldnameorder = ['Name','Primary Type','Secondary Type','Generation','Primary Ability', 'Secondary Ability', 'Hidden Ability', 'Height', 'Weight', 'Primary Egg Group', 'Secondary Egg Group', 'Color', ]
#checks to see if the pokemon data has already been stored, and then downloads it if not


if path.exists('list.json') == False:
    jsonmaker.jsonmake()

def paste():
    user_input = input ('Paste pokemon here')
    #Returns the substring location of the beginning and ending character of "favorites":
    start_text = re.search ('"favorites":', user_input)
    #Returns the substring position of the ending character
    startmarker = (start_text.span()[-1])
    end_text =  re.search (',"settings"', user_input)
    endmarker = (end_text.span()[0])
    #deletes everything before the last character of start_text and everything after the first character of end_text
    rawnumbers = (user_input[startmarker:endmarker])
    #converts the harvested string into a list
    list = ast.literal_eval(rawnumbers)
    return list

#loops through the imported list and adds the pokemon data sorted by preference
position = 0
for number in paste():
    with open('list.json') as json_file:
        data = json.load(json_file)
        listholder = (data[number])
        rankedlist.append(listholder)
        position += 1

#exports the rankedlist dict in csv
with open('rankedlist.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnameorder)
    writer.writeheader()
    writer.writerows(rankedlist)
    print('Finished')
    
