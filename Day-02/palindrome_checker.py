def is_palindrome(text):
    """
    Checks if a string is a palindrome.
    Ignores case, spaces, underscores, and hyphens.
    Works with numbers (e.g., '12-21').
    """
    # We convert to lowercase first so 'A' == 'a'
    # Then we replace space, underscore, and hyphen with nothing ("")
    clean_text = text.lower().replace(" ", "").replace("_", "").replace("-", "")
    
    # [::-1] creates a copy of the string in reverse
    reversed_text = clean_text[::-1]
    
    # Return the Boolean result (True or False)
    return clean_text == reversed_text

if __name__ == "__main__":
    # Input
    user_input = input("Enter text/number to check: ")
    
    # Processing
    result = is_palindrome(user_input)
    
    # Output
    if result:
        print(f"True! '{user_input}' is a Palindrome.")
    else:
        print(f"False. '{user_input}' is NOT a Palindrome.")
