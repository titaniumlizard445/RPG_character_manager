#PS 1st Character inspection

#function for inventory changer (character chosen, character dictionary)
    #loop until user is done with inventory management
        #greet user
        #display options for inventory (change inventory, display inventory or leave)
        #loop until user chooses valid option
            #input to choose option
            #if the valid option is chosen
                #leave loop
            #else
                #display to user how to fix their input
        #if display inventory is chosen
            #display the inventory
        #if change inventory is chosen
            #loop until done with inventory changer
                #Ask to add or remove items from the inventory
                #if add is chosen
                    #create storage dictionary for all values
                    #have user input name of the item
                    #have user input the value
                    #have user input a description
                    #have user input attributes
                    #store all the of the information in the dictionary
                    #add that to the player's inventory
                #if remove was chosen
                    #ask for the name of the item to remove or put leave if they don't want to input anything
                    #if the input is leave
                        #tell user they left remover
                    #else
                        #find the item in the inventory
                        #confirm that they want to remove this item
                        #if yes
                            #remove it
                #ask if the user is done with the inventory changer
                #if yes
                    #break out of loop
        #ask if user is done with the inventory changer
            #if yes
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
