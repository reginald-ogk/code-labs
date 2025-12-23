def classify_number(n: int) -> str:
    """Classify a number as 'positive', 'negative', or 'zero'.

    Args:
        n (int): The number to classify.
    Returns:
        str: The classification of the number ('positive', 'negative', or 'zero').
    """
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
    
def main() -> None:
    """Main function to demonstrate classify_number function."""
    raw = input("Enter an integer: ").strip()

    if raw.startswith("-"):
        is_valid = raw[1:].isdigit()
    else:
        is_valid = raw.isdigit()

    if not is_valid:
        print("Invalid input.")
        return
        
    n = int(raw)
    result = classify_number(n)
    print(f"{n} is {result}")

if __name__ == "__main__":
    main()

def is_even(n: int) -> bool:
        """Check if a number is even.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is even, False otherwise.
        """
        return n % 2 == 0
    
if __name__ == "__main__":
    main()