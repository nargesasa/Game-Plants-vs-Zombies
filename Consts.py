import json

# Open the JSON file
with open("consts.json", "r") as file:
    # Load the JSON data
    salam = json.load(file)

# Access a value from the JSON data
# print(salam["mahdy"])

#scale
SCALE = 0.1

#sun value
SUN_VALUE = 25

# Plants
PEA_SHOOTER_DAMAGE = 5
SNOW_PEA_SHOOTER_DAMAGE = 8
SUN_FLOWER_DAMAGE = 0
SIB_ZAMINI_DAMAGE = 0

PEA_SHOOTER_HEALTH = 40
SNOW_PEA_SHOOTER_HEALTH = 30
SUN_FLOWER_HEALTH = 30
SIB_ZAMINI_HEALTH = 200

PEA_SHOOTER_COOL_DOWN = 5
SNOW_PEA_SHOOTER_COOL_DOWN = 9
SUN_FLOWER_COOL_DOWN = 10
SIB_ZAMINI_COOL_DOWN = 10

PEA_SHOOTER_HIT_RATE = 5
SNOW_PEA_SHOOTER_HIT_RATE = 5
SUN_FLOWER_HIT_RATE = 12
SIB_ZAMINI_HIT_RATE = 0

PEA_SHOOTER_SPEED = 7 * 2
SNOW_PEA_SHOOTER_SPEED = 5 * 2
SUN_FLOWER_SPEED = 0
SIB_ZAMINI_SPEED = 0

PEA_SHOOTER_PRICE = 4 * SUN_VALUE
SNOW_PEA_SHOOTER_PRICE = 6 * SUN_VALUE
SUN_FLOWER_PRICE = 2 * SUN_VALUE
SIB_ZAMINI_PRICE = 2 * SUN_VALUE



# Zombies
REGULAR_ZOMBIE_DAMAGE = 10
GIANT_ZOMBIE_DAMAGE = 20

REGULAR_ZOMBIE_HEALTH = 50
GIANT_ZOMBIE_HEALTH = 80

REGULAR_ZOMBIE_HIT_RATE = 1
GIANT_ZOMBIE_HIT_RATE = 1.2

REGULAR_ZOMBIE_SPEED = 7 * SCALE
GIANT_ZOMBIE_SPEED = 5 * SCALE



# OtherItems
SUN_SPEED = 10 * SCALE
SUN_INTERVAL = 10 * 0.2




# dict row -> y_pos
DICT_ROW_Y_POS = {
    0: 155,
    1: 265,
    2: 375,
    3: 485,
    4: 595
}

# dict row -> y_pos
DICT_Y_POS_ROW = {
    155: 0,
    265: 1,
    375: 2,
    485: 3,
    595: 4
}

# game time (sc)
GAME_TIME_IN_SEC = 300



# distance before zombie starting to eat plant
DISTANCE_ZOMBIE_PLANT_EAT = 20

# 
DISTANCE_BULLET_ZOMBIE_HIT = 5
