#PS main file for character manager
from character_managment import create_character,characters
from UI_NOT_liam import character_comparison, search_character, user_help
from inspect_character import character_inspect_menu


species_list=['Human', 'Elf', 'Dwarf', 'Halfling', 'Dragonborn', 'Gnome', 'Tiefling', 'Aasimar', 'Goliath', 'Orc', 'Tabaxi', 'Warforged', 'Genasi', 'Lizardfolk', 'Changeling']
classes=['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
def main_menu():
    print("This is an RPG character manager!")
    while True:
        print("Main Menu\n1. Create Character\n2. Inspect Character\n3. Search for a Character\n4. Compare two characters\n5. Help\n6. Exit")
        menu_choice = input("What would you like to do? Enter number:\n").strip()
        match menu_choice:
            case "1":
                create_character(species_list,classes,characters)
            case "2":
                character_inspect_menu(characters,species_list,classes)
                pass
            case "3":
                search_character(characters)
                pass
            case "4":
                character_comparison(characters)
            case "5":
                user_help()
            case "6":
                check = input("Are you sure you want to exit? Your characters will not be saved. Y/N: ").strip().capitalize()
                if check == "Y":
                    
                    print("Goodbye!")
                    break
                else:
                    continue
if __name__=="__main__":
    main_menu()
                    
