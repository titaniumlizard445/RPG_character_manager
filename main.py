#PS main file for character manager
from character_managment import create_character,characters
from UI_NOT_liam import character_comparison,search_character,user_help
from inspect_character import character_inspect_menu
import utill_functions

species_list=["Human","Elf","Dwarf","Halfling","Dragonborn","Gnome","Tiefling","Aasimar","Goliath","Orc","Tabaxi","Warforged","Genasi","Lizardfolk","Changeling"]
classes=["Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
def reinstate_csv(new_data,file):
    file.overwrite_all(new_data)
def main_menu():
    try:
        filer=utill_functions.csv_file("dnd.csv")
        characters=filer.get_as_character_dict()
        print("This is an RPG character manager!")
        while True:
            menu_choice=utill_functions.get_valid_type(int,"0 to quit\n1 to create character\n2 to inspect character\n3 to search for a character\n4 to compare two characters\n5 for help\n6 to remove character\nwhat do you want: ",valid=(0,6))
            match menu_choice:
                case 0:
                    
                    check=utill_functions.get_valid_type(str,"Are you sure you want to exit(y/n): ",valid=["y","n"])
                    if check=="y":
                        print("Goodbye!")
                        break
                    else:
                        continue
                case 1:
                    create_character(species_list,classes,characters)
                case 2:
                    character_inspect_menu(characters,species_list,classes)
                    pass
                case 3:
                    search_character(characters,classes)
                    pass
                case 4:
                    character_comparison(characters)
                case 5:
                    user_help()
                case 6:
                    if not(characters):
                        print("there are no characters")
                        break
                    names_list = list(characters.keys())
                    for num,name in enumerate(names_list):
                        char_class=characters[name].get("class","Unknown")
                        print(f"{num} for {name} ({char_class})")
                    remove_choice=utill_functions.get_valid_type(int,"Enter the number of the character to delete: ",valid=(0,len(names_list)-1))
                    target_name=names_list[remove_choice]
                    confirm=utill_functions.get_valid_type(str,f"Are you sure you want to delete {target_name}? (y/n): ",valid=["y","n"])
                    if confirm == "y":
                        del characters[target_name]
                        reinstate_csv(list(characters.values()), filer)
                    else:
                        break
    except KeyboardInterrupt:
        print("exit normally please")
if __name__=="__main__":
    main_menu()
                    
