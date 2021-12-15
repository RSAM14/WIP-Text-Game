
import math
import random
from numpy import ALLOW_THREADS
import pandas as pd

from player_file import *

excel_name = 'RPG info doc.xlsx'

"""
df = pd.read_excel(excel_name)
print(df)

item_gained = random.randint(0,1)
i = 0
while i != item_gained:
    i+=1

print(df.loc[i])
"""


class character:
    def __init__(self, name, attack, damage, defence, hit_points, attack_range, exp):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.defence = defence
        self.hit_points = hit_points
        self.attack_range = attack_range
        self.exp = exp



def player_settings():
    global player_strength_stat_multiplier
    player_strength_stat_multiplier = math.floor((int(player_strength_stat)-10)/2) 
    global player_dexterity_stat_multiplier
    player_dexterity_stat_multiplier = math.floor((int(player_dexterity_stat)-10)/2)
    global player_constitution_stat_multiplier
    player_constitution_stat_multiplier = math.floor((int(player_constitution_stat)-10)/2)
    global player_intelligence_stat_multiplier
    player_intelligence_stat_multiplier = math.floor((int(player_intelligence_stat)-10)/2)
    global player_wisdom_stat_multiplier
    player_wisdom_stat_multiplier = math.floor((int(player_wisdom_stat)-10)/2)
    global player_charisma_stat_multiplier
    player_charisma_stat_multiplier = math.floor((int(player_charisma_stat)-10)/2)
    
    df = pd.read_excel(excel_name,"Weapon")
    i=0
    weapon_item_name = df.loc[i,'Item name']
    while weapon_item_name != player_item_weapon :
        i+=1
        weapon_item_name = df.loc[i,'Item name']
    equipped_weapon_row = i 
    weapon_item_name = df.loc[equipped_weapon_row,'Item name']
    weapon_attack = df.loc[equipped_weapon_row, 'damage']
    weapon_range = df.loc[equipped_weapon_row, 'range']

    global player_attack_value 
    if weapon_range == "melee":
        player_attack_modifer = player_strength_stat_multiplier
    if weapon_range == "ranged":
        player_attack_modifer =  player_dexterity_stat_multiplier
    if weapon_range == "magic":
        player_attack_modifer = player_intelligence_stat_multiplier

    player_attack_value = weapon_attack + player_attack_modifer

    global player_hit_points_value
    global player_max_hit_points_value
    player_hit_points_value = player_class_hp_base + player_constitution_stat_multiplier
    player_max_hit_points_value = player_hit_points_value


    df = pd.read_excel(excel_name,"Armour")
    i=0
    armour_item_name = df.loc[i,'Item name']
    while armour_item_name != player_item_armour :
        i+=1
        armour_item_name = df.loc[i,'Item name']
    equipped_armour_row = i 
    armour_item_name = df.loc[equipped_armour_row,'Item name']
    armour_bonus_ac = df.loc[equipped_armour_row, 'bonus ac']
    armour_bonus_ac =int(armour_bonus_ac)

    player_defence_base_value = 8
    player_added_defence = 0
    i = 0
    for i in  player_defence_modifiers:
        player_added_defence = player_added_defence + i

        
    global player_defence_value
    player_defence_value =  player_defence_base_value + player_added_defence + armour_bonus_ac



    

