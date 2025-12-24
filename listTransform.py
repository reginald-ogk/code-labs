def square_even_numbers(numbers: list[int]) -> list[int]:
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n * 2)

    return result


def main() -> None:
    raw = input("Enter a list of numbers separated by spaces: ")
    parts = raw.split(",")

    numbers = []
    for p in parts:
        p = p.strip()
        if p.startswith("-"):
            valid = p[1:].isdigit()
        else:
            valid = p.isdigit()

        if not valid:
            print(f"'{p}' is an invalid number. Skipped.")
            continue

        numbers.append(int(p))

    squares = square_even_numbers(numbers)

    print("The doubled even numbers are:", squares)
    print("The original numbers are:", numbers)

if __name__ == "__main__":
    main()