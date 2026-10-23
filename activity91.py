# ---------- PART 1: the loop and the guess ----------
print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

secret = 27
max_attempts = 5
count = 0
guess = 0

while count < max_attempts and guess != secret:
    guess = int(input("Your guess: "))
    count += 1

    # ---------- PART 2: win or not ----------
    if guess == secret:
        print("You win!")
    else:
        # ---------- PART 3: distance and hint ----------
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("Ice cold")
        elif diff >= 10:
            print("Cold")
        elif diff >= 5:
            print("Warm")
        else:
            print("Hot")

        # ---------- PART 4: lives left ----------
        remaining = max_attempts - count

        if remaining > 0:
            for i in range(remaining):
                print("❤️", end=" ")
            print()

# ---------- GAME OVER (after the loop) ----------
if guess != secret:
    print("Game over")
    print("The secret number was:", secret)

