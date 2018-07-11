# Your Informatics teacher at school likes coming up with new ways to help
# you understand the material. When you started studying numeral systems,
# he introduced his own numeral system, which he's convinced will help clarify
# things. His numeral system has base 26, and its digits are represented by
# English capital letters - A for 0, B for 1, and so on.
# The teacher assigned you the following numeral system exercise:
# given a one-digit number, you should find all unordered pairs of one-digit
# numbers whose values add up to the number.
# Example
# For number = 'G', the output should be
# newNumeralSystem(number) = ["A + G", "B + F", "C + E", "D + D"].
# Translating this into the decimal numeral system we get:
# number = 6, so it is ["0 + 6", "1 + 5", "2 + 4", "3 + 3"].
# Assume input is "A" <= number <= "Z".

def newNumeralSystem(number):
    # Initialize and empty solution list
    solution = []
    # Define the number system.
    system = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
        'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    # Invert the dict for reverse lookups.
    system_inv = dict((v, k) for k, v in system.items())
    print('System[number]=', system[number])
    # Find unordered pairs of one-digit numbers that add up to 'number'.
    for i in range(0, system[number]):
        for j in range(i, system[number]+1):
            if (i + j) == system[number]:
                success = str(system_inv[i] + ' + ' + system_inv[j])
                solution.append(success)
    # Handle case where number = 'A'
    if number == 'A': return ['A' + ' + ' + 'A']
    return solution

newNumeralSystem('A')
