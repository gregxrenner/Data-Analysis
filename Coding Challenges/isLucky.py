# This is the first challenge from CodeFights.com, the challenge
#   is: Ticket numbers usually consist of an even number of digits.
#   A ticket number is considered "lucky" if the sum of the first
#   half of the digits is equal to the sum of the second half.
#   Given a ticket number "n", determine if a ticket is lucky.

def isLucky(n):
    # check that n is an integer
    if type(n) != int:
         return "n must be an integer."
    n_length = len(str(n))
    # make sure n has an even number of digits
    if n_length%2 != 0:
        return "n must have an even number of digits."
    first_half_sum = totalDigits(str(n)[:n_length//2])
    second_half_sum = totalDigits(str(n)[n_length//2:])
    if first_half_sum == second_half_sum:
        return True
    else:
        return False

def totalDigits(x):
    total = 0
    for i in x:
        total += int(i)
    return total

isLucky(123231)
