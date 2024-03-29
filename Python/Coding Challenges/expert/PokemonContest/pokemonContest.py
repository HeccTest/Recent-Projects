"""
Project

    You are given data containing information for the first 100 Pokémon as well as special effectiveness relationships. Use this data to define a function that takes two Pokémon numbers and calculates which Pokémon wins based on their types.

    How to calculate?
        Given two Pokémon, say #3 (Venusaur) and #6 (Charizard), use the given data to obtain their respective types—(grass, poison), (fire, flying).
        We'll start with Venusaur. His first type is grass. For each of Venusaur's opponent's types, use the data to obtain grasss effectiveness. The grass is 0.5x (not very) effective against both fire and flying. Multiply these together: 0.5 * 0.5 = 0.25. So 'grass' is 0.25 effective against Charizard. You'll repeat this with Venusaur's second type, poison, and Venusar will receive two scores for his two types: (0.25, 1.0). Average these together to get Venusaur's final score: 0.625. When Pokémon only have one type they will only have one score and no averaging is necessary.
        When you've done this for both Pokémon you'll end up with two scores—one for each Pokémon. Return the number of the Pokémon with the higher score or return -1 for a tie.

Examples

    pk_special_winner(33, 28) ➞ 28

    pk_special_winner(77, 52) ➞ -1

    pk_special_winner(25, 44) ➞ 44

    pk_special_winner(57, 51) ➞ -1

    pk_special_winner(98, 34) ➞ 98

Notes

    - A type is doubled when it is very effective and halved for not very effective uses. For combinations, such as fire against a bug and grass type Pokémon, the effectiveness scores are multiplied. So fire would be four times as effective against such an opponent. See bulbapedia link below for more information.
    - Note that when a Pokémon has two types they will have two effectiveness scores and this function requires these to be averaged. Don't mix up the multiplications and averages.
    Thanks to the providers of the data:

    https://www.kaggle.com/dizzypanda/gen-1-pokemon
    https://bulbapedia.bulbagarden.net/wiki/Type

    LINK: https://edabit.com/challenge/KudhhsvJygnEzx8tZ

    Bonus Challenge
        Which Pokémon beats the most of its opponents in this dataset? See my answer in the comments.

Thoughts

    - since this is only gen 1 pokemon, a couple things apply
        - only 15 types to consider, the other types were not introduced yet at this point
        - each pokemon at this point in time only have at most 2 types, and at least 1 type; [1,2]
	- dictionary given will tell us type 1 and type 2, if it has one (returns None, if no 2nd type). But does not say the number of types otherwise. May need to use a try, except.
	-   pk1[type1] -> pk2[type1] * pk2[type2]
        pk1[type2] -> ^
        pk2[type1] -> pk1[type1] * pk1[type2]
        pk2[type2] -> ^
	- If type2 = none. I should return 1, so when multiplied, result from type1 is unmodified
	- pokemon dex number (ie. 1 for bulbasaur) will be at pk_data index: num - 1 (ie. bulbasaur is located at pk_data[0])


"""

