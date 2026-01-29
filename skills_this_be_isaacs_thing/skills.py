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
    },
    #magic missile = requirements, damage, and roll
    #fireball = requirements, damage, roll

    #fighter skills = {Extra strike, Heavy Strike}
    fighter_skills = {
        'extra strike' : {'damage' : 'whatever weapon in use',
                        'class requirements' : 'fighter'
        },
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
rogue_skills = {'sneak_attack', 'parkour', 'pocket_sand', 'not_yours_to_take'}
wizard_skills = {''}
barbarian_skills = {'rage', 'too_angry_to_die', 'angry_bonk', 'physics_is_optional'}
bard_skills = {'sick_lick','distracting_solo','power_chord', 'platinum_record'}
fighter_skills = {'stab', 'parry_this', 'tactical_yelling', 'stop_moving'}

skills_list = [level_one = [rogue_skills = [], wizard_skills = [], bard_skills = [], fighter_skills = []]]
def skills_available(skills_list,characters,character_name, level,):
    available_skills = []
    if characters[character_name][level] < 10:
        match characters[character_name]['Class']:
            case 'Fighter':
                available_skills.append(skills_list[level_10_below[fighter_skills]])
            case 'Bard':
                available_skills.append(skills_list[level_10_below[bard_skills]])
            case 'Wizard':
                available_skills.append(skills_list[level_10_below[wizard_skills]])
            case 'Rogue':
                available_skills.append(skills_list[level_10_below[rogue_skills]])
    return available_skills

def skill_choice():
    chosen_skill = input(f"Which skill do you want? Type the name of your chosen skill.{available_skills}").strip()
    