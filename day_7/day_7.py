"""
- parse input into two arrays
    - 1 for test values
    - 1 for array of numbers in each equation

- loop over each value & numbers:
    - make multiples arrays of length len(numbers) - 1 for order of operators:
        - use backtracking to to make multiple permutations of the two possibilities
    - test each order and add value to sum if equation result matches
"""