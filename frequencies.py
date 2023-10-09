"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequency = {}
   
    for item in items:
        string_item = str(item)

        if string_item in frequency:
            frequency[string_item] += 1
        else:
            frequency[string_item] = 1    
    return frequencies

result1 = frequencies(['a', 'a' , 'b', 'b', 'b', 'c'])
print(result1)