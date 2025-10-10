import random

MIN = 1
MAX = 20
number = random.randint(MIN, MAX)

print(number)

print(f"Pick a number between {MIN} and {MAX}")

guess = input ("> ")

print(guess)