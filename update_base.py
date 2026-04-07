
import utill_functions

from faker import Faker

import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
class data_visualisation:
    def __init__(self):
        self.figuer,self.axis=plt.subplots()
    def radar_graph(self,catigorys,vals,radius=30,definition=10):
        x_points=[]
        y_points=[]
        shape=RegularPolygon((0,0),numVertices=len(catigorys),radius=radius,facecolor="none",edgecolor="black",linewidth=1)
        self.axis.add_patch(shape)
        angles=360/len(catigorys)
        for x in range(len(catigorys)):
            angle_rad=math.radians(angles * x+90)
            target=[radius*math.cos(angle_rad),(radius*math.sin(angle_rad))]
            plt.plot([0,target[0]],[0,target[1]])
            lx=(radius * 1.1) * math.cos(angle_rad)
            ly=(radius * 1.1) * math.sin(angle_rad)
            self.axis.text(lx,ly,catigorys[x],ha="center",va="center",fontsize=10)
            vx=vals[x] * math.cos(angle_rad)
            vy=vals[x] * math.sin(angle_rad) 
            x_points.append(vx)
            y_points.append(vy)
        x_points.append(x_points[0])
        y_points.append(y_points[0])
        self.axis.plot(x_points,y_points,color="blue",linewidth=2)
        self.axis.fill(x_points,y_points,color="blue",alpha=0.3)
        for x in range(definition):
            shape=RegularPolygon((0,0),numVertices=len(catigorys),radius=x*(radius/definition),facecolor="none",edgecolor="black",linewidth=.5)
            self.axis.add_patch(shape)
        self.axis.text(0,-45,"Close this window to continue",ha="center",va="center",fontsize=12,fontweight="bold",color="red")
        self.axis.set_xlim(-40,40)
        self.axis.set_ylim(-40,40)
        self.axis.set_aspect("equal") # Keeps it from being squashed
        self.axis.axis("off")
        plt.show(block=False)
