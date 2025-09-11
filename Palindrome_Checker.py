# palindrome_checker.py

def is_palindrome(number: int) -> bool:
    """
    Function to check if the given number is a palindrome.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if number is palindrome, False otherwise.
    """
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original == reversed_number


def main():
    num = int(input("Enter a number to check palindrome: "))
    if is_palindrome(num):
        print(f"{num} is a Palindrome ✅")
    else:
        print(f"{num} is NOT a Palindrome ❌")


if __name__ == "__main__":
    main()
