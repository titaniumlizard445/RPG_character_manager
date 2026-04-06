# CB 1st Character Manager Pseudocode
# characters = ({"Name":"Example", "Class":"Example", "Level":1, "Stats":{"Stat1":Example Num}, "Skills":{"Skill_name":"Skill_desc"}, "Inventory":{"Item_name":"Item_desc"}})

# skills_list = []

# classes_list = []

# define function create_character():
    # new_character = {}
    # stats_dictionary = {"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10} (Note: These are just placeholders)
    # skills_dictionary = {}
    # while True:
        # ask user for character name
        # save character name in a variable
        # have user choose race (human, elf, dwarf, gnome,dragonborn,halfling)
        # have user set level
        # ask user if these choices are okay, display name choice and race choice
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
        # ask user to choose skills (combat, support, misc) available skills are based off of attributes
        # once user has chosen as many skills as their level is, ask if these choices are okay
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
            # have user choose a skill to gain that they don't already have
            # break

# define function manage_inspect():
    # while True:
        # display Name, Race, Level, and Class of inspected character
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



import faker, random,utill_functions,update_base
characters = {
    
}
def available_items():
    fake = faker()
    stuff={}
    for x in 15:
        word=fake.word()
        color=fake.color_name()
        stuff[f"{color} {word}:"]={"Description": f"{color} {word} from {fake.city()}","Weight": f"{fake.random_int(min=1, max=100)} pounds","Value": f"{faker.random_int(min=1,max=100)} gold"}
    return stuff
def create_inventory(character_name,items):
    inventory = {}
    for _ in range(7):
        available_items_list = available_items(characters, character_name, items)               
        for i in inventory.keys():
            if i in available_items_list.keys():
                available_items_list.pop(i)
        while True:
            print("Available Items:")
            print("0 to return")
            for num,i in enumerate(available_items_list):
                print(f"{num} for {i}")
                maxi=num
            item_to_add = available_items_list[utill_functions.get_valid_type("What do you want: ",valid=(0,maxi))]
            check = utill_functions.get_valid_type(str,"Would you like to add that item? (y/n): ",valid=["y","n"])
            if check == "y":
                inventory[item_to_add] = available_items_list[item_to_add]
                break
            else:
                continue

    return inventory

def create_character(species_list,classes_list,characters): 
    new_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    stats_list=['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    if utill_functions.get_valid_type(str,"do you want a random character (y/n): ",valid=["y","n"])=="y":
        character=update_base.RandomGenerator.random_character()
        characters[character["name"]]={}
        characters[character["name"]]["race"]=character["race"]
        characters[character["name"]]["stats"]=character["stats"]
        characters[character["name"]]["description"]=character["description"]
        characters[character["name"]]["origin"]=character["origin"]
        characters[character["name"]]["class"]=character["class"]
        characters[character["name"]]["story"]=character["story"]

    while True:
        
        character_name = utill_functions.get_valid_type(str,"What is the name of your character: ")
        
        check = utill_functions.get_valid_type(str,f"do you want {character_name} to be your characters name (y/n): ",valid=["y","n"])
        if check == "y":
            characters[character_name] = {}
            characters[character_name]["Level"] = 1
            level = 1
            break
        else:
            continue

    while True:
        
        print("Available Races")
        for i in species_list:
            print(i)
        race = utill_functions.get_valid_type(str,"What is your race: "valid=species_list)
        check = utill_functions.get_valid_type(f"Do you want {character_name} to be a {race} (y/n): ",valid=["y","n"])
        if check == "y":
            race = tuple([race])
            characters[character_name]["Race"] = race
            match race:
                case "Human":
                    new_stats["Constitution"] += 2
                case "Elf":
                    new_stats["Wisdom"] += 2
                case "Dwarf":
                    new_stats["Strength"] += 2
                case "Gnome":
                    new_stats["Intelligence"] += 2
                case "Dragonborn":
                    new_stats["Dexterity"] += 2
                case "Halfling":
                    new_stats["Charisma"] += 2
            break
        else:
            continue
    while True:
        for i in stats_list:
            while True:
                
                stat = input(f"What do you want your base stat for {i} to be?")
                if stat.isnumeric() == False:
                    
                    print("Invalid answer")
                    continue
                else:
                    stat = int(stat)
                    final_stat = new_stats[i] + stat
                    if final_stat > 20:
                        
                        print("That would make the stat go over 20. Please enter a lower number.")
                        continue
                    else:
                        
                        check = input(f"{i}: {final_stat}. Are you sure this is what you want? Y/N: ").strip().capitalize()
                        if check == "Y":
                            new_stats[i] = final_stat
                            break
                        else:
                            continue
        characters[character_name]["Stats"] = new_stats
        break   
    print("Available Classes:")
    for i in classes_list:
        print(i)
    while True:
        
        class_choice = input("What class do you want to take?\nEnter here: ").strip().capitalize()
        if class_choice not in classes_list:
            print("Invalid answer")
        else:
            
            check = input(f"Are you sure you want to take {class_choice} as your class? Y/N: ").strip().capitalize()
            if check == "Y":
                class_choice = tuple([class_choice])
                characters[character_name]["Class"] = class_choice
                break
            else:
                continue
    
    while True:
        inventory = create_inventory(character_name,)
        characters[character_name]["Inventory"] = inventory
        break
    
    print("Character Creation Finished!")
    return


def level_up(characters,character_name):
    characters[character_name]["level"]=utill_functions.get_valid_type(int,"what is your new level: ",valid=(1,20))
    return
def manage_inspect(characters,character_name):
    while True:
        print(f"Name: {character_name}\nRace: {str(characters[character_name]["Race"][0])}\nClass: {str(characters[character_name]["Class"][0])}\nLevel: {characters[character_name]["Level"]}")
        change = input("Would you like to edit the Name or Level of your character? Y/N: ").strip().capitalize()
        if change == "N":
            break
        elif change == "Y":
            
            item_to_change = input("Name or Level?\nEnter here: ").strip().capitalize()
            if item_to_change == "Name":
                while True:
                    
                    new_name = input("Enter the new name of your character: ")
                    
                    check = input(f"Are you sure you want {new_name} to tbe the name of your character? Y/N: ").strip().capitalize()
                    if check == "Y":
                        characters[new_name] = characters[character_name].pop()
                        character_name = new_name
                    else:
                        continue
            elif item_to_change == "Level":
                while True:
                    
                    print(f"Current Level: {characters[character_name]["Level"]}")
                    
                    new_level = input("What do you want to change your level to? It can only be increased. Type 'Exit' to go back to the inspect menu.\nEnter here: ").strip().capitalize()
                    if new_level == "Exit":
                        return character_name
                    elif new_level.isnumeric() is False or int(new_level) > 20 or int(new_level) < characters[character_name]["Level"]:
                        print("Please enter a valid answer.")
                        continue
                    else:
                        
                        check = input(f"Are you sure you want to set your character's level to {new_level}? Y/N: ").strip().capitalize()
                        if check == "Y":
                            old_level = characters[character_name]["Level"]
                            new_level = int(new_level)
                            characters[character_name]["Level"] = new_level
                            for _ in range(new_level - old_level):
                                level_up(characters,character_name)
                            break
                        else:
                            continue
            else:
                
                print("Please enter 'Name' or 'Level'.")
                continue
                    