class RandomGenerator:
    def __init__(self):
        self.race_flavor_descriptions={
            "Human": ["a wide-eyed scholar seeking forbidden knowledge in ancient ruins.","a battle-hardened mercenary who has seen too many wars.","a charismatic noble trying to restore their family's fallen name.","a street-smart urchin who knows every alleyway in the capital.","a weary traveler looking for a place to finally call home."],
            "Elf": ["a graceful archer who moves through the forest like a ghost.","an ancient high-mage whose memories span several human lifetimes.","a rebellious wood elf who prefers the wild to the gilded halls.","a melancholic artist seeking to capture the beauty of the stars.","a stern sentinel guarding the borders of a hidden sylvan kingdom."],
            "Dwarf": ["a soot-covered blacksmith with a hammer and a grudge.","a traditionalist warrior who can recite their entire genealogy.","a greedy prospector looking for the 'motherlode' in the deep dark.","a jovial brewer who believes every problem can be solved with ale.","a stoic mountain guard who hasn,t seen the sun in decades."],
            "Halfling": ["a lucky thief who manages to stumble into treasure by accident.","a brave community leader defending their village with a sling.","a curious cook traveling the world for the perfect spice.","a quiet gardener who was forced into adventure by a wizard.","a nimble acrobat performing in a traveling circus."],
            "Dragonborn": ["a proud knight who puts the honor of their clan above all else.","a draconic zealot seeking to awaken the power of their ancestors.","a mercenary captain whose breath smells of smoke and sulfur.","a wandering hermit looking for the meaning of a draconic prophecy.","a disciplined monk who channels their inner dragon into combat."],
            "Gnome": ["an eccentric tinkerer whose pockets are full of exploding gadgets.","a forest-dwelling illusionist who communicates with small animals.","a gem-cutter who claims they can hear the music of the earth.","a frantic researcher who hasn,t slept in three days.","a cheerful prankster who uses magic to lighten the mood."],
            "Tiefling": ["a cynical investigator working the grime-covered city streets.","a soft-spoken poet trying to prove they aren't their ancestry.","a flamboyant warlock who embraces their infernal heritage.","a suspicious outcast who trusts no one but their blade.","a desperate seeker looking for a way to break a family curse."],
            "Aasimar": ["a luminous warrior guided by the whispers of a celestial deva.","a fallen angel seeking redemption through acts of great mercy.","a quiet healer whose touch brings a warmth like the sun.","a stern judge who enforces divine law with a flaming sword.","an orphan who discovered their heritage through a terrifying vision."],
            "Goliath": ["a competitive athlete who views every challenge as a contest.","a lone hunter who survived a winter on the highest peaks.","a massive brawler who values strength and honesty above all.","a tribe-less wanderer looking for a new group to protect.","a spiritual guide who speaks to the spirits of the wind and stone."],
            "Orc": ["a scarred veteran who values the bond of the war-band.","a powerful shaman who channels the primal rage of the wilds.","a wandering smith looking for the strongest metal in the world.","a defiant survivor who escaped a life of endless raiding.","a quiet protector of a small,integrated frontier village."],
            "Tabaxi": ["a hyper-active scout obsessed with shiny trinkets and stories.","a silent hunter who stalks prey across the desert dunes.","a curious lore-gatherer who won't leave until every book is read.","a fickle performer who changes their stage name every week.","a nimble rogue who treats every heist like a game of cat and mouse."],
            "Warforged": ["a rusted soldier still following orders from a war that ended years ago.","a peaceful gardener trying to understand the concept of 'growth'.","a mechanical bodyguard who takes their 'protection' duty literally.","an experimental unit looking for the soul it believes it has.","a heavy-plated juggernaut who acts as a literal shield for their party."],
            "Genasi": ["an airy dreamer whose hair literally floats in the breeze.","a hot-headed pyromancer who leaves scorched footprints.","a solid,dependable earth-dweller with skin like cracked stone.","a fluid and adaptable traveler with a deep love for the sea.","an elemental hybrid struggling to balance two opposing natures."],
            "Lizardfolk": ["a literal-minded survivalist who views friends as 'useful assets'.","a swamp-shaman who uses bones and teeth to cast spells.","a cold-blooded warrior who feels no fear and no pity.","a curious outlander trying to understand why mammals cry.","a pragmatic hunter who never lets any part of a kill go to waste."],
            "Changeling": ["a cautious spy who has lived ten different lives in ten different cities.","a lost soul who has forgotten what their 'true' face looks like.","a playful actor who uses their gift for the ultimate performance.","a master of disguise working for the highest-paying guild.","a shape-shifter seeking a place where they can be their real self."]
        }
        self.dnd_origins=["the City of Splendors (Waterdeep)","the Jewel of the North (Neverwinter)","the Underdark (Menzoberranzan)","the High Forest","the Spine of the World","the Sea of Fallen Stars","the Feywild (Plane of Faerie)","the Shadowfell (Plane of Shadow)","the Elemental Plane of Fire","the Astral Sea","a Secluded Monastery in the Cloud Peaks","a Nomadic tribe in the Shaar","the Clockwork Realm of Mechanus","a Floating Citadel in the Plane of Air","the Iron City of Dis (Nine Hells)"]
        self.dnd_stats=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
        self.classes=["Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
        self.dnd_races=["Human","Elf","Dwarf","Halfling","Dragonborn","Gnome","Tiefling","Aasimar","Goliath","Orc","Tabaxi","Warforged","Genasi","Lizardfolk","Changeling"]
        self.dnd_names={
            "Human": ["Hama","Kosef","Morn","Adran","Ander","Blath","Bran","Frath","Geth","Lander","Luth","Malark","Morn","Nosew","Pavel","Randal","Stedd","Tama","Urth","Aseir","Bardeid","Haseid","Khemed","Mehmen","Sudeiman","Zasheir","Darvin","Dorn","Evendur","Gorstag"],
            "Elf": ["Aramil","Arjhan","Berrian","Carric","Enialis","Erdan","Erevan","Galinndan","Hadarai","Heian","Himo","Immeral","Ivellios","Laucian","Mindartis","Paelias","Peren","Quarion","Riardon","Rolen","Soveliss","Thamior","Tharivol","Theren","Varis","Adrie","Althaea","Anastrianna","Andraste","Antinua"],
            "Dwarf": ["Adrik","Alberich","Baern","Barendd","Brottor","Bruenor","Dain","Darrak","Delg","Eberk","Einkil","Fargrim","Flint","Gardain","Harbek","Kildrak","Morgran","Orsik","Oskar","Rangrim","Rurik","Thoradin","Thorin","Tordek","Traubon","Travok","Ulfgar","Veit","Vondal","Gloin"],
            "Halfling": ["Alton","Ander","Cade","Corrin","Eldon","Errich","Finnan","Garret","Lindal","Lyle","Merric","Milo","Osborn","Perrin","Reed","Roscoe","Wellby","Andry","Bree","Callie","Cora","Euphemia","Jillian","Kithri","Lavinia","Lidda","Merla","Nedda","Paela","Portia"],
            "Dragonborn": ["Arjhan","Balasar","Bharash","Donaar","Ghesh","Heskan","Kriv","Medrash","Mehen","Nadarr","Pandjed","Patrin","Rhogar","Shamash","Shedinn","Tarhun","Torinn","Akra","Biri","Daar","Farideh","Harann","Havilar","Jheri","Kava","Korinn","Mishann","Nala","Perra","Raiann"],
            "Gnome": ["Alston","Alvyn","Boddynock","Brocc","Burgell","Dimble","Eldon","Erky","Fonkin","Frug","Gerbo","Gimble","Glim","Jebeddo","Kellen","Namfoodle","Orryn","Roondar","Seebo","Sindri","Warryn","Wrenn","Zook","Bimpnottin","Breena","Caramip","Carlin","Donella","Duvamil","Ella"],
            "Tiefling": ["Akmenos","Amnon","Barakas","Damakos","Ekemon","Iados","Kairon","Leucis","Melech","Mordai","Morthos","Pelaios","Skamos","Therai","Art","Carrion","Chant","Creed","Despair","Excellence","Fear","Glory","Hope","Ideal","Music","Nowhere","Open","Poetry","Quest","Random"],
            "Aasimar": ["Arithel","Hestia","Valerius","Aedar","Bariel","Casiel","Daphiel","Exequiel","Fenriel","Gabriel","Hadariel","Imriel","Jariel","Kael","Lariel","Muriel","Nariel","Oriel","Pariel","Quariel","Raziel","Sariel","Tariel","Uriel","Variel","Xariel","Yariel","Zariel","Amon","Balthazar"],
            "Goliath": ["Gauthak","Thuliaga","Vaklov","Aukan","Ehalu","Gae-Al","Kalas","Keothi","Kuori","Lo-Kag","Maveith","Nalla","Orilo","Paavu","Pethani","Thalav","Thutam","Uthal","Vaunea","Vigdis","Anakal","Bearkiller","Dawncaller","Fearless","Flintfinder","Horncarver","Keeneye","Lonehunter","Longleaper","Skywatcher"],
            "Orc": ["Dench","Grell","Krusk","Feng","Gell","Henk","Holg","Imsh","Krutu","Lort","Mhurren","Ront","Shump","Thokk","Urg","Baggi","Emen","Engong","Kansif","Myev","Neega","Ovak","Ownka","Shautha","Sutha","Vola","Volen","Yursh","Zarg","Zod"],
            "Tabaxi": ["Cloud on Mount","River of Stars","Skitter","Adroit Shadow","Bright Flower","Call of the Wild","Distant Rain","Eldritch Eye","Five Echoes","Garden of Thorns","Hidden Path","Ice on the Lake","Jumping Frog","Kindle of Sparks","Left-Handed Hummingbird","Morning Mist","Night Sky","Odd Gift","Path of the Moon","Quick Fox","Rain in the Sun","Seven Snakes","Thunder of Hooves","Under the Leaves","Vibrant Wing","Walking Breeze","X-Ray Vision","Yellow Moon","Zephyr Breeze","Stalking Cat"],
            "Warforged": ["Bastion","Halt","Sledge","Anvil","Banner","Blade","Bulwark","Cask","Clinch","Colossus","Crucible","Dagger","Echo","Fathom","Glaive","Hammer","Iron","Juggernaut","Keeper","Lance","Mace","Nexus","Obsidian","Pillar","Quarry","Rivet","Sentry","Tower","Unit","Vault"],
            "Genasi": ["Ember","Gale","Onyx","Aqua","Ash","Blaze","Breeze","Cinder","Cliff","Coal","Current","Dew","Dust","Flint","Flood","Frost","Gully","Gust","Heat","Mist","Mud","Puddle","Pyre","Quartz","Rain","River","Rock","Scorch","Shale","Silt"],
            "Lizardfolk": ["Achuak","Garurt","Irhtos","Baeshra","Darastrix","Ghesh","Isk","Jharym","Kriv","Lim","Mim","Noch","Oth","Patrin","Rhogar","Shedinn","Tir","Usk","Valignat","Vrix","Vutha","Vyth","Xer","Yoth","Zik","Zis","Zit","Zof","Zon","Zov"],
            "Changeling": ["Bin","Cas","Doppel","Ael","Bryn","Cis","Dax","Eil","Fay","Glyn","Hix","Iri","Jax","Kael","Lux","Mox","Nix","Ori","Pax","Quin","Rix","Sox","Trix","Ur","Vex","Wox","Xax","Yix","Zix","Chance","Mask"]
        }
    def random_character(self):
        race=self.dnd_races[random.randint(1,len(self.dnd_races)-1)]
        name=self.dnd_names[race][random.randint(1,len(self.dnd_names[race])-1)]
        descrip=self.race_flavor_descriptions[race][random.randint(0,len(self.race_flavor_descriptions[race])-1)]
        oregen=self.dnd_origins[random.randint(1,len(self.dnd_origins)-1)]
        classs=self.classes[random.randint(1,len(self.classes)-1)]
        level=random.randint(1,20)
        stats={"Strength":random.randint(1,30),"Dexterity":random.randint(1,30),"Constitution":random.randint(1,30),"Wisdom":random.randint(1,30),"Intelligence":random.randint(1,30),"Charisma":random.randint(1,30)}
        return {"name":name,"race":race,"level":level,"stats":stats,"description":descrip,"origin":oregen,"class":classs,"story":f"{name},a level {level} {race} {classs} who is {descrip} from {oregen}"}

# --- TEST EXECUTION ---
if __name__ == "__main__":

    
    # Instance 1: High Strength "Goliath"
    goliath_stats = [28, 12, 25, 10, 12, 8] 
    vis1 = data_visualisation()
    vis1.axis.set_title("Goliath Warrior")
    vis1.radar_graph(dnd_stats, goliath_stats)

    # Instance 2: High Intelligence "Elf"
    elf_stats = [8, 20, 12, 28, 15, 18]
    vis2 = data_visualisation()
    vis2.axis.set_title("Elf Mage")
    vis2.radar_graph(dnd_stats, elf_stats)

    # This opens both windows at the same time
    print("Displaying 2 radar charts. Close windows to finish.")
    plt.show()