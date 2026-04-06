#PS 1st Character inspection

#import from pryors stuff

#import attribute manager
from attribute_management import attribute_inspect
from character_managment import manage_inspect,characters,available_items,items
from UI_NOT_liam import print_indict_dictionaries
import utill_functions
#function for inventory changer (character chosen, character dictionary)










def inspect_inventory(characters,items, character_name):
    inventory = characters[character_name]["Inventory"]
    print_indict_dictionaries(characters,character_name,type="Inventory")
    while True:
        choise=utill_functions.get_valid_type(int,"0 to return\n1 to add something to your invintory\n2 to remove something from your inventory: ",valid=(0,2))
        if choise == "1":
            available_items_list = available_items()
            print("0 to return")
            for num,i in enumerate(available_items_list):
                print(f"{num+1} for {i}")
            try:
                item_to_add = available_items_list[]
            except:
                break
            check = input(f"Are you sure you want to add {item_to_add} to your inventory? Y/N: ").strip().capitalize()
            
            if check == "Y":
                inventory[item_to_add] = available_items_list[item_to_add]
            break  
        
        elif inventory_function == "Remove":
            if len(inventory) == 0:
                print("You have nothing in your inventory to remove. Add something to it first.")
                break
            else:
                for i in inventory:
                    print(i)
            
            item_to_remove = input("What item would you like to remove? Enter the name exactly as it is seen on the list.\nEnter here:  ")
            
            check = input(f"Are you sure you want to remove {item_to_remove} from your inventory? Y/N: ").strip().capitalize()
            
            if check == "Y":
                inventory.pop(item_to_remove)
            break  
        else:
            
            print("Please enter 'Add' or 'Remove'.")
            continue
                
        
        elif change == "N":
            break
        
        else:
            
            print("Please enter 'Y' or 'N'.")
            continue

        go_again = input("Would you like to continue with inventory inspection? Y/N:\n")
        if go_again == "Y":
            continue
        else:
            break

        
    return inventory



def character_inspect_menu(characters):
    
    print("Character Names")
    if bool(characters) == False:
        print("You have no characters currently.")
        return
    else:
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
                            inventory = inspect_inventory(characters, items, character_name)
                            characters[character_name]["Inventory"] = inventory
                        case "2":
                            attribute_inspect(characters,character_name)
                            pass
                        case "3":
                            print_indict_dictionaries(characters,character_name,type = "Skills")
                        case "4":
                            manage_inspect(characters,character_name)
                        case "5":
                            return
                        case _:
                            print("Please enter 1, 2, 3, 4, or 5 as your answer.")
                            continue
                    


    return inventory

