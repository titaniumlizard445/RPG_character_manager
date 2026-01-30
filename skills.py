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


def skills_available(level,character_class): 
    global ten_rouge_skills,ten_wizard_skills,ten_barbarian_skills,ten_bard_skills,ten_fighter_skills,ten_cleric_skills

    global twenty_rouge_skills,twenty_wizard_skills,twenty_barbarian_skills,twenty_bard_skills,twenty_fighter_skills,twenty_cleric_skills
    available_skills = set()
    if level < 10:
        character_class = str(character_class)
        match character_class:
            case 'Fighter':
                ten_fighter_skills = list(ten_fighter_skills)
                available_skills.add(ten_fighter_skills.split(","))
            case 'Bard':
                ten_bard_skills = list(ten_bard_skills)
                available_skills.add(ten_bard_skills.split(","))
            case 'Wizard':
                ten_wizard_skills = list(ten_wizard_skills)
                available_skills.add(ten_wizard_skills.split(","))
            case 'Rogue':
                ten_rouge_skills = list(ten_rouge_skills)
                available_skills.add(ten_rouge_skills.split(","))
            case 'Barbarian':
                ten_barbarian_skills = list(ten_barbarian_skills)
                available_skills.add(ten_barbarian_skills.split(","))
            case 'Cleric':
                ten_cleric_skills = list(ten_cleric_skills)
                available_skills.add(ten_cleric_skills.split(","))
    else:
        match character_class:
            case 'Fighter':
                twenty_fighter_skills = list(twenty_fighter_skills)
                available_skills.add(twenty_fighter_skills.split(","))
            case 'Bard':
                twenty_bard_skills = list(twenty_bard_skills)
                available_skills.add(twenty_bard_skills.split(","))
            case 'Wizard':
                twenty_wizard_skills = list(twenty_wizard_skills)
                available_skills.add(twenty_wizard_skills.split(","))
            case 'Rogue':
                twenty_rouge_skills = list(twenty_rouge_skills)
                available_skills.add(twenty_rouge_skills.split(","))
            case 'Barbarian':
                twenty_barbarian_skills = list(twenty_barbarian_skills)
                available_skills.add(twenty_barbarian_skills.split(","))
            case 'Cleric':
                twenty_cleric_skills = list(twenty_cleric_skills)
                available_skills.add(twenty_cleric_skills.split(","))

    for i in available_skills:
        print(i)
    return available_skills

def skill_choice(available_skills,characters,character_name,amount_of_skills):
    print("Available Skills")
    new_skills = {}
    for i in available_skills:
        print(i)
    for _ in range(amount_of_skills):
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
    return new_skills
