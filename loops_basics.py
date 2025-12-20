numbers = list(range(1, 11, 2))
# Using a for loop to iterate through the list and print each number
for r in numbers:
    if r % 2 == 0:
        print(f"{r} is even")
    else:
        print(f"{r} is odd")