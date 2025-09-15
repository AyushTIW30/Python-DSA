def Selection(a):
    """
    Implements Selection Sort algorithm to sort a list in ascending order.
    
    :param a: List of integers
    :return: Sorted list in ascending order
    """
    n = len(a)

    # Traverse the list
    for i in range(n):
        # Assume the current index i is the minimum
        min_ind = i

        # Find the index of the minimum element in the remaining unsorted part
        for j in range(i, n):
            if a[j] < a[min_ind]:
                min_ind = j

        # Swap the found minimum element with the element at index i
        a[i], a[min_ind] = a[min_ind], a[i]

    return a

if __name__ == "__main__":
    a = [2, 4, 9, 1, 5, 3, 8, 6]
    print("Original list:", [2, 4, 9, 1, 5, 3, 8, 6])
    print("Sorted list:  ", Selection(a))
