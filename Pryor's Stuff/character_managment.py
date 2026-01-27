# CB 1st Character Manager Pseudocode
# characters = ({"Name":"Example", "Class":"Example", "Level":1, "Stats":{"Stat1":Example Num}, "Skills":{"Skill_name":"Skill_desc"}, "Inventory":{"Item_name":"Item_desc"}})

# skills_list = []

# classes_list = []

# define function create_character():
    # new_character = {}
    # stats_dictionary = {"Strength":10,"Dexterity":10,"Consititution":10,"Wisdom":10,"Intelligence":10,"Charisma":10} (Note: These are just placeholders)
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
        # ask user to choose class (display list of avaiable classes based off of attributes)
        # ask user if this choice is okay (display class choice)
        # if yes:
            # break
        # if no:
            # continue
    # while True:
        # ask user to choose skills (combat, support, misc) avaiable skills are based off of attributes
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


characters = ({"Name":"Example",
               "Race":"Example", 
               "Class":"Example", 
               "Level":1, 
               "Stats":{"Stat1":"Example Num"}, 
               "Skills":{"Skill_name":"Skill_desc"}, 
               "Inventory":{"Item_name":"Item_desc"},})

species_list = ["Human (+2 to Consitution)","Elf (+2 to Wisdom)","Dwarf (+2 to Strength)","Gnome (+2 to Intelligence)","Dragonborn (+2 to Dexterity)","Halfling (+2 to Charisma)"]
actual_species_list = ["Human","Elf","Dwarf","Gnome","Dragonborn","Halfling"]
stats_list = ["Strength","Dexterity","Constitution","Wisdom","Intelligence","Charisma"]

def create_character_stepone(species_list):
    new_character = {}
    new_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    while True:
        name = input("What will the name of your character be?").strip()
        check = input(f"Are you sure you want {name} to be your character's name? Y/N").strip().capitalize()
        if check == "Y":
            new_character["Name"] = name
            break
        else:
            continue

    while True:
        print("Available Races")
        count = 0
        for i in species_list:
            count += 1
            print(f"{count}. {i}")
        race = input("What will the race of your character be?").strip().capitalize()
        if race not in actual_species_list:
            print("Invalid answer")
        else:
            check = input(f"Are you sure you want {name} to be a {race}? It cannot be changed later. Y/N").strip().capitalize()
            if check == "Y":
                race = tuple(race)
                new_character["Race"] = race
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
                        check = input(f"{i}: {final_stat}. Are you sure this is what you want? Y/N").strip().capitalize()
                        if check == "Y":
                            new_stats[i] = final_stat
                            break
                        else:
                            continue
        new_character["Stats"] = new_stats
        break
    available_classes = []
    if new_stats["Charisma"] >= 13:
        available_classes.append("Bard")
    if new_stats["Constitution"] >= 13:
        available_classes.append("Barbarian")        
    if new_stats["Dexterity"] >= 13:
        available_classes.append("Rouge")
    if new_stats["Wisdom"] >= 13:
        available_classes.append("Wizard")
    if new_stats["Strength"] >= 13:
        available_classes.apppend("Fighter")
    if new_stats["Intelligence"] >= 13:
        available_classes.append("Sorcerer")   
    print("Available Classes:")
    for i in available_classes:
        print(i)
    while True:
        class_choice = input("What class do you want to take?").strip().capitalize()
        if class_choice not in available_classes:
            print("Invalid answer")
        else:
            check = input(f"Are you sure you want to take {class_choice} as your class? Y/N").strip().capitalize()
            if check == "Y":
                new_character["Class"] = class_choice
                break
            else:
                continue
    
    print(new_character)
    
create_character_stepone(species_list)
    

