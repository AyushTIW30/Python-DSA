import math
import time

def find_divisors_optimized(number):
    """Efficiently find all divisors of a number using sqrt method."""
    divisors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)

def find_divisors_bruteforce(number):
    """Brute-force approach to find all divisors of a number."""
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# User input
num = int(input("Enter a number: "))

# Choose approach
print("Choose method: 1 → Optimized, 2 → Brute-force")
choice = input("Enter choice (1/2): ")

start_time = time.time()

if choice == '1':
    divisors = find_divisors_optimized(num)
elif choice == '2':
    divisors = find_divisors_bruteforce(num)
else:
    print("Invalid choice! Using optimized method by default.")
    divisors = find_divisors_optimized(num)

end_time = time.time()

print(f"Divisors of {num} are:\n{divisors}")
print(f"Execution time: {end_time - start_time:.6f} seconds")





