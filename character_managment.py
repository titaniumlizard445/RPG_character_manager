# CB 1st Character Manager Pseudocode
# characters=({"Name":"Example","Class":"Example","Level":1,"Stats":{"Stat1":Example Num},"Skills":{"Skill_name":"Skill_desc"},"Inventory":{"Item_name":"Item_desc"}})

# skills_list=[]

# classes_list=[]

# define function create_character():
    # new_character={}
    # stats_dictionary={"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10} (Note: These are just placeholders)
    # skills_dictionary={}
    # while True:
        # ask user for character name
        # save character name in a variable
        # have user choose race (human,elf,dwarf,gnome,dragonborn,halfling)
        # have user set level
        # ask user if these choices are okay,display name choice and race choice
        # if yes:
            # append character name and level to new_character dictionary
            # apply race based attribute bonuses to attributes dictionary
            # break
        # if no:
            # continue
    # while True:
        # ask user to enter attributes (use a for loop)
        # if an attribute is bigger than 20:
            # tell user to enter a different thing that is less than 20
        # once user has entered all their attributes:
            # display attributes
            # ask if these are okay
            # if yes:
                # Set stats_dictionary attributes
                # break
            # if no:
                # reset attributes
                # continue
    # while True:
        # ask user to choose class (display list of available classes based off of attributes)
        # ask user if this choice is okay (display class choice)
        # if yes:
            # break
        # if no:
            # continue
    # while True:
        # ask user to choose skills (combat,support,misc) available skills are based off of attributes
        # once user has chosen as many skills as their level is,ask if these choices are okay
        # if yes:
            # break
        # if no:
            # reset skills
            # continue

# define function level_up():
    # while True:
        # ask user if they want a stat boost or a new skill
        # if stat:
            # have user choose a stat to add 1 to
            # if that stat would go over 20:
                # have user choose a different stat
            #else:

                # break
        # if skill:
            # have user choose a skill to gain that they don"t already have
            # break

# define function manage_inspect():
    # while True:
        # display Name,Race,Level,and Class of inspected character
        # ask user if they want to change character name or level
        # if Name:
            # have user enter new name for character
            # ask user if they want to continue changing stuff
            # if yes:
                # continue
            # if no:
                # return to character inspect menu
        # if Level:
            # have user set new level that is higher then current level
            # if new level <= current level:
                # tell user to set a different level
            # else:
                # per new level:
                    # run level_up() function



import random,utill_functions,update_base
from faker import Faker
characters={
    
}
def available_items():
    fake=Faker()
    stuff={}
    for x in range(15):
        word=fake.word()
        color=fake.color_name()
        stuff[f"{color} {word}:"]={"Description": f"{color} {word} from {fake.city()}","Weight": f"{random.randint(1,100)} pounds","Value": f"{random.randint(1,100)} gold"}
    return stuff
def create_inventory(character_name):
    inventory={}
    for _ in range(7):
        available_items_list=available_items()               
        for i in inventory.keys():
            if i in available_items_list.keys():
                available_items_list.pop(i)
        while True:
            print("Available Items:")
            print("0 to return")
            for num,i in enumerate(available_items_list):
                print(f"{num+1} for {i}")
            maxi=len(available_items_list)
            choice=utill_functions.get_valid_type(int,"What do you want: ",valid=(0,maxi))
            if choice==0:
                break
            item_to_add=available_items_list[choice-1]
            check=utill_functions.get_valid_type(str,"Would you like to add that item? (y/n): ",valid=["y","n"])
            if check=="y":
                inventory[item_to_add]=available_items_list[item_to_add]
                break
            else:
                continue

    return inventory

