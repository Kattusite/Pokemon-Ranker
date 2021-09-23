pokemon = []
#removes quoation marks and commas, then moves it into a list
user_input = input ('Paste pokemon here')
user_input = user_input.replace ('"','')
user_input = user_input.strip(",")
pokemon = user_input.split()
print (pokemon)