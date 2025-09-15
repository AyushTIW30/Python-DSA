def insertion(a):
    """
    Implements Insertion Sort algorithm to sort a list in ascending order.
    
    :param a: List of integers
    :return: Sorted list in ascending order
    """
    n = len(a)
    
    # Start from second element (index 1)
    for i in range(1, n):
        key = a[i]      # The element to be inserted at correct place
        j = i - 1
        
        # Move elements greater than key to one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        
        # Insert key at the correct position
        a[j + 1] = key
    
    return a


# Driver code
if __name__ == "__main__":
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Original list:", [9, 8, 7, 6, 5, 4, 3, 2, 1])
    print("Sorted list:  ", insertion(a))
