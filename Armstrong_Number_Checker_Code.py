def is_armstrong(number: int) -> bool:
    """
    Function to check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its digits
    raised to the power of the number of digits.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if number is Armstrong, False otherwise.
    """
    original = number
    nod = len(str(number))  # Number of digits
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** nod
        number = number // 10

    return total == original


def main():
    num = int(input("Enter a number to check if it is Armstrong: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is NOT an Armstrong Number")


if __name__ == "__main__":
    main()
