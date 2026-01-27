#PS 1st Character inspection

#import from pryors stuff

#function for inventory changer (character chosen, character dictionary)
def inventory_changer(character,char_dict):
    #loop until user is done with inventory management
    while True:
        #greet user
        print("Welcome to the inventory changer\n")
        #display options for inventory (change inventory, display inventory or leave)
        print("\nWould you like to \n1)change inventory \n2)display inventory\n3)leave\n")
        #loop until user chooses valid option
        while True:
            #input to choose option
            choice = input("Enter the number here: ").strip()
            #if the valid option is chosen
            #leave loop
            match choice:
                case "1":
                    break
                case "2":
                    break
                case "3":
                    break
                #else
                    #display to user how to fix their input
                case _:
                    print("please input a valid value")
        #if display inventory is chosen
        if choice == "1":
            #display the inventory
            print(f"{character}'s inventory consists of: {char_dict[character]["inventory"]}")
        #if change inventory is chosen
        if choice == "2":
            #loop until done with inventory changer
            while True:
                #Ask to add or remove items from the inventory
                type_of_change = input("Would you like to add items or remove items from your inventory?\nEnter here (add/remove):").strip().lower()
                #if add is chosen
                if type_of_change == "add":
                    #create storage dictionary for all values
                    storage = {}
                    #have user input name of the item
                    name = input("What is the name of the item: ").strip().title()
                    #have user input the value
                    worth = float(input(f"What is number for the worth of {name}").strip())
                    #have user input a description
                    desc = input(f"Please write a description for {name} here:").strip()
                    #have user input an attribute
                    attribute = input("Please write a attribute in the form of: (attribute:what the attribute does) here:").strip()
                    #store all the of the information in the dictionary
                    storage = {
                        "name":name,
                        "worth":worth,
                        "description":desc,
                        "attribute":attribute}
                    #add that to the player's inventory
                    char_dict[character]["inventory"].update(storage)
                #if remove was chosen
                if choice == "3":
                    #ask for the name of the item to remove or put leave if they don't want to input anything
                    if not char_dict[character]["inventory"]:
                        #if the input is leave
                            #tell user they left remover
                        print("You don't have anything in the inventory to remove, leaving item remover...")
                    #else
                    else:
                        #find the item in the inventory
                        item_to_remove = input("Please Enter the name of the item you would like to remove here: ").strip().title()
                        #confirm that they want to remove this item
                        certain = input("Are you sure you want to remove this item? (y/n):").strip().lower()
                        #if yes
                        if certain == "y":
                            #remove it
                            char_dict[character]["inventory"].remove(item_to_remove)
                #ask if the user is done with the inventory changer
                done = input("are you done using the item changer? (y/n): ")
                #if yes
                if done == "y":
                    #break out of loop
                    break
        #ask if user is done with the inventory changer
        if done == "y":
            #if yes
            break
                #leave
    #return character dictionary

#function for character inspection (characters dictionary)
    #Display list of characters
    #Input for which character they want to inspect
    #Display options for what part of the character they would like to inspect (Class, Level, Inventory, Attributes, skills, Leave ,or Help Button)
    #Input for choosing one of the displayed options
    #if they choose inventory
        #call inventory changer function
    #or if they choose attributes
        #use function from attribute_management.py
    #or if they choose class & Level
        #go to Class and level function
    #or if they go to skills
        #Go to skills menu
    #if they choose leave
        #exit this function
    #if they ask for help
        #display a brief help guide
    #return character dictionary
