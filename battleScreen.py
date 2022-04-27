def battle(adventurerHP, adventurerAC, adventurerDMG, adventurerBNS):
    from collections import namedtuple
    import random
    loot = 0

    # Monsters
    Monster = namedtuple('Monster', ['name', 'health', 'attack', 'armorClass'])

    troll = Monster("Troll", 10, 2, 10)
    skeleton = Monster("Skeleton", 15, 1, 5)
    kobold = Monster("Kobold", 5, 1, 10)

    # Determine monster at random
    random_monster = random.randint(1, 3)
    if random_monster == 1:
        monster = troll
    elif random_monster == 2:
        monster = skeleton
    else:
        monster = kobold

    print(f'A {monster.name} is attacking you.')
    print()

    # Battle Begin
    keep_going = True
    monster_health = monster.health
    while keep_going:
        adventurer_attack = random.randint(1, 20) + adventurerBNS
        if adventurer_attack >= monster.armorClass:
            print(f'You attack the {monster.name} and hit dealing '
                  f'{adventurerDMG} points of damage.')
            monster_health -= adventurerDMG
        else:
            print(f'You attack the {monster.name} but miss.')

        monster_attack = random.randint(1, 20) + monster.attack
        if monster_attack >= adventurerAC:
            print(f'The {monster.name} attacks and hits. It deals '
                  f'{monster.attack} point(s) of damage.')
            adventurerHP -= monster.attack
        else:
            print(f'The {monster.name} attacks but misses.')

        print(f'Your current HP is: {adventurerHP}')
        print(f'The {monster.name}\'s current HP is: {monster_health}')

        print()

        if adventurerHP <= 0:
            break
        elif monster_health <= 0:
            loot = random.randint(300, 1000)
            print(f'You defeated the {monster.name} and looted {loot} gold! '
                  f'Congratulations!')
            print()
            break
        else:
            print()
            keep_going_ask = input("You're both still alive. "
                                   "Keep attacking? Y/N: ")
            print()
            if keep_going_ask.lower() == 'y':
                keep_going = True
            else:
                keep_going = False

    return adventurerHP, loot