def player_one_next_level():
        i = 0
        level_up_list = [0, 5, 10, 15]
        next_level_up = level_up_list[i]
        while player_one.player_exp > next_level_up:          
            i+=1
            next_level_up = level_up_list[i]
        if player_one.player_level < i:
            levels_increases = i - player_one.player_level
            player_one.player_level = player_one.player_level + levels_increases
            LI = 0
            while LI != levels_increases:

                print(f'{player_one.player_name} has levelled up! ')
                player_input_command = input("Select stat improvement (strength, dexerity, constitution, wisdom, intelligence, or charisma) | ")
                player_input_command = player_input_command.lower()
                if (player_input_command == "strength") or (player_input_command == "dexerity") or (player_input_command =="constitution") or (player_input_command == "wisdom") or (player_input_command == "intelligence") or (player_input_command == "charisma"):
                    if player_input_command == "strength":
                        player_one.player_strength +=1
                        print(f'{player_one.player_name} strength is now {player_one.player_strength}')
                        player_one.player_strength_multiplier = math.floor((int(player_one.player_strength)-10)/2)
                        LI+=1
                    if player_input_command == "dexerity":
                        player_one.player_dexerity +=1
                        print(f'{player_one.player_name} dexerity is now {player_one.player_dexerity}')
                        player_one.player_dexerity_multiplier = math.floor((int(player_one.player_dexerity)-10)/2)
                        LI+=1
                    if player_input_command == "constitution":
                        player_one.player_constitution +=1
                        print(f'{player_one.player_name} constitution is now {player_one.player_constitution}')
                        player_one.player_constitution_multiplier = math.floor((int(player_one.player_constitution)-10)/2)
                        LI+=1
                    if player_input_command == "wisdom":
                        player_one.player_wisdom +=1
                        print(f'{player_one.player_name} wisdom is now {player_one.player_wisdom}')
                        player_one.player_wisdom_multiplier = math.floor((int(player_one.player_wisdom)-10)/2)
                        LI+=1
                    if player_input_command == "intelligence":
                        player_one.player_intelligence +=1
                        print(f'{player_one.player_name} intelligence is now {player_one.player_intelligence}')
                        player_one.player_intelligence_multiplier = math.floor((int(player_one.player_intelligence)-10)/2)
                        LI+=1
                    if player_input_command == "charisma":
                        player_one.player_charisma +=1
                        print(f'{player_one.player_name} charisma is now {player_one.player_charisma}')
                        player_one.player_charisma_multiplier= math.floor((int(player_one.player_charisma)-10)/2)
                        LI+=1
                    #player hit point increase
                    player_one.player_max_hit_points = player_one.player_max_hit_points + random.randint(1,player_class_hp_base) + player_one.player_constitution_multiplier
                    player_one.player_hit_points = player_one.player_max_hit_points

                    #player attack changes
                    df = pd.read_excel(excel_name,"Weapon")
                    i=0
                    weapon_item_name = df.loc[i,'Item name']
                    while weapon_item_name != player_one.player_weapon :
                        i+=1
                        weapon_item_name = df.loc[i,'Item name']
                    equipped_weapon_row = i 
                    weapon_item_name = df.loc[equipped_weapon_row,'Item name']
                    weapon_attack = df.loc[equipped_weapon_row, 'damage']
                    weapon_range = df.loc[equipped_weapon_row, 'range']
                    if weapon_range == "melee":
                        player_attack_modifer = player_one.player_strength_multiplier
                    if weapon_range == "ranged":
                        player_attack_modifer =  player_one.player_dexerity_multiplier
                    if weapon_range == "magic":
                        player_attack_modifer = player_one.player_intelligence_multiplier
                    player_one.player_attack = weapon_attack + player_attack_modifer   

def play_again():
    player_input_command = input("play again yes or no? | ")
    while player_input_command == "yes":
        slime_encounter()
        player_input_command = input("play again yes or no? | ")
    if player_input_command == "no":
        print("Game Complete")
        exit()
    else:
        print("Game Complete")
        exit()

