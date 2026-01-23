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
#define stupid profed input (type return, prompt=input thy info, invalid prompt= that aint a valid input)
#	reapete forever
#		try
#			return type return input(prompt)
#		error
#			output(invalid prompt)
#	
#define search and compare (char dict)
#	reapete forever
#		if stupid profed input(string, do you want to use (y/n))=n
#			return
#       output(char dict)
#  
# 		char1=char dict[stupid profed input (string, what is the name of thy chariucter you whant to have as the firstt comnparason for)]
#		char2=char dict[stupid profed input (string, what is the name of thy chariucter you whant to have as the second comnparason for)]
#		output(stat names)
#       stat=stat dict[stupid profed input (string, what is the name of thy stat you whant to have as the comnparason for)]		
#		output(char1 name:stat for char1
#		char2 name: stat for char2)
#
#define user help():
#   repete forevver:
#       help with = stupid profed input(int,1 for help with classes\n2 for help with level\n3 for help with inventory\n4 for help with attrabutes\n5 for help with skills\n6 to go back)
#       if help=6
#           return
#       else if 5:
#           output(skills are bonusus to ablillitys or new abilitys)
#       else if 4:
#           output(attrabutes are your bace stats such as strength or carizzma)
#       else if 3:
#           output(your inventory is what items you have)
#       else if 2:
#           output(your level is your overall power and at higher levels you can get new stuff such as items new abillitys or other things)
#       else if1:
#           output(your class is like your job, it also sets what you have acsses to)
#the stupid profed input 
def stupid_input(type_return,propt="imput thy infoooo: ",invillid_prompt="invalid input"):
    while True:
        try:
            return type_return(input(propt))
        except:
            print(invillid_prompt)
def serch_and_compare(char_dict,stats):
    while True:
        #makes shure the user whants to use
        if stupid_input(str,"do you want to use (y/n): ")=="n"or len(char_dict)<2:
            if len(char_dict)<2:
                print("you dont have enugh charitcters to compare")
            return
        print(char_dict)
        #get the charicters that you want to compare and the stat
        while True:
            try:   
                char1=char_dict[stupid_input(str,"what is the name of the first charicter that you want to compare: ")]
                break
            except:
                print("there is no charicter with that name")
        while True:
            try:   
                char2=char_dict[stupid_input(str,"what is the name of the second charicter that you want to compare: ")]
                break
            except:
                print("there is no charicter with that name")
        print(stats)
        while True:
            try:   
                stat=stats[stupid_input(str,"what is the name of the stat that you whant to compare from both charsicters: ")]
                break
            except:
                print("there is no stat with that name")
        print(f"charicter name|{stat}\n{char1["name"]}:{char1[stat]}\n{char2["name"]}:{char2[stat]}")
# if the user is confused this function will help
def user_help():
    while True:
        help_with=stupid_input(int,"1 for help with classes\n2 for help with level\n3 for help with inventory\n4 for help with attrabutes\n5 for help with skills\n6 to go back\nwhat do you want: ","that is not an option")
        if help_with==6:
            return
        elif help_with==5:
            print("skills are bonusus to ablillitys or new abilitys")
        elif help_with==4:
            print("attrabutes are your bace stats such as strength or carizzma")
        elif help_with==3:
            print("your inventory is what items you have")
        elif help_with==2:
            print("your level is your overall power and at higher levels you can get new stuff such as items new abillitys or other things")
        elif help_with==1:
            print("your class is like your job, it also sets what you have acsses to")
        else:
            print("that is not an option")
#this is to debug
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
        choise=stupid_input(int,"1 to test serch and compare 2 to test user help 3 to quit: ")
        if choise==1:
            serch_and_compare(test_char_dict,test_stats)
        if choise==2:
            user_help()
        if choise==3:
            quit()