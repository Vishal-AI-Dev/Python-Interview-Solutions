def count_character_frequency(text):
    
    #  Initialize an empty dictionary (The "Paper")
    frequency_map = {}
    
    # Pre-process the text
    # Lowercase everything so 'A' == 'a'
    clean_text = text.lower()
    
    #  The Logic Loop
    for char in clean_text:
        # We only want to count letters and numbers (isalnum)
        # This removes spaces, commas, etc.
        if char.isalnum():
            
            # Check if we have seen this char before
            if char in frequency_map:
                frequency_map[char] += 1  # Increment count
            else:
                frequency_map[char] = 1   # First time seeing it
                
    return frequency_map

if __name__ == "__main__":
    # Input
    user_input = input("Enter a string to analyze: ")
    
    # Process
    result = count_character_frequency(user_input)
    
    # Output (Printing cleanly)
    print("\nCharacter Frequencies:")
    for char, count in result.items():
        print(f"'{char}': {count}")