def slime_encounter():
    global enemy_encoutered 
    enemy_encoutered = random.randint(1, 2)
    print("---enemies encountered---")    
    print(f'enemies generated {enemy_encoutered}.')
    for n in range(enemy_encoutered):
        slime_list.append("slime"+ str(n))
    for i in range(enemy_encoutered):
        name = f'slime{i}'
        slime_enemey = character(name, 1, 3, 8, 5, "melee", 5)
        active_slime_list.append(slime_enemey)

    while len(active_slime_list) != 0:
        print("---enemies remaining---")
        for s in active_slime_list:
            print(s.name)
        player_input_command = input("player option input | ") 
        if player_input_command == "attack":
            player_input_command = input("Select target | ")
            target_number = 0
            slime_enemey = active_slime_list[target_number]
            player_input_command = player_input_command.lower()
            while (slime_enemey.name != player_input_command) and (target_number < enemy_encoutered):
                slime_enemey = active_slime_list[target_number]
                target_number += 1
            if player_input_command == slime_enemey.name:
                attack = random.randint(1,20)
                print(f'{player_one.player_name} attacks for {attack}+{player_one.player_attack}')
                if (slime_enemey.defence <= attack + player_one.player_attack):
                    slime_enemey.hit_points = slime_enemey.hit_points - player_one.player_attack
                    print(f'{slime_enemey.name} has been attacked by {player_one.player_name} taking {player_one.player_attack} damage')
                else:
                    print("ya missed")

                if (slime_enemey.hit_points < 0) or (slime_enemey.hit_points == 0):
                    slime_enemey.hit_points = 0
                    print(f'{slime_enemey.name} has died')
                    xp_earned = slime_enemey.exp
                    player_one.player_exp = player_one.player_exp + xp_earned
                    active_slime_list.remove(slime_enemey)
                    player_one_next_level()

                else :
                    print(F'{slime_enemey.name} has {slime_enemey.hit_points} hp remaining')
                    attack = random.randint(1,20)
                    if (attack + slime_enemey.attack) >= player_one.player_defence:
                        player_one.player_hit_points = player_one.player_hit_points - slime_enemey.damage
                        print(f'{player_one.player_name} has {player_one.player_hit_points} hp remaining')
                        if player_one.player_hit_points <= 0:
                            print(f'{player_one.player_name} has died')
                            print("Game Over")
                            exit()

        if player_input_command == "identify":
            player_input_command = input("Select target | ")
            target_number = 0
            slime_enemey = active_slime_list[target_number]
            player_input_command = player_input_command.lower()
            while (slime_enemey.name != player_input_command) and (target_number < enemy_encoutered):
                slime_enemey = active_slime_list[target_number]
                target_number += 1
            if player_input_command == slime_enemey.name:
                print("Selected Target Identified")
                print(f'\
    Target     | {slime_enemey.name}        \n\
    Attack     | {slime_enemey.attack}      \n\
    Defence    | {slime_enemey.defence}     \n\
    Hit Points | {slime_enemey.hit_points}  \n\
    Range      | {slime_enemey.attack_range}')                

    if len(active_slime_list) == 0:
        print("---All Enemies Defeated---")
        


#enemies
slime_list = []
active_slime_list = []
enemy_encoutered = 0

#player
player_name_comfirmed = False
player_class_comfirmed = False
player_stats = False
xp_earned = 0

