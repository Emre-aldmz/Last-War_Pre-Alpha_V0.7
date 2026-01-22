import random
number = random.randint(1,100)
x = int(input("Enter number for start game (1-100): "))
i = 1

while (x != number):
    x = int(input("Try again! : "))
    i+=1

    if x > number:
        print("down please!")
    elif x < number:
        print("up please!")

    if number - 2 < x < number + 2 and x != number:
        print("OMG so close!")

    elif number - 5 < x < number + 5 and x != number:
        print("so close!")

print(f"yes you find the secret number!! '{x}' tryied '{i}' times")

