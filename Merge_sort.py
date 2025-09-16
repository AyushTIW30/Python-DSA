def merge_array(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    :param left: Sorted left array
    :param right: Sorted right array
    :return: Merged sorted array
    """
    i, j = 0, 0
    n, m = len(left), len(right)
    result = []
    
    # Merge elements from left and right in sorted order
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements from left (if any)
    while i < n:
        result.append(left[i])
        i += 1
    
    # Append remaining elements from right (if any)
    while j < m:
        result.append(right[j])
        j += 1
    
    return result


def Merge_sort(a):
    """
    Recursively sorts an array using Merge Sort algorithm.
    
    :param a: List of integers
    :return: Sorted list in ascending order
    """
    if len(a) <= 1:
        return a  # Base case: array of length 0 or 1 is already sorted
    
    mid = len(a) // 2
    left_arr = a[:mid]
    right_arr = a[mid:]
    
    # Recursively sort left and right halves
    left_arr = Merge_sort(left_arr)
    right_arr = Merge_sort(right_arr)
    
    # Merge sorted halves
    return merge_array(left_arr, right_arr)


# Driver code
if __name__ == "__main__":
    a = [6, 5, 4, 3, 2, 1]
    print("Original list:", [6, 5, 4, 3, 2, 1])
    print("Sorted list:  ", Merge_sort(a))
