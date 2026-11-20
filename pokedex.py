# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# i = int(input("What pokemon do you want to see?"))
# print(data[i])

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!



import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

# def first():
#     x = int(input("What pokemon do you want to see?"))
#     print(data[x])
# first()

def lang():
    language = input("What language do you want to see your pokemon in? 1 for English/2 for Japanese/3 for Chinese/4 for French")
    for pokemon in data:
        if language == "1":
            print(pokemon["name"]["english"])
        elif language == "2":
            print(pokemon["name"]["japanese"])
        elif language == "3":
            print(pokemon["name"]["chinese"])
        elif language == "4":
            print(pokemon["name"]["french"])
    # x = int(input("What pokemon do you want to see?"))
    # print(data[x])
    #need fix
lang()

def type():
    question = input("What pokemon type are you looking for?")
    found = False
    for pokemon in data:
        if question in [pokemon_type.lower() for pokemon_type in pokemon["type"]]:
            print(pokemon["name"]["english"])
            found=True
    if not found:
        print(f"Theres no valid {question}type")
type()

def poke():
    ask = input("What kind of pokemon are you looking for?")
    found = False
    for pokemon in data:
        if ask in [pokemon_name.lower() for pokemon_name in pokemon["name"]]:
            print(pokemon["name"]["english"])
            found=True                                                      
    if not found:                                                                                                                               
        print(f"Theres no valid {ask}pokemon")   
poke()