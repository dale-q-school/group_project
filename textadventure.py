import addorsubtract
import professions
import races
from battleScreen import *
from clearscreen import *


def textadventure():
    import random
    from collections import namedtuple
    from time import sleep

    # Splash Screen
    print(
        """
                            _|_|_|      _|_|    _|        _|_|_|_|  _|   _|_|_|
                            _|    _|  _|    _|  _|        _|           _|      
                            _|    _|  _|_|_|_|  _|        _|_|_|         _|_|  
                            _|    _|  _|    _|  _|        _|                 _|
                            _|_|_|    _|    _|  _|_|_|_|  _|_|_|_|     _|_|_|  
        
        
                                _|_|_|_|_|  _|_|_|_|  _|      _|  _|_|_|_|_|
                                    _|      _|          _|  _|        _|    
                                    _|      _|_|_|        _|          _|    
                                    _|      _|          _|  _|        _|    
                                    _|      _|_|_|_|  _|      _|      _|    
        
        
          _|_|    _|_|_|    _|      _|  _|_|_|_|  _|      _|  _|_|_|_|_|  _|    _|  _|_|_|    _|_|_|_|
        _|    _|  _|    _|  _|      _|  _|        _|_|    _|      _|      _|    _|  _|    _|  _|      
        _|_|_|_|  _|    _|  _|      _|  _|_|_|    _|  _|  _|      _|      _|    _|  _|_|_|    _|_|_|  
        _|    _|  _|    _|    _|  _|    _|        _|    _|_|      _|      _|    _|  _|    _|  _|      
        _|    _|  _|_|_|        _|      _|_|_|_|  _|      _|      _|        _|_|    _|    _|  _|_|_|_|  
        """
    )
    sleep(3)
    clear()

    # Meet and greet the adventurer
    print("Welcome Adventurer! You are about to embark on your very own "
          "journey. You will likely face many perils "
          "along the way, but should you live, the riches shall be plenty.")
    print()
    adventurer_name = input("Every adventure begins the same...with a name. "
                            "What is yours? ")
    print()
    print("Greetings " + adventurer_name + "!")

    # Character Creation
    # Races
    player_race, bonus = races.raceselection(adventurer_name)

    # Professions
    player_profession, armor_class = professions.professionselection(
        adventurer_name)

    # Random Starting Attributes and Gear
    start_strength = random.randint(5, 10)
    start_health = random.randint(5, 10)
    start_wisdom = random.randint(5, 10)
    start_dexterity = random.randint(5, 10)
    strength = start_strength
    health = start_health
    wisdom = start_wisdom
    dexterity = start_dexterity
    attrib_bonus = 0
    point_pool = 10
    total_loot = 0
    finish = 'yes'

    print(f'These are your starting attributes which have been randomized and '
          f'does not include your racial bonus:\n\n'
          f'Dexterity: {dexterity}\n'
          f'Strength: {strength}\n'
          f'Wisdom: {wisdom}\n'
          f'Health: {health}')
    print()

    # Spend points
    print(f'You may now spend {point_pool} points and add them to your current '
          f'attributes. Spend them wisely.')
    print()
    while point_pool >= 0:
        if point_pool == 0 and finish == 'yes':
            print("You have spent all your points.")
            finish = input("Would you like to finish and start you adventure? "
                           "Type Yes or No: ")
            if finish.lower() == 'yes':
                print()
                break
            elif finish.lower() == 'no':
                print()
                continue
        finish = 'yes'
        attrib = input("Which attribute would you like to work with? ")
        if attrib.lower() == "strength":
            strength, point_pool = addorsubtract.addsub("strength",
                                                        start_strength,
                                                        strength, point_pool)
        elif attrib.lower() == "health":
            health, point_pool = addorsubtract.addsub("health", start_health,
                                                      health, point_pool)
        elif attrib.lower() == "wisdom":
            wisdom, point_pool = addorsubtract.addsub("wisdom", start_wisdom,
                                                      wisdom, point_pool)
        elif attrib.lower() == "dexterity":
            dexterity, point_pool = addorsubtract.addsub("dexterity",
                                                         start_dexterity,
                                                         dexterity, point_pool)

    # Add Racial Bonus
    if player_race.lower() == 'elf':
        dexterity += bonus
    elif player_race.lower() == 'dwarf':
        strength += bonus
    elif player_race.lower() == 'human':
        wisdom += bonus

    # Compare Race to Profession to Apply Damage Bonus
    if player_race.lower() == 'elf' and player_profession.lower() == 'thief':
        attrib_bonus = 2
    elif player_race.lower() == 'dwarf' and \
            player_profession.lower() == 'warrior':
        attrib_bonus = 2
    elif player_race.lower() == 'human' and \
            player_profession.lower() == 'wizard':
        attrib_bonus = 2

    clear()

    # Player Character Information
    Character = namedtuple('Character', ['name', 'race', 'profession',
                                         'strength', 'wisdom', 'attribBonus',
                                         'dexterity', 'health', 'armorClass',
                                         'baseDamage'])

    adventurer = Character(adventurer_name, player_race, player_profession,
                           strength, wisdom, attrib_bonus, dexterity, health,
                           armor_class, 2)

    print(f'Alright {adventurer.name}, these are your final stats:')
    if adventurer.race.lower() == 'elf':
        print(f'You are an {adventurer.race} who has chosen the '
              f'{adventurer.profession} profession and you have the following '
              f'attributes.')
    else:
        print(f'You are a {adventurer.race} who has chosen the '
              f'{adventurer.profession} profession and you have the following '
              f'attributes.')
    print()
    print(f'Dexterity: {adventurer.dexterity}\n'
          f'Strength: {adventurer.strength}\n'
          f'Wisdom: {adventurer.wisdom}\n'
          f'Health: {adventurer.health}')
    print()
    input("Press Enter to start you adventure!")
    clear()

    # Adventure Begins
    print("You're adventure begins with a battle!! Prepare yourself!")
    health, loot = battle(adventurer.health, adventurer.armorClass,
                    adventurer.baseDamage, adventurer.attribBonus)
    total_loot += loot

    adventurer = Character(adventurer_name, player_race, player_profession,
                           strength, wisdom, attrib_bonus, dexterity, health,
                           armor_class, 2)
    keep_playing = input("Would you like to continue your adventure? "
                         "Y/N:")
    print()

    while keep_playing.lower() == 'y':
        if adventurer.health <= 0:
            print("It looks like you're adventure was cut short. Better luck "
                  "next time")
            break
        else:
            health, loot = battle(adventurer.health, adventurer.armorClass,
                                  adventurer.baseDamage, adventurer.attribBonus)
            total_loot += loot

            adventurer = Character(adventurer_name, player_race,
                                   player_profession, strength, wisdom,
                                   attrib_bonus, dexterity, health, armor_class,
                                   2)
            keep_playing = input("Would you like to continue your adventure? "
                                 "Y/N:")
            print()

        if adventurer.health > 0:
            print(f'You managed to obtain a wealth of {total_loot} gold on this'
                  f' adventure.')
            print()

    input("Thank you for playing! Press Enter to return to the main menu.")

    clear()


































































