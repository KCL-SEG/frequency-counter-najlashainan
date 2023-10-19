"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    for i in items:
        i = str(i) #convert to string
        if i not in frequencies.keys() :
            frequencies[i] = 1
        else:
            frequencies[i]+= 1

    return frequencies


result1 = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(result1)  # Output: { 'a': 2, 'b': 3, 'c': 1 }