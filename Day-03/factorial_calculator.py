def calculate_factorial(n):
    
    #  Handle Negative Numbers (Edge Case)
    if n < 0:
        return None  # Factorial does not exist for negatives
    
    # Handle Zero (Edge Case)
    if n == 0:
        return 1
    
    # The Logic Loop
    result = 1
    # We loop from 1 up to n (inclusive)
    # range(1, n + 1) generates: 1, 2, 3, ... n
    for i in range(1, n + 1):
        result = result * i  # Accumulate the multiplication
        
    return result

if __name__ == "__main__":
    try:
        # Input
        user_input = int(input("Enter a non-negative integer: "))
        
        # Processing
        fact = calculate_factorial(user_input)
        
        # Output Logic
        if fact is None:
            print("Error: Factorial does not exist for negative numbers.")
        else:
            print(f"The factorial of {user_input} is {fact}")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")
