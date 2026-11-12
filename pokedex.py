# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# i = int(input("What pokemon do you want to see?"))
# print(data[i])


# # Add a language choice feature and print the pokemons name based on the user input

# # Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# #Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


# #Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!



import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
while True:
    language = int(input("What language do you want to see your pokemon in? e for English/j for Japanese/c for Chinese/f or French"))
    if () == "e":
        print(data[english])
        break
    elif () == "j":
        print(data[japanese])
        break
    elif () == "c":
        print(data[chinese])
        break
    elif () == "f":
        print(data[french])
        break
x = int(input("What pokemon do you want to see?"))
print(data[i])
print(data[x])