print("Small Calculator")
print("""
Menu Options
1. Sum.
2. Weight Converter.
3. Guess Game.
4. Quit.
""")
command=""
while command != 4:
    command=int(input("Opción:"))
    if command == 1:
        print("__"*20)
        print("You are in the space to sum two numbers")
        a=int(input("First number: "))
        b=int(input("Second number: "))
        total=a+b
        print(f"The result is {total}.")
        print("__" * 20)
    elif command == 2:
        print("__"*20)
        print("You can convert your weight")
        weight = int(input("Your Weight: "))
        tip = input("Write if this is in (l)bs or (K)g:")
        if tip == "l":
            a=weight*0.45
            print(f"The weight is {a} Kg.")
        elif tip == "k":
            a=weight/0.45
            print(f"The weight is {a} lbs")
        else:
            print("Try again and write l or k")
        print("__" * 20)
    elif command == 3:
        print("__" * 20)
        print("GUESS GAME")
        print("You have to guess a number between 1 and 10")
        secret_number = 5
        counter = 0
        limit_counter = 3
        while counter < limit_counter:
            guess = int(input("Type your guess:"))
            counter = counter + 1
            if guess == secret_number:
                print("You Won!!")
                print("__" * 20)
                break
        else:
            print("You lost")
            print("__" * 20)
    elif command == 4:
        print("__" * 20)
        print("Good by")
        break
    else:
        print("It's not an option, try again")

