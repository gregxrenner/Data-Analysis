# Given an integer size, return an array containing each integer from 1 to size in the following order:
# 1, size, 2, size - 1, 3, size - 2, 4, ...
# For size = 7, the output should be constructArray(size) = [1, 7, 2, 6, 3, 5, 4].
# Guaranteed constraints: 1 ≤ size ≤ 15.

def constructArray(size):
    # Initialize arr as empty lst to build into
    lst = []
    # Create a list from 1 to size to build lst from
    resources = list(range(1, size+1))
    while len(resources) > 0:
        # Reverse the resources list
        resources.reverse()
        # Pop the last element from the sequence
        lst.append(resources.pop(-1))
        #print('resources=', resources)
        #print('lst=', lst)
    return lst

# Test
constructArray(7)
