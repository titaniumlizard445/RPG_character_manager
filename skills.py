#Isaac Covington CP2 Skill Management


import random


skills_list = {"Level 1-10":{ "Rouge Skills":{'Sneak Attack':"What do you think it is?", 'Parkour':"Do cool acrobratics acroos rooftops (while yelling 'Parkour!' of course)"},

"Wizard Skills":{'Fireball':"It's a ball of fire. Boom!", 'Wrong Spell':'You cast the wrong spell! Its basically just wild magic.'},

"Barbarian Skills":{'Rage':"Get angry and hit stuff harder!", 'Angry Bonk':"Get angry and hit stuff really really hard"},

"Bard Skills":{'Sick Lick': 'Not saliva, but a diss so strong it makes people cry. Magic sold seperately.', 'Distracting_solo': 'Really distracting music.'},

"Fighter Skills":{'Stab':"Just shank 'em, it works pretty well.", 'Tactical Yelling':"Yell so well it scared the enemies. Like a lot."},

"Cleric Skills":{'Judgy Heal':"Heal someone, but with a heavy sigh to ecompany the heal. Your party really is the dumbest.", 'Divine “I Told You So"':"Give someone a hefty bonus to an action you said they should do."}
},

"Level 11-20":{"Rouge Skills":{'Pocket Sand':"Need something to blind your enemies? Pocket sand works!", 'Not Yours To Take':"Grab any item that does not weigh more than you, and is not bolted down."},

"Wizard Skills":{'Mystical Firearm':"A gun, but it's magical.", 'Magic Tape':'This stuff can really fix anything!'},

"Barbarian Skills":{'Too Angry To Die':"Death is for wusses that are calm.", 'Optional Physics':"Physics? Pff, who needs that? Get there instantaneously."},

"Bard Skills":{'Power Chord': 'Hit a cord so hard that people are blown away. Literally', 'Platinum_Record':'Screw the haters. Slightly bend reality with just the power of music'},

"Fighter Skills":{'Parry This':"An unblockable attack that really confuses the enemy.", 'Panic Attack' : "Oh crap a monster! Just hit something repeatedly with no end until it's dead, or you come to your senses."},

"Cleric Skills":{"Holy Reverse":"Use the power of god to Uno Reverse Someone."}}, 

"General Skills":{"Persuasion":"You are able to convince people of your viewpoint better.","Athletics":"You have better endurance and physical capabilities than most others.","Animal Handling":"You work much better with animals than other people do.","Intimidation":"Scare the crap out of people, for the fun of it."}}

def skills_available(characters,character_name,skills_list,level): 
    
    available_skills = set()
    if characters[character_name]["Level"] < 10:
        match characters[character_name]["Class"]:
            case 'Fighter':
                for i in skills_list["Level 1-10"]["Fighter Skills"]:
                    available_skills.add(i)
            case 'Bard':
                for i in skills_list["Level 1-10"]["Bard Skills"]:
                    available_skills.add(i)
            case 'Wizard':
                for i in skills_list["Level 1-10"]["Wizard Skills"]:
                    available_skills.add(i)
            case 'Rogue':
                for i in skills_list["Level 1-10"]["Rogue Skills"]:
                    available_skills.add(i)
            case 'Barbarian':
                for i in skills_list["Level 1-10"]["Barbarian Skills"]:
                    available_skills.add(i)
            case 'Cleric':
                for i in skills_list["Level 1-10"]["Cleric Skills"]:
                    available_skills.add(i)
    else:
        match characters[character_name]["Class"]:
            case 'Fighter':
                for i in skills_list["Level 11-20"]["Fighter Skills"]:
                    available_skills.add(i)
            case 'Bard':
                for i in skills_list["Level 11-20"]["Bard Skills"]:
                    available_skills.add(i)
            case 'Wizard':
                for i in skills_list["Level 11-20"]["Wizard Skills"]:
                    available_skills.add(i)
            case 'Rogue':
                for i in skills_list["Level 11-20"]["Rogue Skills"]:
                    available_skills.add(i)
            case 'Barbarian':
                for i in skills_list["Level 11-20"]["Barbarian Skills"]:
                    available_skills.add(i)
            case 'Cleric':
                for i in skills_list["Level 11-20"]["Cleric Skills"]:
                    available_skills.add(i)
    for i in available_skills:
        print(i)
    return available_skills

def character_creation_skills(character_class,level,skills_list):
    available_skills = set()
    if level <= 10:
        match character_class:
            case 'Fighter':
                for i in skills_list["Level 1-10"]["Fighter Skills"]:
                    available_skills.add(i)
            case 'Bard':
                for i in skills_list["Level 1-10"]["Bard Skills"]:
                    available_skills.add(i)
            case 'Wizard':
                for i in skills_list["Level 1-10"]["Wizard Skills"]:
                    available_skills.add(i)
            case 'Rogue':
                for i in skills_list["Level 1-10"]["Rogue Skills"]:
                    available_skills.add(i)
            case 'Barbarian':
                for i in skills_list["Level 1-10"]["Barbarian Skills"]:
                    available_skills.add(i)
            case 'Cleric':
                for i in skills_list["Level 1-10"]["Cleric Skills"]:
                    available_skills.add(i)
    else:
        match character_class:
            case 'Fighter':
                for i in skills_list["Level 11-20"]["Fighter Skills"]:
                    available_skills.add(i)
            case 'Bard':
                for i in skills_list["Level 11-20"]["Bard Skills"]:
                    available_skills.add(i)
            case 'Wizard':
                for i in skills_list["Level 11-20"]["Wizard Skills"]:
                    available_skills.add(i)
            case 'Rogue':
                for i in skills_list["Level 11-20"]["Rogue Skills"]:
                    available_skills.add(i)
            case 'Barbarian':
                for i in skills_list["Level 11-20"]["Barbarian Skills"]:
                    available_skills.add(i)
            case 'Cleric':
                for i in skills_list["Level 11-20"]["Cleric Skills"]:
                    available_skills.add(i)
    for i in available_skills:
        print(i)
    return available_skills

def skill_choice(skills_list,available_skills,characters,character_name):
    print("Available Skills")
    print()
    for i in available_skills:
        print(i)
    while True:
        chosen_skill = input(f"Which skill do you want? Type the name of your chosen skill.\nEnter here: ").strip()
        if chosen_skill in available_skills:
            check = input(f"Are you sure you want to take {chosen_skill} as a skill? Y/N: ").strip().capitalize()
            if check == "Y":
                characters[character_name]["Skills"][available_skills] = (skills_list)# whatever we're gonna have for skill description
                break
            else:
                continue
        else:
            print("Invalid answer")
            continue
    return characters
