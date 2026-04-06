#PS 1st attribute manager
#

#
from character_managment import characters
from UI_liam import print_indict_dictionaries
import utill_functions

#function called attribute_manager(character dictionary, character chosen)

def attribute_manager(char_dict,character):
  #Display attributes of chosen character
  
  print(char_dict[character]["stats"])
  #Input for user to choose if they want to change any of them
  
  use = utill_functions.get_valid_type(str,"Would you like to change any of the attributes? (y/n): ",valid=["y","n"])
  #if yes
  if use == "y":
    #for each attribute
    for x in char_dict[character]["stats"]:
      #display the attribute
      print(f"Would you like to change: {char_dict[character]["stats"][x]}")
      #ask user if they want to change that attribute
      change = utill_functions.get_valid_type(str,"Would you like to change any of the attributes? (y/n): ",valid=["y","n"])
      #if yes
      if change == "y":
        #ask for what they want to update the value to
        new_value = utill_functions.get_valid_type(int,f"What is the new value for: {char_dict[character]["stats"][x.keys()]}: ",valid=(0,30))
        #Update the value
        char_dict[character]["stats"][x] = new_value
    #display that it is done with the attribute changer
  #return character dictionary
  return char_dict

def stat_change(characters,character_name,stat):
  while True:
    
    new_stat = utill_functions.get_valid_type(int,f"What do you want to change {stat} to? It cannot go above 30 or below 0: ",valid=(0,30))
    check = utill_functions.get_valid_type(str,"Would you like to change any of the attributes? (y/n): ",valid=["y","n"])
    if check == "y":
      characters[character_name]["Stats"][stat] = int(new_stat)
      break
    else:
      continue

def attribute_inspect(characters,character_name):
  while True:
    print_indict_dictionaries(characters, character_name, type = "Stats")
    
    change = utill_functions.get_valid_type(str,"Would you like to change any of the attributes? (y/n): ",valid=["y","n"])
    if change == "n":
      return
    elif change == "y":
      
      stat_to_change = utill_functions.get_valid_type("1 for Strength\n2 for Dexterity\n3 for Constitution\n4 forIntelligence\n5 for Wisdom\n6 for Charisma\nWhat stat do you want to change: ")
      match stat_to_change:
        case "1":
          stat_change(characters,character_name,stat = "Strength")
          break
        case "2":
          stat_change(characters,character_name,stat = "Dexterity")
          break
        case "3":
          stat_change(characters,character_name,stat = "Constitution")
          break
        case "4":
          stat_change(characters,character_name,stat = "Intelligence")
          break
        case "5":
          stat_change(characters,character_name,stat = "Wisdom")
          break
        case "6":
          stat_change(characters,character_name,stat = "Charisma")
          break
        case 0:
          break

