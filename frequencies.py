"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    # Create an empty dictionary to store frequencies
    frequency_dict = {}

    # Iterate through the items list
    for item in items:
        # Convert the item to a string if it's not already
        item_str = str(item)

        # Check if the item_str is already a key in the dictionary
        if item_str in frequency_dict:
            # If it is, increment the count
            frequency_dict[item_str] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            frequency_dict[item_str] = 1

    return frequency_dict

# Test cases
result1 = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(result1)  # Output: { 'a': 2, 'b': 3, 'c': 1 }
