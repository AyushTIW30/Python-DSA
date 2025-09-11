from math import log10, floor # Or just use "*" instead

def extract_digits(n):
    """Extract digits of an integer and return as a list."""
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits

def count_digits_log(v):
    """Count number of digits using logarithm."""
    if v == 0:
        return 1  # Special case: log10(0) is undefined
    return int(log10(abs(v)) + 1)

def count_digits_floor_log(v):
    """Count digits using floor and log10."""
    if v == 0:
        return 1
    return floor(log10(abs(v))) + 1

def count_digits_str(v):
    """Count number of digits by converting to string."""
    return len(str(abs(v)))

def count_digits_simple(v):
    """Another simple string-based digit count."""
    return len(str(abs(v)))

# Example usage
if __name__ == "__main__":
    n = 2345456
    v = 234556

    digits_list = extract_digits(n)
    digit_count_log = count_digits_log(v)
    digit_count_floor_log = count_digits_floor_log(v)
    digit_count_str = count_digits_str(v)
    digit_count_simple = count_digits_simple(v)

    print("Extracted Digits:", digits_list)
    print("Digit Count (log10 method):", digit_count_log)
    print("Digit Count (floor + log10 method):", digit_count_floor_log)
    print("Digit Count (string method):", digit_count_str)
    print("Digit Count (simple method):", digit_count_simple)



