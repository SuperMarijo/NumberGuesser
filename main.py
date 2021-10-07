while True:

    secret = 7

    guess = int(input("What's your guess? "))

    if guess == secret:
        print("Incredible, that's correct!")
        break
    elif guess == 42:
        print("This is the answer to the ultimate question of life, the universe, and everything, "
              "however it's not our answer. But let's give it another shot.")
    elif guess == 666:
        print("The number of the beast!!! But not the number we were looking for. Try guessing again but way lower "
              "this time.")
    elif guess >= secret:
        print("Sorry but that's too high. Try something lower?")
    elif guess <= secret:
        print("Too low, you should aim higher than that. So what is it?")
