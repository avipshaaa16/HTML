import random

# pick a secret number between 1 and 50
secret = random.randint(1, 50)

attempts = 5
i = 1

while i <= attempts:
    guess = int(input("Enter your guess (1-50): "))

    if guess == secret:
        print("Correct! You win!")
    else:
        diff = abs(secret - guess)
        if diff > 20:
            print("Ice cold!")
        elif diff > 10:
            print("Cold!")
        elif diff > 5:
            print("Warm!")
        else:
            print("Hot!")

        # remaining lives as hearts
        hearts = "<3 " * (attempts - i)
        print("Lives left:", hearts)

    i += 1

if i > attempts and guess != secret:
    print("You lost! The secret number was", secret)
