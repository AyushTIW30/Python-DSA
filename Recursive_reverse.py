def reverse(arr, l, r):
    if l > r:
        return arr
    
    # Swap elements at positions l and r
    arr[l], arr[r] = arr[r], arr[l]
    
    # Recursive call, moving towards center
    return reverse(arr, l + 1, r - 1)

# Input list
arr = [1, 2, 3, 4, 5, 6, 7]

# We want to reverse from index 2 to 5 (0-based index)
l = 2
r = 5

# Calling the function and printing result
print(reverse(arr, l, r))

