#Isaac Covington CP2 Skill Management

#import level up
import random
#def skill requirements:
def skill_requirements():
    #wizard skills = {Magic Missile, Fireball}
    wizard_skills = {
        'magic missile' : {'projectiles':3,
                        'damage': '1d4' +1,
                        'class requirements' : 'Wizard'
        },
        'fireball' : {'damage': '8d6',
                      'class requirements' : 'wizard',
        }
    }
    #magic missile = requirements, damage, and roll
    #fireball = requirements, damage, roll

    #fighter skills = {Extra strike, Heavy Strike}
    fighter_skills = {
        'extra strike' : {'damage' : 'whatever weapon in use',
                          'class requirements' : 'fighter'
        }
    }
    #extra strike = requirements, damage, roll
    #etc for every other skill :)

    #bard skills = {Inspire, Theme Song}
    #rogue skills = {Sneak, Assassinate}
    #strength skills = {boulder lift, Hercules}
    #dexterity skills = {acrobatics}
    #constitution skills = {sickness resistance}
    #intelligence skills = {puzzle solver}
    #wisdom skills = {foresight}
    #charisma skills = {negotiate}#compare player attributes to stat requirements
    #get all skills, and
    #if certain attributes >= requirements
    #repeat for every requirement, and keep the ones that pass
    #For each skill, insert numbers at index 0 in order to show which skills can be used
    #show all skills that player can use
    #ask user which ones they want, and ask them to type the number of the skill they want.
    #if they are all done, ask are you sure? if they respond with yes, add the stats if no, call skill requirements
    #load in user, ask user: what stats do you want?
    #check by using skill requirements
    #add stat that is picked to user stats.
    #attributes altered to accommodate for user skills.

    


