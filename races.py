def raceselection(adventurer_name):
    from collections import namedtuple
    name = adventurer_name
    Race = namedtuple('Race', ['name', 'attributeBonus', 'bonus'])

    elf = Race('Elf', 'Dexterity', 2)
    dwarf = Race('Dwarf', 'Strength', 2)
    human = Race('Human', 'Wisdom', 2)

    print("This world has 3 races.")
    print()
    print(f'{elf.name}: Attribute Bonus: +{elf.bonus} {elf.attributeBonus}')
    print(
        f'{dwarf.name}: Attribute Bonus: +{dwarf.bonus} {dwarf.attributeBonus}')
    print(
        f'{human.name}: Attribute Bonus: +{human.bonus} {human.attributeBonus}')
    print()
    race_choice = input("Which race are you? ")

    while race_choice.lower() != 'elf' and race_choice.lower() != 'dwarf' and \
            race_choice.lower() != 'human':
        print(
            "That race doesn't seem to exist in this world yet. Please choose "
            "Elf, Dwarf, or Human")
        race_choice = input("What is your race? ")

    if race_choice.lower() == 'elf':
        adventurer_race = elf
    elif race_choice.lower() == 'dwarf':
        adventurer_race = dwarf
    else:
        adventurer_race = human

    print()
    if adventurer_race.name == elf.name:
        print(
            f'Okay {name}, looks like you are an {adventurer_race.name}')
        print()
    else:
        print(
            f'Okay {name}, looks like you are a {adventurer_race.name}')
        print()

    return adventurer_race.name, adventurer_race.bonus
