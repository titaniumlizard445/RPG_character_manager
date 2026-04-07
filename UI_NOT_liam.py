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
#define stupid proofed input (type return,prompt=input thy info,invalid prompt= that ain"t a valid input)
#	repeat forever
#		try
#			return type return input(prompt)
#		error
#			output(invalid prompt)
#	
#define search and compare (char dict)
#	repeat forever
#		if stupid proofed input(string,do you want to use (y/n))=n
#			return
#       output(char dict)
#  
# 		char1=char dict[stupid proofed input (string,what is the name of thy character you want to have as the first comparison for)]
#		char2=char dict[stupid proofed input (string,what is the name of thy character you want to have as the second comparison for)]
#		output(stat names)
#       stat=stat dict[stupid proofed input (string,what is the name of thy stat you want to have as the comparison for)]		
#		output(char1 name:stat for char1
#		char2 name: stat for char2)
#
#define user help():
#   repeat forever:
#       help with=stupid proofed input(int,1 for help with classes\n2 for help with level\n3 for help with inventory\n4 for help with attributes\n5 for help with skills\n6 to go back)
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
#           output(your class is like your job,it also sets what you have access to)
#the stupid proofed input 

# If the user is confused this function will help.
# Pryor: I don"t think we"re gonna be having a help function.
import utill_functions,update_base
import matplotlib.pyplot as plt
def stupid_input(type_return,prompt,invalid_prompt):
    while True:
        try:
            return type_return(input(prompt))
        except:
            print(invalid_prompt)

def user_help():
    print("Further Explanation")
    print("This program is intended to be used as a character manager for role-playing games such as D&D. It can hold characters and their details,including inventory,skills,and attributes.")
    print("Create Character: Go through the process to build a level one character.\nInspect Character: Look at the stats,inventory,attributes,or other details of a character that already exists.\nSearch Character: Search for a character by Name,Class,or Level.\nCompare Characters: Compare the skills and attributes of two different characters.")


def print_indict_dictionaries(characters,character_name,type):
    if type=="Stats":
        for k,v in characters[character_name]["Stats"].items():
            print(f"{k}:{v}")
    elif type=="Skills":
        for i in characters[character_name]["Skills"]:
            print(i)
    elif type=="Inventory":
        print(f"{character_name}'s Inventory")
        print(characters[character_name]["Inventory"])
        for ke,va in characters[character_name]["Inventory"].items():
            print(f"{ke}:\nDescription: {va["Description"]}\nValue: {va["Value"]}\nWeight: {va["Weight"]}\n")
   


def search_character(characters,classes):
    if bool(characters)==False:
        print("You have no characters.")
        return
    character_names=list(characters.keys())
    characters_found=[]
    amount_of_characters=len(characters)

    search_type=utill_functions.get_valid_type(int,"0 to return\n1 for Name\n2 for Class\n3 for Level: ",valid=(0,3))

    if search_type==1:
        
        print("Names:")
        for i in character_names:
            print(i)
        name=utill_functions.get_valid_type(str,"Enter name: ")
        if name in character_names:
            characters_found.append(name)

    elif search_type=="class":
        
        for num,x in enumerate(classes):
            print(f"{num+1} for {x}")

        class_name=classes[utill_functions.get_valid_type(int,"what do you want: ",valid=classes)]
        for i in range(amount_of_characters):
            if class_name==characters[character_names[i]]["class"]:
                characters_found.append(character_names[i])

    elif search_type=="level":
        
        level=utill_functions.get_valid_type(int,"Enter level (1-20) (only characters of this exact level will show up): ",valid=(1,20))
        for i in range(amount_of_characters):
            if level==str(characters[character_names[i]]["level"]):
                characters_found.append(character_names[i])

    for i in characters_found:
        
        print("Characters Found")
        print(f"{i},Level {characters[i]["Level"]} {characters[i]["Race"][0]} {characters[i]["Class"][0]}")


def character_comparison(characters):
    if len(characters.keys()) < 2:
        print("You need at least two character to be able to compare them.")
        return
    print("Character Names")
    
    count=0
    for i in characters.keys():
        count += 1
        print(f"{count} for {i}")
    maxi = count
    character_one = list(characters.keys())[utill_functions.get_valid_type(int,"what is the first character you want to compare: ",valid=(1,maxi))-1]

        
    character_two = list(characters.keys())[utill_functions.get_valid_type(int,"what is the second character you want to compare: ",valid=(1,maxi))-1]

    dnd_stats=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]

    print(f"{character_one}'s Attributes")
    print(characters[character_one]["story"])

    v1=update_base.data_visualisation()
    v1.axis.set_title(character_one) 
    v1.radar_graph(dnd_stats,list(characters[character_one]["stats"].values()))


    print(f"{character_two}'s Attributes")
    print(characters[character_two]["story"])

    v1=update_base.data_visualisation()
    v1.axis.set_title(character_two) 
    v1.radar_graph(dnd_stats,list(characters[character_two]["stats"].values()))
    plt.show()