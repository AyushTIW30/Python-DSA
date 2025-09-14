# element_frequency_counter.py

# Approach 1: Using collections.Counter (Recommended way)
from collections import Counter

print("=== Approach 1: Using Counter ===")

n = [1, 2, 3, 7, 8, 9, 1, 2, 3, 2, 1, 4, 2, 1, 5, 3, 1, 54]
m = [1, 4, 7, 10, 9, 33]

# Frequency count using Counter
hash_map = Counter(n)

# Print frequencies of elements in m
for i in m:
    print(f"{i} = {hash_map[i]}")

print("\n=== Approach 2: Manual Hash Map ===")

# Approach 2: Manual frequency counting
n = [1, 2, 3, 7, 8, 9, 1, 2, 3, 2, 1, 4, 2, 1, 5, 3, 1, 54]
m = [1, 4, 7, 10, 9, 33]

hash_map = {}
for i in n:
    hash_map[i] = hash_map.get(i, 0) + 1

# Print frequencies of elements in m
for i in m:
    if i in hash_map:
        print(f"{i} = {hash_map[i]}")
    else:
        print(f"{i} = 0")
