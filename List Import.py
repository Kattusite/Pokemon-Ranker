import re
import ast

pokemon = []
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
print('-------------------------------------------------')
print (list)