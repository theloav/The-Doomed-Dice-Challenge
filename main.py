from collections import Counter
from itertools import product

def calculate_combinations():
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    
    total_combinations = len(die_A) * len(die_B)
    print(f"Total Combinations: {total_combinations}")
    
    sum_distribution = Counter(a + b for a, b in product(die_A, die_B))
    print("\nSum Distribution:")
    for key in sorted(sum_distribution.keys()):
        print(f"Sum {key}: {sum_distribution[key]} occurrences")
    
    probability_distribution = {key: val / total_combinations for key, val in sum_distribution.items()}
    print("\nProbability Distribution:")
    for key in sorted(probability_distribution.keys()):
        print(f"P(Sum = {key}) = {probability_distribution[key]:.4f}")
    
    return probability_distribution

def undoom_dice(original_A, original_B):
    sum_distribution = Counter(a + b for a, b in product(original_A, original_B))
    
    new_die_A = [1, 1, 2, 2, 3, 4]
    new_die_B = [1, 2, 3, 4, 5, 6]
    
    new_distribution = Counter(a + b for a, b in product(new_die_A, new_die_B))
    
    if new_distribution == sum_distribution:
        print("Successfully restored dice!")
    else:
        print("Error: Sum probabilities do not match!")
    
    print(f"New Die A: {new_die_A}")
    print(f"New Die B: {new_die_B}")
    
    return new_die_A, new_die_B

# Part A
probabilities = calculate_combinations()

# Part B
original_A = [1, 2, 3, 4, 5, 6]
original_B = [1, 2, 3, 4, 5, 6]
undoom_dice(original_A, original_B)