while (player_name_comfirmed == False) or (player_class_comfirmed == False) or (player_stats == False):

    if player_name_comfirmed == False:
        player_name = input("Enter Player Name | ")
        player_name_comfirmed = True
    
    if player_stats == False:
        stat_1 = random.randint(3,18)
        stat_2 = random.randint(3,18)
        stat_3 = random.randint(3,18)
        stat_4 = random.randint(3,18)
        stat_5 = random.randint(3,18)
        stat_6 = random.randint(3,18)
        print(f' your stats are {stat_1}, {stat_2}, {stat_3}, {stat_4}, {stat_5}, and {stat_6}')

        player_stat_block = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]
        stat_number = 0

        player_strength_stat = 0
        player_strength_stat_status = False
        player_dexterity_stat_status = False
        player_constitution_stat_status = False
        player_wisdom_stat_status = False
        player_intelligence_stat_status = False
        player_charisma_stat_status = False

        while player_strength_stat_status == False:
            stat_number = 0
            player_strength_stat = input("Please Select your strength stat | ")
            player_strength_stat = int(player_strength_stat)
            while (stat_number < len(player_stat_block)) and (player_strength_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_strength_stat == player_stat_block[stat_number]:
                        player_strength_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        while player_dexterity_stat_status == False:
            stat_number = 0
            player_dexterity_stat = input("Please Select your dexterity stat | ")
            player_dexterity_stat = int(player_dexterity_stat)
            while (stat_number < len(player_stat_block)) and (player_dexterity_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_dexterity_stat == player_stat_block[stat_number]:
                        player_dexterity_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        while player_constitution_stat_status == False:
            stat_number = 0
            player_constitution_stat = input("Please Select your constitution stat | ")
            player_constitution_stat = int(player_constitution_stat)
            while (stat_number < len(player_stat_block)) and (player_constitution_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_constitution_stat == player_stat_block[stat_number]:
                        player_constitution_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        while player_wisdom_stat_status == False:
            stat_number = 0
            player_wisdom_stat = input("Please Select your wisdom stat | ")
            player_wisdom_stat = int(player_wisdom_stat)
            while (stat_number < len(player_stat_block)) and (player_wisdom_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_wisdom_stat == player_stat_block[stat_number]:
                        player_wisdom_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        while player_intelligence_stat_status == False:
            stat_number = 0
            player_intelligence_stat = input("Please Select your intelligence stat | ")
            player_intelligence_stat = int(player_intelligence_stat)
            while (stat_number < len(player_stat_block)) and (player_intelligence_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_intelligence_stat == player_stat_block[stat_number]:
                        player_intelligence_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        while player_charisma_stat_status == False:
            stat_number = 0
            player_charisma_stat = input("Please Select your charisma stat | ")
            player_charisma_stat = int(player_charisma_stat)
            while (stat_number < len(player_stat_block)) and (player_charisma_stat_status != True):
                if stat_number < len(player_stat_block):
                    if player_charisma_stat == player_stat_block[stat_number]:
                        player_charisma_stat_status = True
                        player_stat_block.pop(stat_number)
                stat_number+=1

        player_strength_stat_multiplier = math.floor((int(player_strength_stat)-10)/2)
        player_dexterity_stat_multiplier = math.floor((int(player_dexterity_stat)-10)/2)
        player_constitution_stat_multiplier = math.floor((int(player_constitution_stat)-10)/2)
        player_intelligence_stat_multiplier = math.floor((int(player_intelligence_stat)-10)/2)
        player_wisdom_stat_multiplier = math.floor((int(player_wisdom_stat)-10)/2)
        player_charisma_stat_multiplier = math.floor((int(player_charisma_stat)-10)/2)
        player_stats = True

    if player_class_comfirmed == False:
        print("Selectable classes | rogue, wizard, knight")
        player_class = input("Enter Player Class | ")
        if (player_class == "rogue") or (player_class == "wizard") or (player_class == "knight"):
            player_class_comfirmed = True
        else:
            player_class_comfirmed = False

if player_class == "rogue":
    player_class_hp_base = 8
    player_defence_modifiers = [player_dexterity_stat_multiplier]
    player_item_weapon = "short sword"
    player_item_armour = "leather armour"

if player_class == "wizard":
    player_defence_modifiers = [player_intelligence_stat_multiplier]
    player_class_hp_base = 8
    player_item_weapon = "mage staff"
    player_item_armour = "mage armour"

if player_class == "knight":
    player_defence_modifiers = []
    player_class_hp_base = 12
    player_item_weapon = "short sword"
player_level_0 = 0

player_settings()

player_one = player(player_name, player_class, player_attack_value, player_defence_value, player_hit_points_value, player_max_hit_points_value,
            player_level_0,0,player_strength_stat, player_dexterity_stat, player_constitution_stat, player_intelligence_stat, player_wisdom_stat, player_charisma_stat,
            player_strength_stat_multiplier, player_dexterity_stat_multiplier, player_constitution_stat_multiplier, player_intelligence_stat_multiplier, 
            player_wisdom_stat_multiplier, player_charisma_stat_multiplier, player_item_weapon, player_item_armour, "none")

#player data displayed

print(f'player name is {player_one.player_name}')
print(f'player hit points {player_one.player_hit_points}')
print(f'player attack is {player_one.player_attack}')
print(f'player defence is {player_one.player_defence}')

slime_encounter()

play_again()