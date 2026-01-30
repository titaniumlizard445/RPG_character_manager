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


from skills import skills_available,skill_choice,skills_list



characters = {
    "Dorkus": {
        "Race": "Human",
        "Class": "Rogue",
        "Level": 1,
        "Stats": {
            "Strength": 13,
            "Dexterity": 13,
            "Constitution": 15,
            "Wisdom": 13,
            "Intelligence": 13,
            "Charisma": 13
        },
        "Skills": {
            "Sneak Attack": "Deals extra damage when attacking from stealth",
            "Lockpicking": "Can open locked doors and chests"
        },
        "Inventory": {
            "Dagger": "A small but sharp blade",
            "Lockpick Set": "Tools for opening locks"
        }
    },

    "Elowen": {
        "Race": "Elf",
        "Class": "Wizard",
        "Level": 1,
        "Stats": {
            "Strength": 8,
            "Dexterity": 14,
            "Constitution": 10,
            "Wisdom": 15,
            "Intelligence": 17,
            "Charisma": 12
        },
        "Skills": {
            "Firebolt": "Launches a small bolt of fire",
            "Arcane Knowledge": "Understands magical lore"
        },
        "Inventory": {
            "Spellbook": "Contains basic spells",
            "Mana Potion": "Restores magical energy"
        }
    },

    "Brom": {
        "Race": "Dwarf",
        "Class": "Fighter",
        "Level": 1,
        "Stats": {
            "Strength": 16,
            "Dexterity": 10,
            "Constitution": 16,
            "Wisdom": 12,
            "Intelligence": 10,
            "Charisma": 9
        },
        "Skills": {
            "Shield Block": "Reduces incoming damage",
            "Power Strike": "A strong melee attack"
        },
        "Inventory": {
            "Battle Axe": "A heavy axe for combat",
            "Shield": "Provides extra defense"
        }
    },

    "Nyssa": {
        "Race": "Halfling",
        "Class": "Barbarian",
        "Level": 1,
        "Stats": {
            "Strength": 11,
            "Dexterity": 16,
            "Constitution": 12,
            "Wisdom": 14,
            "Intelligence": 11,
            "Charisma": 13
        },
        "Skills": {
            "Archery": "Increased accuracy with bows",
            "Tracking": "Can follow enemy trails"
        },
        "Inventory": {
            "Short Bow": "A lightweight ranged weapon",
            "Rations": "Food for long journeys"
        }
    }
}


species_list = ["Human (+2 to Consitution)","Elf (+2 to Wisdom)","Dwarf (+2 to Strength)","Gnome (+2 to Intelligence)","Dragonborn (+2 to Dexterity)","Halfling (+2 to Charisma)"]
actual_species_list = ["Human","Elf","Dwarf","Gnome","Dragonborn","Halfling"]
stats_list = ["Strength","Dexterity","Constitution","Wisdom","Intelligence","Charisma"]

def create_character(species_list,characters): 
    new_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    while True:
        
        character_name = input("What will the name of your character be?\nEnter here: ").strip()
        
        check = input(f"Are you sure you want {character_name} to be your character's name? Y/N: ").strip().capitalize()
        if check == "Y":
            characters[character_name] = {}
            characters[character_name]["Level"] = 1
            break
        else:
            continue

    while True:
        
        print("Available Races")
        
        count = 0
        for i in species_list:
            count += 1
            print(f"{count}. {i}")
        
        race = input("What will the race of your character be?\nEnter here: ").strip().capitalize()
        if race not in actual_species_list:
            
            print("Invalid answer")
        else:
            
            check = input(f"Are you sure you want {character_name} to be a {race}? It cannot be changed later. Y/N: ").strip().capitalize()
            if check == "Y":
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
    available_classes = []
    if new_stats["Charisma"] >= 13:
        available_classes.append("Bard")
    if new_stats["Constitution"] >= 13:
        available_classes.append("Barbarian")        
    if new_stats["Dexterity"] >= 13:
        available_classes.append("Rouge")
    if new_stats["Wisdom"] >= 13:
        available_classes.append("Cleric")
    if new_stats["Strength"] >= 13:
        available_classes.append("Fighter")
    if new_stats["Intelligence"] >= 13:
        available_classes.append("Wizard")   
    
    print("Available Classes:")
    
    for i in available_classes:
        print(i)
    while True:
        
        class_choice = input("What class do you want to take?\nEnter here: ").strip().capitalize()
        if class_choice not in available_classes:
            
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
        available_skills = skills_available(characters,character_name,skills_list,level="Level")
        for _ in range(2):
            skill_choice(skills_list,available_skills,characters,create_character)
        break
    while True:
        
        break


def level_up(characters,character_name):
    while True:
        
        choice = input("Would like to to gain +1 to a stat or gain a new skill? Skill/Stat: ").strip().capitalize()
        if choice == "Skill":
            skill_choice(skills_available,characters,character_name)
        elif choice == "Stat":
            while True:
                for key, value in characters[character_name["Stats"]]:
                    print(f"{key}: {value}")
                
                stat = input("What stat would you like to increase? Enter number:\n1. Strength\n2. Dexterity\n3. Constitution\n4. Wisdom\n5. Intellgience\n6. Charisma\nEnter here:").strip()
                match stat:
                    case "1":
                        if characters[character_name]["Stats"]["Strength"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Strength"] += 1
                            break
                    case "2":
                        if characters[character_name]["Stats"]["Dexterity"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Dexterity"] += 1
                            break
                    case "3":
                        if characters[character_name]["Stats"]["Constitution"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Constitution"] += 1
                            break
                    case "4":
                        if characters[character_name]["Stats"]["Wisdom"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Wisdom"] += 1
                            break
                    case "5":
                        if characters[character_name]["Stats"]["Intelligence"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Intelligence"] += 1
                            break
                    case "6":
                        if characters[character_name]["Stats"]["Charisma"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Charisma"] += 1
                            break
                    case _:
                        
                        print("Invalid answer")
                        continue

def manage_inspect(characters,character_name):
    while True:
        
        print(f"Name: {character_name}\nRace: {characters[character_name]["Race"]}\nClass: {characters[character_name]["Class"]}\nLevel: {characters[character_name]["Level"]}")
        
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
                    elif new_level.isnumeric() is False or int(new_level) > 20 or new_level < characters[character_name]["Level"]:
                        
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
                        else:
                            continue
            else:
                
                print("Please enter 'Name' or 'Level'.")
                continue
                    
