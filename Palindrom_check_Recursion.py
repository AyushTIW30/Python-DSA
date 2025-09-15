# palindrome_checker.py

def palin(s, l, r):
    """
    Recursive function to check if string s is a palindrome.
    
    :param s: Input string
    :param l: Left pointer (starting from 0)
    :param r: Right pointer (starting from len(s)-1)
    :return: True if palindrome, False otherwise
    """
    # Base case: If left pointer crosses right, all characters matched
    if l > r:
        return True

    # If mismatch found, return False immediately
    if s[l] != s[r]:
        return False

    # Recursive call moving towards the center
    return palin(s, l + 1, r - 1)


# Driver code to test the function
if __name__ == "__main__":
    # Example 1: Non-palindrome string
    s1 = "niti"
    print(f"Is '{s1}' a palindrome? → {palin(s1, 0, len(s1)-1)}")  
    # Output: False

    # Example 2: Palindrome string
    s2 = "nitin"
    print(f"Is '{s2}' a palindrome? → {palin(s2, 0, len(s2)-1)}")  
    # Output: True
