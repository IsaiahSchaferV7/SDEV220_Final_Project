secret = 4
guess = int(input())

if guess > 10:
    print("Invalid. Try again")
elif guess > secret:
    print("Too High")
elif guess < secret:
    print("Too Low")
elif guess == secret:
    print("Just Right")