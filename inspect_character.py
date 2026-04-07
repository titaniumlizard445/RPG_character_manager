#PS 1st Character inspection

#import from pryors stuff

#import attribute manager
from attribute_management import attribute_inspect
from character_managment import manage_inspect,characters,available_items
from UI_NOT_liam import print_indict_dictionaries
import utill_functions
#function for inventory changer (character chosen,character dictionary)










def inspect_inventory(characters,character_name):
    inventory=characters[character_name]["Inventory"]
    print_indict_dictionaries(characters,character_name,type="Inventory")
    while True:
        choise=utill_functions.get_valid_type(int,"0 to return\n1 to add something to your invintory\n2 to remove something from your inventory: ",valid=(0,2))
        if choise==0:
            return inventory
        elif choise==1:
            available_items_list=available_items()
            print("0 to return")
            item_names=[]
            for num,i in enumerate(available_items_list):
                print(f"{num+1} for {i}")
                maxi=num+1
                item_names.append(i)
            try:
                item_to_add=available_items_list[item_names[utill_functions.get_valid_type(int,"what do you want to add: ",valid=(0,maxi))-1]]
            except:
                break
            inventory[item_to_add]=available_items_list[item_to_add]
        
        elif choise==2:
            if len(inventory)==0:
                print("You have nothing in your inventory to remove. Add something to it first.")
                break
            print("0 to return")
            item_names=[]
            for num,i in enumerate(inventory):
                print(f"{num+1} for {i}")
                maxi=num+1
                item_names.append(i)
            try:
                item_to_add=[item_names[utill_functions.get_valid_type(int,"what do you want to remove: ",valid=(0,maxi))-1]]
            except:
                break
            inventory.pop(item_to_add)



def character_inspect_menu(characters,races,classes):
    if bool(characters)==False:
        print("You have no characters currently.")
        return
    print("0 to return")
    for num,i in enumerate(characters.keys()):
        print(f"{num+1} for {i}")
        maxi=num+1
    while True:
        try:
            character_name=characters.keys()[utill_functions.get_valid_type(int,"who do you want to inspect: ",valid=(0,maxi))-1]
        except:
            return
        manage_inspect(characters,character_name,races,classes)



