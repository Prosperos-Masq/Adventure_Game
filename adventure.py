start = input("Would you like to start a adventure!: ").strip()

while True:
    if start == "y" or "yes":
        print("Lets get started!")
        name = input("First.. what is your name young adventurer?: ")
        question1 = input("You, {} are a new adventurer... On a daring quest to brave your first dungeon. You are at the entrance of a dark and erie cave... The question is which way will you go forward or back (type forward or back)?: ".format(name))
        if question1 == "forward":
            question2 = input("You now find yourself in a dimly lit cavern with the sound of dripping water somewhere in the distance... to your left you see a hole big enough to fit through, to your right is a wall, forward leads further into the cave.. what will you do?: ")
    else:
        print("No adventure for you..")
        break