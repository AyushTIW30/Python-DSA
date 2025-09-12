"""
Frequency Counter
-----------------
This script demonstrates two approaches to count element frequencies in a list:
1. Using dict.get() method
2. Using collections.Counter (recommended)

"""

from collections import Counter


def count_frequencies_with_get(arr):
    """
    Count frequencies using dict.get() method.

    Args:
        arr (list): Input list of numbers or strings.

    Returns:
        dict: Dictionary with elements as keys and their frequencies as values.
    """
    freq_count = dict()
    for i in range(len(arr)):
        freq_count[arr[i]] = freq_count.get(arr[i], 0) + 1
    return freq_count


def count_frequencies_with_counter(arr):
    """
    Count frequencies using collections.Counter.

    Args:
        arr (list): Input list of numbers or strings.

    Returns:
        dict: Dictionary with elements as keys and their frequencies as values.
    """
    return dict(Counter(arr))


def main():
    # Input list
    a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 6, 9, 10, 2, 7, 3]

    # Approach 1: Using dict.get()
    freq_get = count_frequencies_with_get(a)
    print("Approach 1 - Frequencies (using dict.get()):")
    for key, value in freq_get.items():
        print(f"Element {key}: {value} times")

    # Approach 2: Using collections.Counter
    freq_counter = count_frequencies_with_counter(a)
    print("\nApproach 2 - Frequencies (using collections.Counter):")
    for key, value in freq_counter.items():
        print(f"Element {key}: {value} times")


if __name__ == "__main__":
    main()
