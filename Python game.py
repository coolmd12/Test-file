x=input("What is your name? ")
print("Welcome to Python!")
d=input("Do you want to go east, with the dangerous dragon? Or west, through the scorching desert? ")
if d=="west":
    d=input("You have got everything you need to survive for a week. Yes or no, shall we travel to the oceans to find some treasure? ")
    if d=="yes":
        print("All right! Let's dive in! Oh no! You cut your arm on a sharp piece of coral and you are attacked by a shark!")
        d=input("Do you want to leave the treasure and escape, option A? Or defend yourself with a knife and keep the treasure...if you survive, option B? ")
        if d=="option A":
            print("No problem! You escaped from the shark, but sadly, your treasure is lost forever. But don't worry, there is always more oppurtunities!")
        else:
            print("Smart move! You put up a good fight. Jabbing at the shark's weak spots, you have defeated it! You got some treasure, and now it's time to go home!")
    else:
        print("Okay! It's your decision! Now, it's time to walk all the way back to the city. You have some water, a little food, and a wilderness knife. Good luck!")
        d=input("Whoops! You've run into a deadly rattlesnake! Hiss! Do you want to fight it and get treasure that is in its burrow, option A? Or run away with nothing, option B? ")
        if d=="option A":
            print("Ok! You chose to fight! Hiss! Smack! You are very lucky! The snake slithered away, and you can quickly take the treasure.")
            print("Since you have gathered a good amount of money, let's quickly head back to the city to home sweet home!")
        elif d=="option B":
            print("No problem! You saved your life, at the cost of treasure...but that's okay. At least you are alive!")
            print("Oh wow! A survival squad is here to pick you up! Unfortunately, that was your last chance to earn some money. Time to head back home I guess!")
if d=="east":
    print("Okay! You have chosen the Bravery Dragon Path. You have two items. A knife, and a flamethrower.")
    d=input("Now you have a choice. Fight the dragon, and get jewels and diamonds: option A. Or, you can wait until the dragon is asleep, and sneak away, option B. ")
    if d=="option A":
        print("Oh god! This is a deadly fight! Sadly you lost, but we have to go on.")
        d=input("Another checkpoint. Ninjas up ahead! Do you think you want to fight them and take their valuables, option A? Or leave them alone, option B?")
        if d=="option A":
            print("What a battle! With your superb survival skills, you used the splintered knife against them and won! Woo hoo! Money for you!")
            print("You made great choices throughout the game, and now it's time to go home!")
        else:
            print("Oh well! Unfortunately, that was the last time for you to get money. Time to go home!")