import sys

def find_second_largest(numbers):
    """
    Finds the second largest unique number in a list.
    Constraints: O(N) Time complexity. No sorting.
    """
    # 1. Edge Case: List too short
    if len(numbers) < 2:
        return None

    # 2. Initialize variables
    # We start with the smallest possible numbers
    largest = float('-inf')
    second = float('-inf')

    # 3. The Single Loop (O(N))
    for num in numbers:
        if num > largest:
            # Found a new King. The old King becomes the Prince.
            second = largest
            largest = num
        elif num > second and num != largest:
            # Found a new Prince (smaller than King, bigger than old Prince)
            second = num
            
    # 4. Final Check
    # If second is still -infinity, it means all numbers were the same (e.g., [5, 5, 5])
    if second == float('-inf'):
        return None
        
    return second

if __name__ == "__main__":
    try:
        # Input Logic (Taking a list string and converting it)
        user_input = input("Enter numbers separated by spaces (e.g., 10 20 4 45): ")
        
        # Convert string "10 20" -> list of integers [10, 20]
        number_list = [int(x) for x in user_input.split()]

        # Process
        result = find_second_largest(number_list)

        # Output
        if result is None:
            print("Error: List must have at least two unique numbers.")
        else:
            print(f"The second largest number is: {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