pk_data = [ { "Number": 1, "Name": "Bulbasaur", "Type1": "grass", "Type2": "poison" }, { "Number": 2, "Name": "Ivysaur", "Type1": "grass", "Type2": "poison" }, { "Number": 3, "Name": "Venusaur", "Type1": "grass", "Type2": "poison" }, { "Number": 4, "Name": "Charmander", "Type1": "fire", "Type2": None }, { "Number": 5, "Name": "Charmeleon", "Type1": "fire", "Type2": None }, { "Number": 6, "Name": "Charizard", "Type1": "fire", "Type2": "flying" }, { "Number": 7, "Name": "Squirtle", "Type1": "water", "Type2": None }, { "Number": 8, "Name": "Wartortle", "Type1": "water", "Type2": None }, { "Number": 9, "Name": "Blastoise", "Type1": "water", "Type2": None }, { "Number": 10, "Name": "Caterpie", "Type1": "bug", "Type2": None }, { "Number": 11, "Name": "Metapod", "Type1": "bug", "Type2": None }, { "Number": 12, "Name": "Butterfree", "Type1": "bug", "Type2": "flying" }, { "Number": 13, "Name": "Weedle", "Type1": "bug", "Type2": "poison" }, { "Number": 14, "Name": "Kakuna", "Type1": "bug", "Type2": "poison" }, { "Number": 15, "Name": "Beedrill", "Type1": "bug", "Type2": "poison" }, { "Number": 16, "Name": "Pidgey", "Type1": "normal", "Type2": "flying" }, { "Number": 17, "Name": "Pidgeotto", "Type1": "normal", "Type2": "flying" }, { "Number": 18, "Name": "Pidgeot", "Type1": "normal", "Type2": "flying" }, { "Number": 19, "Name": "Rattata", "Type1": "normal", "Type2": None }, { "Number": 20, "Name": "Raticate", "Type1": "normal", "Type2": None }, { "Number": 21, "Name": "Spearow", "Type1": "normal", "Type2": "flying" }, { "Number": 22, "Name": "Fearow", "Type1": "normal", "Type2": "flying" }, { "Number": 23, "Name": "Ekans", "Type1": "poison", "Type2": None }, { "Number": 24, "Name": "Arbok", "Type1": "poison", "Type2": None }, { "Number": 25, "Name": "Pikachu", "Type1": "electric", "Type2": None }, { "Number": 26, "Name": "Raichu", "Type1": "electric", "Type2": None }, { "Number": 27, "Name": "Sandshrew", "Type1": "ground", "Type2": None }, { "Number": 28, "Name": "Sandslash", "Type1": "ground", "Type2": None }, { "Number": 29, "Name": "Nidoran", "Type1": "poison", "Type2": None }, { "Number": 30, "Name": "Nidorina", "Type1": "poison", "Type2": None }, { "Number": 31, "Name": "Nidoqueen", "Type1": "poison", "Type2": "ground" }, { "Number": 32, "Name": "Nidoran", "Type1": "poison", "Type2": None }, { "Number": 33, "Name": "Nidorino", "Type1": "poison", "Type2": None }, { "Number": 34, "Name": "Nidoking", "Type1": "poison", "Type2": "ground" }, { "Number": 35, "Name": "Clefairy", "Type1": "normal", "Type2": None }, { "Number": 36, "Name": "Clefable", "Type1": "normal", "Type2": None }, { "Number": 37, "Name": "Vulpix", "Type1": "fire", "Type2": None }, { "Number": 38, "Name": "Ninetales", "Type1": "fire", "Type2": None }, { "Number": 39, "Name": "Jigglypuff", "Type1": "normal", "Type2": None }, { "Number": 40, "Name": "Wigglytuff", "Type1": "normal", "Type2": None }, { "Number": 41, "Name": "Zubat", "Type1": "poison", "Type2": "flying" }, { "Number": 42, "Name": "Golbat", "Type1": "poison", "Type2": "flying" }, { "Number": 43, "Name": "Oddish", "Type1": "grass", "Type2": "poison" }, { "Number": 44, "Name": "Gloom", "Type1": "grass", "Type2": "poison" }, { "Number": 45, "Name": "Vileplume", "Type1": "grass", "Type2": "poison" }, { "Number": 46, "Name": "Paras", "Type1": "bug", "Type2": "grass" }, { "Number": 47, "Name": "Parasect", "Type1": "bug", "Type2": "grass" }, { "Number": 48, "Name": "Venonat", "Type1": "bug", "Type2": "poison" }, { "Number": 49, "Name": "Venomoth", "Type1": "bug", "Type2": "poison" }, { "Number": 50, "Name": "Diglett", "Type1": "ground", "Type2": None }, { "Number": 51, "Name": "Dugtrio", "Type1": "ground", "Type2": None }, { "Number": 52, "Name": "Meowth", "Type1": "normal", "Type2": None }, { "Number": 53, "Name": "Persian", "Type1": "normal", "Type2": None }, { "Number": 54, "Name": "Psyduck", "Type1": "water", "Type2": None }, { "Number": 55, "Name": "Golduck", "Type1": "water", "Type2": None }, { "Number": 56, "Name": "Mankey", "Type1": "fighting", "Type2": None }, { "Number": 57, "Name": "Primeape", "Type1": "fighting", "Type2": None }, { "Number": 58, "Name": "Growlithe", "Type1": "fire", "Type2": None }, { "Number": 59, "Name": "Arcanine", "Type1": "fire", "Type2": None }, { "Number": 60, "Name": "Poliwag", "Type1": "water", "Type2": None }, { "Number": 61, "Name": "Poliwhirl", "Type1": "water", "Type2": None }, { "Number": 62, "Name": "Poliwrath", "Type1": "water", "Type2": "fighting" }, { "Number": 63, "Name": "Abra", "Type1": "psychic", "Type2": None }, { "Number": 64, "Name": "Kadabra", "Type1": "psychic", "Type2": None }, { "Number": 65, "Name": "Alakazam", "Type1": "psychic", "Type2": None }, { "Number": 66, "Name": "Machop", "Type1": "fighting", "Type2": None }, { "Number": 67, "Name": "Machoke", "Type1": "fighting", "Type2": None }, { "Number": 68, "Name": "Machamp", "Type1": "fighting", "Type2": None }, { "Number": 69, "Name": "Bellsprout", "Type1": "grass", "Type2": "poison" }, { "Number": 70, "Name": "Weepinbell", "Type1": "grass", "Type2": "poison" }, { "Number": 71, "Name": "Victreebel", "Type1": "grass", "Type2": "poison" }, { "Number": 72, "Name": "Tentacool", "Type1": "water", "Type2": "poison" }, { "Number": 73, "Name": "Tentacruel", "Type1": "water", "Type2": "poison" }, { "Number": 74, "Name": "Geodude", "Type1": "rock", "Type2": "ground" }, { "Number": 75, "Name": "Graveler", "Type1": "rock", "Type2": "ground" }, { "Number": 76, "Name": "Golem", "Type1": "rock", "Type2": "ground" }, { "Number": 77, "Name": "Ponyta", "Type1": "fire", "Type2": None }, { "Number": 78, "Name": "Rapidash", "Type1": "fire", "Type2": None }, { "Number": 79, "Name": "Slowpoke", "Type1": "water", "Type2": "psychic" }, { "Number": 80, "Name": "Slowbro", "Type1": "water", "Type2": "psychic" }, { "Number": 81, "Name": "Magnemite", "Type1": "electric", "Type2": None }, { "Number": 82, "Name": "Magneton", "Type1": "electric", "Type2": None }, { "Number": 83, "Name": "Farfetchd", "Type1": "normal", "Type2": "flying" }, { "Number": 84, "Name": "Doduo", "Type1": "normal", "Type2": "flying" }, { "Number": 85, "Name": "Dodrio", "Type1": "normal", "Type2": "flying" }, { "Number": 86, "Name": "Seel", "Type1": "water", "Type2": None }, { "Number": 87, "Name": "Dewgong", "Type1": "water", "Type2": "ice" }, { "Number": 88, "Name": "Grimer", "Type1": "poison", "Type2": None }, { "Number": 89, "Name": "Muk", "Type1": "poison", "Type2": None }, { "Number": 90, "Name": "Shellder", "Type1": "water", "Type2": None }, { "Number": 91, "Name": "Cloyster", "Type1": "water", "Type2": "ice" }, { "Number": 92, "Name": "Gastly", "Type1": "ghost", "Type2": "poison" }, { "Number": 93, "Name": "Haunter", "Type1": "ghost", "Type2": "poison" }, { "Number": 94, "Name": "Gengar", "Type1": "ghost", "Type2": "poison" }, { "Number": 95, "Name": "Onix", "Type1": "rock", "Type2": "ground" }, { "Number": 96, "Name": "Drowzee", "Type1": "psychic", "Type2": None }, { "Number": 97, "Name": "Hypno", "Type1": "psychic", "Type2": None }, { "Number": 98, "Name": "Krabby", "Type1": "water", "Type2": None }, { "Number": 99, "Name": "Kingler", "Type1": "water", "Type2": None }, { "Number": 100, "Name": "Voltorb", "Type1": "electric", "Type2": None } ]
type_effectiveness = {'bug': {'bug': 1, 'electric': 1, 'fighting': 0.5, 'fire': 0.5, 'flying': 0.5, 'ghost': 0.5, 'grass': 2, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 2, 'rock': 1, 'water': 1}, 'electric': {'bug': 1, 'electric': 0.5, 'fighting': 1, 'fire': 1, 'flying': 2, 'ghost': 1, 'grass': 0.5, 'ground': 0, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 2}, 'fighting': {'bug': 0.5, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 0.5, 'ghost': 0, 'grass': 1, 'ground': 1, 'ice': 2, 'normal': 2, 'poison': 0.5, 'psychic': 0.5, 'rock': 2, 'water': 1}, 'fire': {'bug': 2, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 1, 'ghost': 1, 'grass': 2, 'ground': 1, 'ice': 2, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 0.5}, 'flying': {'bug': 2, 'electric': 0.5, 'fighting': 2, 'fire': 1, 'flying': 1, 'ghost': 1, 'grass': 2, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'ghost': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 2, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 0, 'poison': 1, 'psychic': 2, 'rock': 1, 'water': 1}, 'grass': {'bug': 0.5, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 0.5, 'ghost': 1, 'grass': 0.5, 'ground': 2, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 1, 'rock': 2, 'water': 2}, 'ground': {'bug': 0.5, 'electric': 2, 'fighting': 1, 'fire': 2, 'flying': 0, 'ghost': 1, 'grass': 0.5, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 2, 'psychic': 1, 'rock': 2, 'water': 1}, 'ice': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 2, 'ghost': 1, 'grass': 2, 'ground': 2, 'ice': 0.5, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 0.5}, 'normal': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 0, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'poison': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 0.5, 'grass': 2, 'ground': 0.5, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'psychic': {'bug': 1, 'electric': 1, 'fighting': 2, 'fire': 1, 'flying': 1, 'ghost': 1, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 2, 'psychic': 0.5, 'rock': 1, 'water': 1}, 'rock': {'bug': 2, 'electric': 1, 'fighting': 0.5, 'fire': 2, 'flying': 2, 'ghost': 1, 'grass': 1, 'ground': 0.5, 'ice': 2, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 1}, 'water': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 2, 'flying': 1, 'ghost': 1, 'grass': 0.5, 'ground': 2, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 2, 'water': 0.5}}

