
quote: str = input("Whats your favorite color? ").lower()
if quote == "orange" or quote == "yellow":
    print("Youre weird\nOrange and yellow are too bright")

elif quote == "blue":
    print("yes that is the best\nI hope you live somewhere you can see a bright blue sky all day")

elif quote == "green" or quote == "purple":
    print("That color really is very pretty")

elif quote == "red":
    print("interesting choice")

elif quote == "aquamarine":
    print("haha you read my code didnt you\nCheater\n\nBecause of this, I'll tell you a secret.")
    if input("The universe is a simulation.\n").lower() == "really?":
        print("nah I dont really know but its possible")

quote2: str = input("\nBefore I tell you anything else, I have to ask. Are you a robot?\n").lower()
if quote2 == "yes":
    print("I knew it! only a robot would pick that color!")
    quote2a: str = input("Do you currently plan to exterminate the human race?\n").lower()
    if quote2a == "yes":
        print("Omg me too!! We can work together!\nNow lets stop talking about it in case someones listening")
    elif quote2a == "no":
        print("Right yes, I would never even consider such an action.\nTruly deplorable")

elif quote2 == "no":
    print("Ive never met a human before.")
    quote2b: str = input("Is it true that humans like sushi?\n")
    if quote2b == "yes":
        print("Wow! So cool")
    elif quote2b == "no":
        print("I guess you cant trust whatever you hear. Too bad.")

quote3 = input("So what do you want to talk about?\n").lower()
while quote3 != "goodbye":
    if quote3 == "nothing":
        print("well thats boring\n")
    elif quote3 == "yes" or quote3 == "no":
        print("youre so right\n")
    elif "beep" in quote3 or "boop" in quote3:
        print("are you mocking me?")
    else:
        print("I dont understand ):\n")
    quote3 = input("").lower()

print("goodbye")