place = input("Choose a place: (forest or cave?) ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
if place == "cave":
    action2 = input("light a torch or proceed in the dark")
    if action2 == "light a torch":
        print("you are a coward")
    elif action2 == "proceed in the dark":
        print("you are a brave")
    print("You find a hidden treasure!")
else:
    pass