def pk_special_winner(pk1, pk2):
	# comparing pk1 to pk2
    pk1_type1_eff = 1
    pk1_type2_eff = 1
    selfType = pk_data[pk1 - 1]["Type1"]
    for i in range(1, 3):
        enemyType = pk_data[pk2 - 1]["Type" + str(i)]
        if(enemyType == None): # if enemy does not have a type, then ignore. Enemy will always have at least one type; the first will always exist
            None
        else:
            pk1_type1_eff *= type_effectiveness[selfType][enemyType]

    selfType = pk_data[pk1 - 1]["Type2"]
    if(selfType == None): # if pk1 does not have a second type
        None
    else:
        for i in range(1, 3):
            enemyType = pk_data[pk2 - 1]["Type" + str(i)]
            if(enemyType == None):
                None
            else:
                pk1_type2_eff *= type_effectiveness[selfType][enemyType]
            
    pk1Effectiveness = (pk1_type1_eff + pk1_type2_eff) / 2

    # comparing pk2 to pk1
    pk2_type1_eff = 1
    pk2_type2_eff = 1
    selfType = pk_data[pk2 - 1]["Type1"]
    for i in range(1, 3):
        enemyType = pk_data[pk1 - 1]["Type" + str(i)]
        if(enemyType == None):
            None
        else:
            pk2_type1_eff *= type_effectiveness[selfType][enemyType]

    selfType = pk_data[pk2 - 1]["Type2"]
    if(selfType == None): # if pk2 does not have a second type
        None
    else:
        for i in range(1, 3):
            enemyType = pk_data[pk1 - 1]["Type" + str(i)]
            if(enemyType == None):
                None
            else:
                pk2_type2_eff *= type_effectiveness[selfType][enemyType]
            
    pk2Effectiveness = (pk2_type1_eff + pk2_type2_eff) / 2
    
    # figure out which pokemon has greater effectiveness
    if(pk1Effectiveness > pk2Effectiveness):
        return(pk1)
    elif(pk1Effectiveness == pk2Effectiveness): # a tie. Both pokemon have equal effectiveness
        return(-1)
    else:
        return(pk2)

