# A sequence of integers is called a zigzag sequence if
# each of its elements is either strictly less than all
# its neighbors or strictly greater than all its neighbors.
# For example, the sequence 4 2 3 1 5 3 is a zigzag,
# but 7 3 5 5 2 and 3 8 6 4 5 aren't. Sequence of length 1
# is also a zigzag.

# For a given array of integers return the length of its
# longest contiguous sub-array that is a zigzag sequence.

def ZigZag(a):
    # Assume 2 < a.length < 25 and 0 < a[i] < 100
    
