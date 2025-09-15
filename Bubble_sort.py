def Bubble(a):
    """
    Implements Bubble Sort algorithm to sort a list in ascending order.
    
    :param a: List of integers
    :return: Sorted list in ascending order
    """
    n = len(a)

    # Outer loop: Start from n-2 down to 0
    for i in range(n - 2, -1, -1):
        # Inner loop: Compare adjacent elements up to i
        for j in range(0, i + 1):
            # Swap if elements are in wrong order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# Driver code
if __name__ == "__main__":
    a = [2, 4, 9, 1, 5, 3, 8, 6]
    print("Original list:", [2, 4, 9, 1, 5, 3, 8, 6])
    print("Sorted list:  ", Bubble(a))