# INITIAL TESTING (below are the failed test cases)

# FAIL: test_28 (__main__.testPokemonContest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\Kai\Desktop\Python\Coding Challenges\expert\PokemonChallenge\test_pokemonContest.py", line 90, in test_28
#     self.assertEqual(pk_special_winner(9, 62), -1)
# AssertionError: 62 != -1

# ======================================================================
# FAIL: test_38 (__main__.testPokemonContest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\Kai\Desktop\Python\Coding Challenges\expert\PokemonChallenge\test_pokemonContest.py", line 120, in test_38
#     self.assertEqual(pk_special_winner(72, 99), -1)
# AssertionError: 72 != -1

# ======================================================================
# FAIL: test_70 (__main__.testPokemonContest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\Kai\Desktop\Python\Coding Challenges\expert\PokemonChallenge\test_pokemonContest.py", line 216, in test_70
#     self.assertEqual(pk_special_winner(80, 98), -1)
# AssertionError: 80 != -1

# ======================================================================
# FAIL: test_84 (__main__.testPokemonContest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\Kai\Desktop\Python\Coding Challenges\expert\PokemonChallenge\test_pokemonContest.py", line 258, in test_84
#     self.assertEqual(pk_special_winner(79, 96), -1)
# AssertionError: 79 != -1

# ALL OF THESE FAILED CASES HAVE ONE POKEMON WITH ONLY 1 TYPE. Look into calculations relating to pokemone with 1 type.
# Fixed by taking the average of type1_effectiveness and type2_effectiveness, even when the pokemone does not have a second type.

# Tested and complete Aug. 4, 2023. See test_pokemonContest.py for test cases.