#Isaac Covington CP2 Skill Management

#import level up
import random
from character_managment_functions import level_up()
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

skills = {"Level 1-10":{ "Rouge Skills":{'Sneak Attack':"What do you think it is?", 'Parkour':"Do cool acrobratics acroos rooftops (while yelling 'Parkour!' of course)"},

"Wizard Skills":{'Fireball':"It's a ball of fire. Boom!", 'Wrong Spell':'You cast the wrong spell! Its basically just wild magic.'},

"Barbarian Skills":{'Rage':"Get angry and hit stuff harder!", 'Angry Bonk':"Get angry and hit stuff really really hard"},

"Bard Skills":{'Sick Lick': 'Not saliva, but a diss so strong it makes people cry. Magic sold seperately.', 'Distracting_solo': 'Really distracting music.'},

"Fighter Skills":{'Stab':"Just shank 'em, it works pretty well.", 'Tactical Yelling':"Yell so well it scared the enemies. Like a lot."},

"Cleric Skills":{'Judgy Heal':"Heal someone, but with a heavy sigh to ecompany the heal. Your party really is the dumbest.", 'Divine “I Told You So"':"Give someone a hefty bonus to an action you said they should do."}
},

"Level 11-20":{"Rouge Skills":{'Pocket Sand':"Need something to blind your enemies? Pocket sand works!", 'Not Yours To Take':"I'm not even sure what this skill does."},

"Wizard Skills":{'Mystical Firearm':"A gun, but it's magical.", 'Magic Tape':'This stuff can really fix anything!'},

"Barbarian Skills":{'Too Angry To Die':"Death is for wusses that are calm.", 'Optional Physics':"Physics? Pff, who needs that? Get there instantaneously."},

"Bard Skills":{'Power Chord': 'Hit a cord so hard that people are blown away. Literally', 'Platinum_Record':'Screw the haters. Slightly bend reality with just the power of music'},

"Fighter Skills":{'Parry This':"An unblockable attack that really confuses the enemy.", 'Panic Attack' : "Oh crap a monster! Just hit something repeatedly with no end until it's dead, or you come to your senses."},

"Cleric Skills":{"Holy Reverse":"Use the power of god to Uno Reverse Someone."}}}


def skills_available(skills,characters,character_name, level, skills_list): 
    
    available_skills = set()
    if characters[character_name][level] <= 10:
        match characters[character_name]['class']:
            case 'Fighter':
                available_skills.append(skills[level_10_below["Fighter Skills"]])
            case 'Bard':
                available_skills.append(skills[level_10_below["Bard Skills"]])
            case 'Wizard':
                available_skills.append(skills[level_10_below["Wizard Skills"]])
            case 'Rogue':
                available_skills.append(skills[level_10_below["Rouge Skills"]])
            case 'Barbarian':
                available_skills.append(skills[level_10_below["Barbarian Skills"]])
    return available_skills

def skill_choice(skills,available_skills,characters,character_name):
    print("Available Skills")
    for i in available_skills:
        print(i)
    while True:
        chosen_skill = input(f"Which skill do you want? Type the name of your chosen skill.").strip()
        if chosen_skill in available_skills:
            check = input(f"Are you sure you want to take {chosen_skill} as a skill? Y/N").strip().capitalize()
            if check == "Y":
                characters[character_name]["Skills"][available_skills] = (skills)# whatever we're gonna have for skill description
                break
            else:
                continue
        else:
            print("Invalid answer")
            continue

