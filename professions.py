def professionselection(adventurer_name):
    from collections import namedtuple
    name = adventurer_name
    Profession = namedtuple('Profession', ['name', 'mainAttribute',
                                           'armorClass'])

    thief = Profession('Thief', 'Dexterity', 12)
    warrior = Profession('Warrior', 'Strength', 15)
    wizard = Profession('Wizard', 'Wisdom', 10)

    print("This world has 3 professions.")
    print()
    print(f'{thief.name}: Main Attribute: {thief.mainAttribute}, '
          f'Armor Class: {thief.armorClass}')
    print(
        f'{warrior.name}: Main Attribute: {warrior.mainAttribute}, '
        f'Armor Class: {warrior.armorClass}')
    print(
        f'{wizard.name}: Main Attribute: {wizard.mainAttribute}, '
        f'Armor Class: {wizard.armorClass}')
    print()
    profession_choice = input("Which profession will you choose? ")

    while profession_choice.lower() != 'thief' and profession_choice.lower() \
            != 'warrior' and profession_choice.lower() != 'wizard':
        print(
            "That profession doesn't seem to exist in this world yet. "
            "Please choose Thief, Warrior, or Wizard")
        profession_choice = input("Which profession will you choose? ")

    if profession_choice.lower() == 'thief':
        adventurer_profession = thief
    elif profession_choice.lower() == 'warrior':
        adventurer_profession = warrior
    else:
        adventurer_profession = wizard

    print()
    print(f'Okay {name}, you have chosen to be a {adventurer_profession.name}.')
    print()

    return adventurer_profession.name, adventurer_profession.armorClass
