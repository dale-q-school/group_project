def addsub(attrib_name, starting_attrib, attrib, pool):
    assign = input("Do you want to add or subtract? ")
    if assign.lower() == "add":
        try:
            num = int(input("How many points would you like to add? "))
            if num > pool:
                print(f'Sorry. You only have {pool} point(s) to spend.')
                print()
            else:
                attrib += num
                pool -= num
                print()
                print(f"Your {attrib_name} is now:", attrib)
                print("Points left to spend:", pool)
                print()
        except ValueError:
            print("Invalid Entry. Please use numbers only")
    elif assign.lower() == "subtract":
        try:
            num = int(input("How many points would you like to subtract? "))
            if (attrib - num) < starting_attrib:
                print()
                print("You can't lower an attribute below it's starting value.")
                print()
            else:
                attrib -= num
                pool += num
                print()
                print(f"Your {attrib_name} is now:", attrib)
                print("Points left to spend:", pool)
                print()
        except ValueError:
            print("Invalid Entry. Please use numbers only")
    return attrib, pool
