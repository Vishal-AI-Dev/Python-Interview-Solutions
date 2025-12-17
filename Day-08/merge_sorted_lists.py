def merge_sorted_lists(list1, list2):
    """
    Merges two sorted lists into one sorted list using Two Pointers.
    Complexity: O(N + M) Time.
    """
    # 1. Initialize Pointers
    i = 0 # Pointer for list1
    j = 0 # Pointer for list2
    merged_list = []
    
    # 2. The Loop (Compare and Append)
    # Run while BOTH lists still have items
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1 # Move pointer i forward
        else:
            merged_list.append(list2[j])
            j += 1 # Move pointer j forward
            
    # 3. Handle Leftovers
    # If list1 has items left, add them all
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
        
    # If list2 has items left, add them all
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
        
    return merged_list

if __name__ == "__main__":
    # Test Data (Must be sorted already!)
    l1 = [1, 3, 5, 7, 10]
    l2 = [2, 4, 6, 8]
    
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    
    result = merge_sorted_lists(l1, l2)
    
    print(f"Merged: {result}")
