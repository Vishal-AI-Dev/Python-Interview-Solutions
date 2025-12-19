def count_characters(text):
    """
    Counts the frequency of each character in a given string.
    Ignores case (A == a) and skips spaces to focus on data.
    """
    frequency = {}
    
    # Clean the data first: lowercase and remove spaces
    clean_text = text.lower().replace(" ", "")
    
    for char in clean_text:
        # METHOD 1: The 'if/else' Check (Standard Logic)
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
        # METHOD 2: The 'Pythonic' Way (Advanced)
        # frequency[char] = frequency.get(char, 0) + 1
            
    return frequency

# --- Test the Code ---
if __name__ == "__main__":
    input_text = "Engineering in Germany"
    result = count_characters(input_text)
    
    # Pretty print the dictionary for readability
    print(f"Analyzing: '{input_text}'\n")
    for key, value in result.items():
        print(f"Character '{key}': {value}")
