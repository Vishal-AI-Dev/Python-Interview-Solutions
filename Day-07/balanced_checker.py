def is_balanced(text):
    """
    Checks if the parentheses in the string are balanced.
    Supports (), [], {}. Ignores other characters.
    Returns: True (Balanced) or False (Unbalanced).
    """
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        # 1. If it is an Opening bracket, push to stack
        if char in mapping.values(): # values are (, [, {
            stack.append(char)
            
        # 2. If it is a Closing bracket, check the stack
        elif char in mapping.keys(): # keys are ), ], }
            # If stack is empty OR top of stack doesn't match, fail immediately
            if not stack or stack.pop() != mapping[char]:
                return False
                
    # 3. Final Check
    # If stack is empty, we are good (True). If items remain, we failed (False).
    return len(stack) == 0

if __name__ == "__main__":
    # Test Cases
    test_cases = [
        "([]){}",       # True
        "(a + b) * c",  # True
        "({[}])",       # False (Wrong order)
        "((",           # False (Not closed)
        ")("            # False (Closed before open)
    ]
    
    print("--- Balanced Parentheses Checker ---")
    for test in test_cases:
        result = is_balanced(test)
        status = "✅ Valid" if result else "❌ Invalid"
        print(f"'{test}' : {status}")

    # User Input
    user_input = input("\nEnter your own string: ")
    if is_balanced(user_input):
        print("Result: Balanced!")
    else:
        print("Result: Unbalanced.")
