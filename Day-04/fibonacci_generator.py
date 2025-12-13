def generate_fibonacci(n):
    """
    Generates a list of the first n Fibonacci numbers.
    Sequence: 0, 1, 1, 2, 3, 5, 8...
    """
    # 1. Handle Negative/Zero inputs
    if n <= 0:
        return []
    
    # 2. Handle First Element case
    if n == 1:
        return [0]

    # 3. Initialize the sequence
    sequence = [0, 1]
    
    # 4. The Loop
    # We already have 2 numbers, so we loop (n - 2) times
    while len(sequence) < n:
        # Get the last two numbers
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        
    return sequence

if __name__ == "__main__":
    try:
        # Input
        n_terms = int(input("How many Fibonacci numbers do you want? "))
        
        if n_terms < 0:
             print("Please enter a positive integer.")
        else:
             # Processing
             result = generate_fibonacci(n_terms)
             
             # Output
             print(f"First {n_terms} Fibonacci numbers:")
             print(result)
             
    except ValueError:
        print("Invalid input. Please enter a whole number.")
