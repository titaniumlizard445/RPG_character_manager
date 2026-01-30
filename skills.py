#Isaac Covington CP2 Skill Management


import random


ten_rouge_skills = {'Sneak Attack', 'Parkour'}

ten_wizard_skills = {'Fireball', 'Wrong Spell'}

ten_barbarian_skills = {'Rage', 'Angry Bonk'}

ten_bard_skills = {'Sick Lick', 'Distracting Solo'}

ten_fighter_skills = {'Stab', 'Tactical Yelling'}

ten_cleric_skills = {'Judgy Heal', 'Divine "I told you so"'}


twenty_rouge_skills = {'Pocket Sand', 'Not Yours to Take'}

twenty_wizard_skills = {'Mystical Firearm', 'Magic Tape'}

twenty_barbarian_skills = {'Too Angry to Die', 'Optional Physics'}

twenty_bard_skills = {'Power Chord', 'Platinum Record'}

twenty_fighter_skills = {'Parry This', 'Panic Attack'}

twenty_cleric_skills = {'Holy Uno Reverse'}


def skills_available(characters,character_name,level,character_class): 
    global ten_rouge_skills,ten_wizard_skills,ten_barbarian_skills,ten_bard_skills,ten_fighter_skills,ten_cleric_skills

    global twenty_rouge_skills,twenty_wizard_skills,twenty_barbarian_skills,twenty_bard_skills,twenty_fighter_skills,twenty_cleric_skills
    available_skills = set()
    if level < 10:
        match character_class:
            case 'Fighter':
                available_skills.add(list(ten_fighter_skills))
            case 'Bard':
                available_skills.add(list(ten_bard_skills))
            case 'Wizard':
                available_skills.add(list(ten_wizard_skills))
            case 'Rogue':
                available_skills.add(list(ten_rouge_skills))
            case 'Barbarian':
                available_skills.add(list(ten_barbarian_skills))
            case 'Cleric':
                available_skills.add(list(ten_cleric_skills))
    else:
        match character_class:
            case 'Fighter':
                available_skills.add(list(twenty_fighter_skills))
            case 'Bard':
                available_skills.add(list(twenty_bard_skills))
            case 'Wizard':
                available_skills.add(list(twenty_wizard_skills))
            case 'Rogue':
                available_skills.add(list(twenty_rouge_skills))
            case 'Barbarian':
                available_skills.add(list(twenty_barbarian_skills))
            case 'Cleric':
                available_skills.add(list(twenty_cleric_skills))

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

def skill_choice(available_skills,characters,character_name):
    print("Available Skills")
    for i in available_skills:
        print(i)
    while True:
        chosen_skill = input(f"Which skill do you want? Type the name of your chosen skill.\nEnter here: ").strip()
        if chosen_skill in available_skills:
            check = input(f"Are you sure you want to take {chosen_skill} as a skill? Y/N: ").strip().capitalize()
            if check == "Y":
                characters[character_name]["Skills"].add(chosen_skill)
                break
            else:
                continue
        else:
            print("Invalid answer")
            continue
    return
