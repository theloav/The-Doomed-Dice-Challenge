# The-Doomed-Dice-Challenge

## Overview
The Doomed Dice Challenge is a probability-based problem involving two six-sided dice. This challenge is divided into two parts:

- **Part A**: Calculate the total number of combinations, display the sum distribution, and determine the probability of obtaining different sums.
- **Part B**: Modify the dice under constraints imposed by Loki while maintaining the same sum probability distribution.

## Implementation
The solution is implemented in Python using `itertools.product` and `collections.Counter` for efficient calculation of combinations and probabilities.

## Files
- `doomed_dice.py`: Contains the implementation of Part A and Part B.

## Usage
### Running the script
Ensure you have Python installed, then run:
```sh
python doomed_dice.py
```
### Expected Output
The script outputs:
1. The total number of possible dice roll combinations.
2. A breakdown of how often each sum appears.
3. The probability distribution of sums.
4. The adjusted dice values after being 'undoomed' while maintaining the same probabilities.

## Functions
### `calculate_combinations()`
- Computes all possible sums from rolling two dice.
- Displays the frequency and probability distribution of sums.

### `undoom_dice(original_A, original_B)`
- Modifies the dice values while ensuring the probability distribution remains unchanged.
- Prints the new dice configurations.

## Example Output
```
Total Combinations: 36

Sum Distribution:
Sum 2: 1 occurrences
Sum 3: 2 occurrences
...
Probability Distribution:
P(Sum = 2) = 0.0278
P(Sum = 3) = 0.0556
...
Successfully restored dice!
New Die A: [1, 1, 2, 2, 3, 4]
New Die B: [1, 2, 3, 4, 5, 6]
```

## Dependencies
- Python 3.x
- No external libraries required

## License
This project is open-source and available under the MIT License.

