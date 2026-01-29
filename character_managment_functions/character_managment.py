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

from skills_this_be_isaacs_thing import available_skills,skills_choice

characters = set({"Name":"Example",
               "Race":"Example", 
               "Class":"Example", 
               "Level":1, 
               "Stats":{"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10}, 
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

def level_up(characters,character_name,skills_list):
    while True:
        choice = input("Would like to to gain +1 to a stat or gain a new skill? Skill/Stat").strip().capitalize()
        if choice == "Skill":
            skills_choice(available_skills,characters,character_name)
        elif choice == "Stat":
            while True:
                for key, value in characters[character_name["Stats"]]:
                    print(f"{key}: {value}")
                stat = input("What stat would you like to increase? Enter number:\n1. Strength\n2. Dexterity\n3. Constitution\n4. Wisdom\n5. Intellgience\n6. Charisma").strip()
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
    
create_character_stepone(species_list)





Items = {
    "Rouge_items": {
        "Weapons": {
            "Daggers": {
                "Description": "A pair of daggers.",
                "Weight": "2 pounds",
                "Value": "5 Gold pieces",
                "Damage": "1d4"
            },
            "Rapier": {
                "Description": "An old European sword with a thin, fast blade.",
                "Weight": "3 pounds",
                "Value": "25 Gold pieces",
                "Damage": "1d8"
            }
        },
        "Armor": {
            "Leather Armor": {
                "Description": "Basic leather armor",
                "Weight": "10 pounds",
                "Value": "10 Gold",
                "AC": "11 + Dex Modifier"
            }
        },
        "Other Items": {
            "Lockpicks": {
                "Description": "A set of lockpicks that can unlock many doors, if you have the skill.",
                "Value": "2 Gold",
                "Weight": "½ pound"
            },
            "Fake ID": {
                "Description": "A fake ID that can get you many places you shouldn’t be.",
                "Value": "Varies",
                "Weight": "Insignificant"
            }
        }
    },

    "Fighter_items": {
        "Weapons": {
            "Greatsword": {
                "Description": "A large two-handed sword ideal for heavy attacks.",
                "Weight": "6 pounds",
                "Value": "50 Gold pieces",
                "Damage": "2d6"
            },
            "Poleaxe": {
                "Description": "A versatile weapon with an axe blade, hammer, and spike.",
                "Weight": "7 pounds",
                "Value": "40 Gold pieces",
                "Damage": "1d10"
            }
        },
        "Armor": {
            "Chainmail": {
                "Description": "Interlocked metal rings providing solid protection.",
                "Weight": "20 pounds",
                "Value": "75 Gold",
                "AC": "16"
            },
            "Full Plate": {
                "Description": "Heavy plate armor covering the entire body.",
                "Weight": "50 pounds",
                "Value": "150 Gold",
                "AC": "18"
            }
        },
        "Other Items": {
            "Military Insignia": {
                "Description": "A symbol representing rank and affiliation.",
                "Value": "10 Gold",
                "Weight": "1 pound"
            },
            "Battle Trinket": {
                "Description": "A personal charm carried into battle for luck.",
                "Value": "5 Gold",
                "Weight": "Negligible"
            }
        }
    },

    "Barbarian_items": {
        "Weapons": {
            "Warhammer": {
                "Description": "A heavy hammer designed for crushing armor.",
                "Weight": "5 pounds",
                "Value": "30 Gold",
                "Damage": "1d8"
            },
            "Greataxe": {
                "Description": "A massive axe for devastating swings.",
                "Weight": "7 pounds",
                "Value": "35 Gold",
                "Damage": "1d12"
            }
        },
        "Armor": {
            "Chainmail": {
                "Description": "Interlocked metal rings providing solid protection.",
                "Weight": "20 pounds",
                "Value": "75 Gold",
                "AC": "16"
            }
        },
        "Other Items": {
            "Stress Toy": {
                "Description": "Something to make sure the barbarian doesn’t rage during a fine(ish) dinner, or any other situation.",
                "Value": "1 Gold",
                "Weight": "Negligible"
            },
            "Unidentified Blood Vial": {
                "Description": "A vial of blood that the barbarian won’t say where or what it’s from.",
                "Value": "Unknown",
                "Weight": "Negligible"
            }
        }
    },

    "Cleric_items": {
        "Weapons": {
            "Holy Staff": {
                "Description": "A staff imbued with divine power.",
                "Weight": "4 pounds",
                "Value": "20 Gold",
                "Damage": "1d6"
            }
        },
        "Armor": {
            "Robes": {
                "Description": "Simple robes that offer minimal protection.",
                "Weight": "3 pounds",
                "Value": "5 Gold",
                "AC": "10"
            },
            "Leather": {
                "Description": "Light leather armor for additional protection.",
                "Weight": "10 pounds",
                "Value": "10 Gold",
                "AC": "11 + Dex Modifier"
            }
        },
        "Other Items": {
            "Holy Symbol": {
                "Description": "A symbol representing the cleric's deity.",
                "Value": "15 Gold",
                "Weight": "1 pound"
            },
            "Scriptures": {
                "Description": "Religious texts for prayer and guidance.",
                "Value": "10 Gold",
                "Weight": "2 pounds"
            }
        }
    },

    "Wizard_items": {
        "Weapons": {
            "Magic Focus": {
                "Description": "An object used to channel magical energy.",
                "Weight": "1 pound",
                "Value": "30 Gold",
                "Damage": "Varies by spell"
            }
        },
        "Armor": {
            "Leather": {
                "Description": "Light armor providing minimal protection.",
                "Weight": "10 pounds",
                "Value": "10 Gold",
                "AC": "11 + Dex Modifier"
            }
        },
        "Other Items": {
            "Textbooks": {
                "Description": "Books full of spells, theories, and magical research.",
                "Value": "50 Gold",
                "Weight": "10 pounds"
            },
            "Really Cool Hat": {
                "Description": "A really tall wizard’s hat with stars and stuff on it.",
                "Value": "Undetermined",
                "Weight": "1 pound"
            }
        }
    },

    "Bard_items": {
        "Weapons": {
            "Instrument": {
                "Description": "A musical instrument used for performance and magic.",
                "Weight": "3 pounds",
                "Value": "25 Gold",
                "Damage": "1d4"
            }
        },
        "Armor": {
            "Leather": {
                "Description": "Light armor providing minimal protection.",
                "Weight": "10 pounds",
                "Value": "10 Gold",
                "AC": "11 + Dex Modifier"
            },
            "Chainmail": {
                "Description": "Interlocked metal rings providing solid protection.",
                "Weight": "20 pounds",
                "Value": "75 Gold",
                "AC": "16"
            }
        },
        "Other Items": {
            "Notepad": {
                "Description": "A book to jot down lyrics, stories, or magical notes.",
                "Value": "2 Gold",
                "Weight": "1 pound"
            },
            "Tuning Fork": {
                "Description": "A tuning fork for the bard’s instrument.",
                "Value": "5 Gold",
                "Weight": "1 pound"
            }
        }
    },

    "General_Items": {
        "Ropes": {
            "Description": "Strong ropes for climbing or tying objects.",
            "Value": "5 Gold",
            "Weight": "5 pounds"
        },
        "Torches": {
            "Description": "Standard torches for lighting dark areas.",
            "Value": "1 Gold",
            "Weight": "1 pound"
        },
        "First-aid kit": {
            "Description": "Basic supplies for treating wounds.",
            "Value": "10 Gold",
            "Weight": "3 pounds"
        },
        "Potions": {
            "Description": "Various potions for healing, mana, or temporary boosts.",
            "Value": "Varies",
            "Weight": "1 pound each"
        }
    }
}



def available_items(characters, character_name, items):
    Available_items = {}

    # Add general items
    for key in items["General_Items"].keys():
        Available_items[key] = items["General_Items"][key]

    # Add class-specific items
    match characters[character_name]["Class"]:
        case "Rouge":
            for key in items["Rouge_items"].keys():
                Available_items[key] = items["Rouge_items"][key]

        case "Fighter":
            for key in items["Fighter_items"].keys():
                Available_items[key] = items["Fighter_items"][key]

        case "Barbarian":
            for key in items["Barbarian_items"].keys():
                Available_items[key] = items["Barbarian_items"][key]

        case "Cleric":
            for key in items["Cleric_items"].keys():
                Available_items[key] = items["Cleric_items"][key]

        case "Wizard":
            for key in items["Wizard_items"].keys():
                Available_items[key] = items["Wizard_items"][key]

        case "Bard":
            for key in items["Bard_items"].keys():
                Available_items[key] = items["Bard_items"][key]

    return Available_items


def inspect_inventory(characters, character_name,items):
    while True:
        change = input("Would you like to add or remove items from your inventory? Y/N ").strip().capitalize()
        if change == "Y":
            while True:
                add_remove = input("Are you adding or removing something from the inventory? Add/Remove ").strip().capitalize()
                
                if add_remove == "Add":
                    available_items_list = available_items(characters, character_name, items)
                    
                    for i in characters[character_name]["Inventory"]:
                        if i in available_items_list:
                            available_items_list.pop(i)
                    
                    if len(characters[character_name]["Inventory"]) == 7:
                        print("Your inventory is at max capacity. You first need to remove something.")
                        continue
                    else:
                        for i in available_items_list:
                            print(i)
                    
                    item_to_add = input("What item would you like to add? Make sure to enter the name exactly as it is in the list. ")
                    check = input(f"Are you sure you want to add {item_to_add} to your inventory? Y/N ").strip().capitalize()
                    
                    if check == "Y":
                        characters[character_name]["Inventory"][item_to_add] = available_items_list[item_to_add]
                    break  
                
                elif add_remove == "Remove":
                    if len(characters[character_name]["Inventory"]) == 0:
                        print("You have nothing in your inventory to remove. Add something to it first.")
                        break
                    else:
                        for i in characters[character_name]["Inventory"]:
                            print(i)
                    
                    item_to_remove = input("What item would you like to remove? Enter the name exactly as it is seen on the list. ")
                    check = input(f"Are you sure you want to remove {item_to_remove} from your inventory? Y/N ").strip().capitalize()
                    
                    if check == "Y":
                        characters[character_name]["Inventory"].pop(item_to_remove)
                    break  
                
                else:
                    print("Please enter 'Add' or 'Remove'.")
                    continue
        
        elif change == "N":
            break
        
        else:
            print("Please enter 'Y' or 'N'.")


    

