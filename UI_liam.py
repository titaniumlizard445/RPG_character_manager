# THE search and comparison
# made by liam
#⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠾⠛⠋⠉⠉⠉⠉⠙⠛⠷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⣠⣴⠟⢁⣠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀
#⠀⠀⠀⢀⣼⠟⠁⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀⠀
#⠀⠀⢀⡾⠁⢠⣾⡟⠁⠀⠀⠀⣠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀
#⠀⢀⣾⠁⣠⣿⠏⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀
#⠀⢸⡇⠀⣿⠏⠀⠀⢀⣴⣷⡀⠻⣿⣿⣿⣿⠟⢀⣾⣦⡀⠀⠀⠀⠀⠀⢸⡇⠀
#⠀⢸⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⣤⠈⠁⣤⣴⣿⣿⣿⡇⠀⠀⠀⢰⠃⢸⡇⠀
#⠀⠈⢿⡀⠀⠀⠀⠀⠀⠻⠿⡿⠿⠃⠀⠀⠘⠿⢿⠿⠟⠀⠀⠀⡰⠟⢀⡿⠁⠀
#⠀⠀⠈⢿⣤⡀⠀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⠀⢀⣤⡿⠁⠀⠀
#⠀⠀⠀⠀⠉⠛⠛⠋⣡⣤⣌⠙⠻⠶⣦⣴⠶⠟⠋⣡⣤⣌⠙⠛⠛⠉⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⢀⣴⣶⠄⠠⣶⣦⡀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡏⠈⢿⣿⠀⠀⣿⡿⠁⢹⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠀⠀⠉⠀⠀⠉⠀⠀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#define stupid proofed input (type return, prompt=input thy info, invalid prompt= that ain't a valid input)
#	repeat forever
#		try
#			return type return input(prompt)
#		error
#			output(invalid prompt)
#	
#define search and compare (char dict)
#	repeat forever
#		if stupid proofed input(string, do you want to use (y/n))=n
#			return
#       output(char dict)
#  
# 		char1=char dict[stupid proofed input (string, what is the name of thy character you want to have as the first comparison for)]
#		char2=char dict[stupid proofed input (string, what is the name of thy character you want to have as the second comparison for)]
#		output(stat names)
#       stat=stat dict[stupid proofed input (string, what is the name of thy stat you want to have as the comparison for)]		
#		output(char1 name:stat for char1
#		char2 name: stat for char2)
#
#define user help():
#   repeat forever:
#       help with = stupid proofed input(int,1 for help with classes\n2 for help with level\n3 for help with inventory\n4 for help with attributes\n5 for help with skills\n6 to go back)
#       if help=6
#           return
#       else if 5:
#           output(skills are bonuses to abilities or new abilities)
#       else if 4:
#           output(attributes are your base stats such as strength or chiasma)
#       else if 3:
#           output(your inventory is what items you have)
#       else if 2:
#           output(your level is your overall power and at higher levels you can get new stuff such as items new abilities or other things)
#       else if1:
#           output(your class is like your job, it also sets what you have access to)
#the stupid proofed input 

# If the user is confused this function will help.
# Pryor: I don't think we're gonna be having a help function.
def stupid_input(type_return,prompt,invalid_prompt):
    while True:
        try:
            return type_return(input(prompt))
        except:
            print(invalid_prompt)

def user_help():
    while True:
        help_with=stupid_input(int,"1 for help with classes\n2 for help with level\n3 for help with inventory\n4 for help with attributes\n5 for help with skills\n6 to go back\nwhat do you want: ","that is not an option")
        # Pryor: You should be using match-case here.
        if help_with==6:
            return
        elif help_with==5:
            print("Skills are bonuses to abilities or new abilities.")
        elif help_with==4:
            print("Attributes are your base stats such as strength or chiasma.")
        elif help_with==3:
            print("Your inventory is what items you have.")
        elif help_with==2:
            print("Your level is your overall power and at higher levels you can get new stuff such as items new abilities or other things.")
        elif help_with==1:
            print("Your class is like your job, it also sets what skills you have access to.")
        else:
            print("That is not an option.")


def print_indict_dictionaries(characters, character_name, type):
    if type == "Stats":
        for k in characters[character_name]["Stats"].keys():
            print(f"{k}:{characters[character_name]['Stats'][k]}")
    elif type == "Skills":
        for k in characters[character_name]["Skills"].keys():
            print(f"{k}:{characters[character_name]['Skills'][k]}")
    elif type == "Inventory":
        for k in characters[character_name]["Inventory"].keys():
            print(f"{k}:{characters[character_name]['Inventory'][k]}")


def search_character(characters):
    character_names = list(characters.keys())
    characters_found = []
    amount_of_characters = len(characters)

    search_type = input("Search by Name, Class, or Level: ")

    if search_type == "Name":
        print("Names:")
        for i in character_names:
            print(i)
        name = input("Enter name: \n")
        if name in character_names:
            characters_found.append(name)

    elif search_type == "Class":
        print("Classes")
        print("Rouge\nFighter\nBarbarian\nCleric\nWizard\nBard")
        class_name = input("Enter class: \n")
        for i in range(amount_of_characters):
            if class_name == characters[character_names[i]]["Class"]:
                characters_found.append(character_names[i])

    elif search_type == "Level":
        level = input("Enter level (1-20) (Note: only characters of this exact level will show up.): ")
        for i in range(amount_of_characters):
            if level == str(characters[character_names[i]]["Level"]):
                characters_found.append(character_names[i])

    for i in characters_found:
        print("Characters Found")
        print(f"{i}, Level {characters[i]['Level']} {characters[i]['Race']} {characters[i]['Class']}")


def character_comparison(characters):
    print("Character Names")
    count = 0
    for i in characters.keys():
        count += 1
        print(f"{count}. {i}")

    while True:
        character_one = input("Enter first character to compare; Name must be entered exactly as seen on list.\nEnter here: ")
        if character_one not in list(characters.keys()):
            print("Invalid answer")
            continue
        else:
            break

    while True:
        character_two = input("Enter second character to compare; Name must also be entered exactly as seen on list.")
        if character_two not in list(characters.keys()):
            print("Invalid answer")
            continue
        else:
            break

    print(f"{character_one}'s Attributes")
    print_indict_dictionaries(characters, character_name=character_one, type="Stats")
    print(f"{character_one}'s Skills")
    print_indict_dictionaries(characters, character_name=character_one, type="Skills")

    print(f"{character_two}'s Attributes")
    print_indict_dictionaries(characters, character_name=character_two, type="Stats")
    print(f"{character_two}'s Skills")
    print_indict_dictionaries(characters, character_name=character_two, type="Skills")


"""1
Dave
y
Human
y
13
y
13
y
13
y
13
y
13
y
13
y
Bard
y
"""