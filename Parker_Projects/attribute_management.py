#PS 1st attribute manager

#function called attribute_manager(character dictionary, character chosen)
def attribute_manager(char_dict,character):
  #Display attributes of chosen character
  print(char_dict[character]["stats"])
  #Input for user to choose if they want to change any of them
  use = input("Would you like to change any of the attributes? (y/n): ").strip().lower()
  #if yes
  if use == "y":
    #for each attribute
    for x in char_dict[character]["stats"]:
      #display the attribute
      print(f"Would you like to change: {char_dict[character]["stats"][x]}")
      #ask user if they want to change that attribute
      change = input("Enter here y/n: ").strip().lower()
      #if yes
      if change == "y":
        #ask for what they want to update the value to
        new_value = int(input(f"Enter the number for: {char_dict[character]["stats"][x.keys()]} here:").strip())
        #Update the value
        char_dict[character]["stats"][x] = new_value
    #display that it is done with the attribute changer
    print("attribute changer is done")
  #return character dictionary
  return char_dict
