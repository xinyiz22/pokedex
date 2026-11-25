import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

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
        if ask.lower() in pokemon["name"]["english"].lower():
            print(pokemon["name"]["english"])
            found=True                                                      
    if not found:                                                                                                                               
        print(f"Theres no valid {ask} pokemon")   
poke()

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

import json
move = open("./moves.json", encoding="utf8")
cheese = json.load(moves.file)
def apple():
    ask = input("What pokemon's possible moves would you like to see?")
    for moves in cheese:
        if ask.lower() in pokemon["name"]["english"].lower():
            print(pokemon["name"]["english"])                                                   
        else:                                                                                                                               
            print(f"Theres no valid {ask} pokemon move")   
apple()
