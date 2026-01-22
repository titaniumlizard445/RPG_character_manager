# CB 1st Character Manager Pseudocode
# characters = ({"Name":"Example", "Class":"Example", "Level":1, "Stats":{"Stat1":Example Num}, "Skills":{"Skill_name":"Skill_desc"}, "Inventory":{"Item_name":"Item_desc"}})

# skills_list = []

# classes_list = []

# define function create_character():
    # new_character = {}
    # stats_dictionary = {"Strength":10,"Dexterity":10,"Consititution":10,"Wisdom":10,"Intelligence":10,"Charisma":10} (Note: These are just placeholders)
    # skills_dictionary = {}
    # while True:
        # ask user for character name
        # save character name in a variable
        # have user choose race (human, elf, dwarf, gnome)
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
        # ask user to choose class (display list of avaiable classes based off of attributes)
        # ask user if this choice is okay (display class choice)
        # if yes:
            # break
        # if no:
            # continue
    # while True:
        # ask user to choose skills (combat, support, misc) avaiable skills are based off of attributes
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
