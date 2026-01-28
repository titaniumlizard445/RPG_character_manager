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
import main
import character_managment_functions.character_managment
import Parker_Projects.attribute_management
import Parker_Projects.inspect_character
def check_each_char(word,type_checking):
    for x in word:
        if type_checking==int:
            if x in ["1","2","3","4","5","6","7","8","9","0"]:
                continue
            else:
                return False
        if type_checking==float:
            if x in ["1","2","3","4","5","6","7","8","9","0","."]:
                continue
            else:
                return False
        else:
            return True
    return True
def stupid_input(type_return,prompt="Input thy info: ",invalid_prompt="Invalid input"):
    while True:
        user_input=input(prompt)
        if check_each_char(user_input,type_return):
            return type_return(user_input)
        else:
            print(invalid_prompt)
def search_and_compare(char_dict,stats):
    while True:
        # Liam: Makes sure the user wants to use.
        # Pryor: They got here using a menu, this is redundant.
        if stupid_input(str,"Do you want to use (y/n): ")=="n"or len(char_dict)<2:
            if len(char_dict)<2:
                print("You dont have enough characters to compare.")
            return
        for char,names_for_char in char_dict.items():
            print(f"{char}:{names_for_char}")
        # Liam: Get the characters that you want to compare and the stat.
        while True:
            # Pryor: The characters will be saved as a set of dictionaries.
            # Pryor: Example Character
            # characters = set({"Name":"Example",
            #  "Race":"Example", 
            # "Class":"Example", 
            #"Level":1, 
            # "Stats":{"Stat1":"Example Num"}, 
            # "Skills":{"Skill_name":"Skill_desc"}, 
            # "Inventory":{"Item_name":"Item_desc"},})

            # Pryor: We might want to let the user choose how to search for the characters, such as by Name, Race, or Class.
            if user_input:= stupid_input(str,"What is the name of the first character that you want to compare: ")in char_dict:
                char1=char_dict[user_input]
                break
            else:
                print("There is no character with that name.")
        while True:  
            if user_input:= stupid_input(str,"What is the name of the second character that you want to compare: ")in char_dict:
                char2=char_dict[user_input]
                break
            else:
                print("There is no character with that name.")
        # Pryor: What is stats?
        for stat,val in stats.items():
            print(f"{stat}:{val}")
        while True:
            # Pryor: We're not just comparing the stats of the characters. We want to compare Class, Level, Race, and Stats.
            if user_input:= stupid_input(str,"What is the name of the stat that you want to compare from both characters stats: ") in char_dict:   
                # Pryor: There isn't a seperate stats dictionary.
                stat=stats[user_input]
                break
            else:
                print("There is no stat with that name.")
                # Pryor: This is written like each character has its own seperate dictionary.
        print(f"Character Name|{stat}\n{char1["name"]}:{char1[stat]}\n{char2["name"]}:{char2[stat]}")
# If the user is confused this function will help.
# Pryor: I don't think we're gonna be having a help function.
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
def main_menu(species,char_dict):
    while True:
        choice=stupid_input(int,"1 to inspect character\n2 to create new character\n3 to search and compare characters\n0 to quit")
        if choice==1:
            Parker_Projects.inspect_character.inspection_de_character(char_dict)
        if choice==2:
            character_managment_functions.character_managment.create_character_stepone(species)
        if choice==3:
            search_and_compare()
        if choice==0:
            return








# Liam: This is to debug.
if __name__=="__main__":
    test_char_dict={}
    test_stats={}
    print("""
     ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠾⠛⠋⠉⠉⠉⠉⠙⠛⠷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⠟⢁⣠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⠟⠁⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀⠀
⠀⠀⢀⡾⠁⢠⣾⡟⠁⠀⠀⠀⣠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀
⠀⢀⣾⠁⣠⣿⠏⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀
⠀⢸⡇⠀⣿⠏⠀⠀⢀⣴⣷⡀⠻⣿⣿⣿⣿⠟⢀⣾⣦⡀⠀⠀⠀⠀⠀⢸⡇⠀
⠀⢸⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⣤⠈⠁⣤⣴⣿⣿⣿⡇⠀⠀⠀⢰⠃⢸⡇⠀
⠀⠈⢿⡀⠀⠀⠀⠀⠀⠻⠿⡿⠿⠃⠀⠀⠘⠿⢿⠿⠟⠀⠀⠀⡰⠟⢀⡿⠁⠀
⠀⠀⠈⢿⣤⡀⠀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⠀⢀⣤⡿⠁⠀⠀
⠀⠀⠀⠀⠉⠛⠛⠋⣡⣤⣌⠙⠻⠶⣦⣴⠶⠟⠋⣡⣤⣌⠙⠛⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⢀⣴⣶⠄⠠⣶⣦⡀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡏⠈⢿⣿⠀⠀⣿⡿⠁⢹⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠀⠀⠉⠀⠀⠉⠀⠀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
      _      _                 _             
     | |    | |               (_)            
   __| | ___| |__  _   _  __ _ _ _ __   __ _ 
  / _` |/ _ \ '_ \| | | |/ _` | | '_ \ / _` |
 | (_| |  __/ |_) | |_| | (_| | | | | | (_| |
  \__,_|\___|_.__/ \__,_|\__, |_|_| |_|\__, |
                          __/ |         __/ |
                         |___/         |___/           """)
    while True:
        choice=stupid_input(int,"1 to test search and compare 2 to test user help 3 for main menu 0 to quit: ")
        if choice==1:
            search_and_compare(test_char_dict,test_stats)
        if choice==2:
            user_help()
        if choice==3:
            main_menu()
        if choice==0:
            quit()
# Liam: Yes I am a Metroid fan.
# Pryor: This ascii art just clutters your code.
# Liam: Tt's an artistic choice, programming is a form of art.