def create_character(species_list,classes_list,characters): 
    new_stats={"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    stats_list=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
    if utill_functions.get_valid_type(str,"do you want a random character (y/n): ",valid=["y","n"])=="y":
        rc=update_base.RandomGenerator()
        character=rc.random_character()
        name=character["name"]
        characters[name]={}
        characters[name]["level"]=1
        characters[name]["race"]=tuple([character["race"]])
        characters[name]["stats"]=character["stats"]
        characters[name]["description"]=character["description"]
        characters[name]["origin"]=character["origin"]
        characters[name]["class"]=tuple([character["class"]])
        characters[name]["story"]=character["story"]
        characters[name]["inventory"]=available_items()
        return
    while True:
        
        character_name=utill_functions.get_valid_type(str,"What is the name of your character: ")
        
        check=utill_functions.get_valid_type(str,f"do you want {character_name} to be your characters name (y/n): ",valid=["y","n"])
        if check=="y":
            characters[character_name]={}
            characters[character_name]["level"]=1
            level=1
            break
        else:
            continue

    while True:
        
        print("Available Races")
        for num,i in enumerate(species_list):
            print(f"{num+1} for {i}")
        maxi=len(species_list)
        race=species_list[utill_functions.get_valid_type(int,"What is your race: ",valid=(1,maxi))-1]
        check=utill_functions.get_valid_type(str,f"Do you want {character_name} to be a {race} (y/n): ",valid=["y","n"])
        if check=="y":
            race=tuple([race])
            characters[character_name]["race"]=race
            break
    while True:
        for i in stats_list:
            while True:
                
                final_stat=utill_functions.get_valid_type(int,f"What is your {i}: ",valid=(0,30))
                    
                check=utill_functions.get_valid_type(str,f"{i}: {final_stat}:\nis this what you want (y/n): ",valid=["y","n"])
                if check=="y":
                    new_stats[i]=final_stat
                    break
                else:
                    continue
        characters[character_name]["stats"]=new_stats
        break   
    print("Available Classes:")
    for num,i in enumerate(classes_list):
        print(f"{num+1} for {i}")
    maxi=len(classes_list)
    while True:
        
        class_choice =classes_list[utill_functions.get_valid_type(int,"what class do you want: ",valid=(1,maxi))-1]    
        check=utill_functions.get_valid_type(str,f"do you want {class_choice} to be your class(y/n): ",valid=["y","n"])
        if check=="y":
            class_choice=tuple([class_choice])
            characters[character_name]["class"]=class_choice
            break
        else:
            continue
    
    while True:
        inventory=create_inventory(character_name)
        characters[character_name]["inventory"]=inventory
        break
    story=utill_functions.get_valid_type(str,"what is your characters story (you can always change this later): \n")
    characters[character_name]["story"]=story
    characters[character_name]["description"]=utill_functions.get_valid_type(str,"what is the description of your character: ")
    characters[character_name]["origin"]=utill_functions.get_valid_type(str,"what is the origin of your character: ")

    print("Character Creation Finished!")
    return


def level_up(characters,character_name):
    new_level = utill_functions.get_valid_type(int,"what is your new level: ",valid=(1,20))
    if new_level <= characters[character_name]["level"]:
        print("New level must be higher than current level")
        return
    characters[character_name]["level"] = new_level
    return
def manage_inspect(characters,character_name,races,classes):
    while True:
        print(f"Name: {character_name}\nRace: {str(characters[character_name]["race"][0])}\nClass: {str(characters[character_name]["class"][0])}\nLevel: {characters[character_name]["level"]}\ndescription:{characters[character_name]["description"]}\norigin:{characters[character_name]["origin"]}\n{characters[character_name]["story"]}")
        choise=utill_functions.get_valid_type(int,"0 to return\n1 to change name\n2 to change race\n3 to change description\n4 to change origin\n5 to change class\n6 to change story\n7 to change level: ")
        if choise==0:
            return
        elif choise==1:    
            new_name=utill_functions.get_valid_type(str,"Enter the new name for your character: ")  
            check=utill_functions.get_valid_type(str,f"Are you sure you want {new_name} to be the name of your character(y/n): ",valid=["y","n"])
            if check=="y":
                characters[new_name]=characters.pop(character_name)
                character_name=new_name
            else:
                continue
        elif choise==2:
            while True:
                print("0 to return")
                for num,x in enumerate(races):
                    print(f"{num+1} for {x}")
                maxi=len(races)
                choice=utill_functions.get_valid_type(int,"what do you want: ",valid=(0,maxi))
                if choice==0:
                    break
                try:
                    race=races[choice-1]
                    if utill_functions.get_valid_type(str,f"do you want {race} to be your new race(y/n): ",valid=["y","n"])=="y":
                        characters[character_name]["race"]=tuple([race])
                        break
                except:
                    continue
        elif choise==3:
            characters[character_name]["description"]=utill_functions.get_valid_type(str,"what is the new description of your character: ")
        elif choise==4:
            characters[character_name]["origin"]=utill_functions.get_valid_type(str,"what is the new origin of your character: ")

        elif choise==5:
            while True:
                print("0 to return")
                for num,x in enumerate(classes):
                    print(f"{num+1} for {x}")
                maxi=len(classes)
                choice=utill_functions.get_valid_type(int,"what do you want: ",valid=(0,maxi))
                if choice==0:
                    break
                try:
                    classs=classes[choice-1]
                    if utill_functions.get_valid_type(str,f"do you want {classs} to be your new class(y/n): ",valid=["y","n"])=="y":
                        characters[character_name]["class"]=tuple([classs])
                        break
                except:
                    continue
        elif choise==6:
            characters[character_name]["story"]=utill_functions.get_valid_type(str,"what is the new story of your character: \n")
        elif choise==7:
            level_up(characters,character_name)
                
