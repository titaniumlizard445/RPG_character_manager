#PS 1st Character inspection

#import from pryors stuff

#import attribute manager
from attribute_management import attribute_inspect
from character_managment import manage_inspect,characters
from UI_liam import print_indict_dictionaries
#function for inventory changer (character chosen, character dictionary)



items = {
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
    available_items = {}

    # Add general items
    for key in items["General_Items"].keys():
        available_items[key] = items["General_Items"][key]

    # Add class-specific items
    match characters[character_name]["Class"]:
        case "Rouge":
            for key in items["Rouge_items"].keys():
                available_items[key] = items["Rouge_items"][key]

        case "Fighter":
            for key in items["Fighter_items"].keys():
                available_items[key] = items["Fighter_items"][key]

        case "Barbarian":
            for key in items["Barbarian_items"].keys():
                available_items[key] = items["Barbarian_items"][key]

        case "Cleric":
            for key in items["Cleric_items"].keys():
                available_items[key] = items["Cleric_items"][key]

        case "Wizard":
            for key in items["Wizard_items"].keys():
                available_items[key] = items["Wizard_items"][key]

        case "Bard":
            for key in items["Bard_items"].keys():
                available_items[key] = items["Bard_items"][key]

    return available_items


def inspect_inventory(characters,items, character_name):
    while True:
        change = input("Would you like to add or remove items from your inventory? Y/N: ").strip().capitalize()
        if change == "Y":
            while True:
                add_remove = input("Are you adding or removing something from the inventory? Add/Remove: ").strip().capitalize()
                
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
                    
                    item_to_add = input("What item would you like to add? Make sure to enter the name exactly as it is in the list.\nEnter here:  ")
                    check = input(f"Are you sure you want to add {item_to_add} to your inventory? Y/N: ").strip().capitalize()
                    
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
                    
                    item_to_remove = input("What item would you like to remove? Enter the name exactly as it is seen on the list.\nEnter here:  ")
                    check = input(f"Are you sure you want to remove {item_to_remove} from your inventory? Y/N: ").strip().capitalize()
                    
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



def character_inspect_menu(characters):
    print("Character Names")
    for i in characters.keys():
        print(i)
    while True:
        character_name = input("What character do you want to inspect? Enter name exactly as seen on the list: ").strip()
        if character_name not in list(characters.keys()):
            print("Enter a valid name.")
        else:
            while True:
                inspect_type = input(f"Do you want to inspect {character_name}'s inventory, attributes, skills, or race and class? Enter number:\n1. Inventory\n2. Attributes\n3. Skills\n4. Race and Class\n5. Return to main menu\nEnter here:\n")
                match inspect_type:
                    case "1":
                        inspect_inventory(characters, character_name, items)
                    case "2":
                        attribute_inspect(characters,character_name)
                        pass
                    case "3":
                        print_indict_dictionaries(characters,character_name,type = "Skills")
                    case "4":
                        manage_inspect(characters,character_name)
                    case "5":
                        break
                    case _:
                        print("Please enter 1, 2, 3, 4, or 5 as your answer.")
                        continue
                    
