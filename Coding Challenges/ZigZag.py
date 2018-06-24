def zigZag(a):
    # initialize zigzag as empty list
    longest_zz = [a[0]]
    zigzag = []
    zigging = False
    seq = []
    index = 0
    # check if the first character is part of a zigZag
    if (a[0] < a[1] and a[1] > a[2]) or (a[0] > a[1] and a[1] < a[2]):
        seq = [a[0]] # add the first character to zigzag
        zigging = True
    else:
        zigging = False
    # itierate through the list
    for i in a[1:-1]:
        index += 1
        print("i=", i)
        if a[index-1] < i and a[index+1] < i:
            if zigging == True:
                seq.append(i)
            else:
                seq = [a[index-1], i]
                zigging = True
        elif a[index-1] > i and a[index+1] > i:
            if zigging == True:
                seq.append(i)
            else:
                seq = [a[index-1], i]
                zigging = True
        else:
            if zigging == True:
                seq.append(i)
                zigzag = list(seq)
                zigging = False
            seq = []
        if len(zigzag) >= len(longest_zz):
            longest_zz = list(zigzag)
        print("seq=", seq)
        print("zigzag=", zigzag)
        print("longest_zz=", longest_zz)
    # check is list ends while zigzaggin
    if zigging == True:
        print('List ends while zigging.')
        seq.append(a[-1])
        zigzag = list(seq)
        print("seq=", seq)
        print("zigzag=", zigzag)
        if len(zigzag) >= len(longest_zz):
            longest_zz = list(zigzag)
        print("longest_zz=", longest_zz)
    # Handle case where no zigzag is found to be longer than 1
    if len(longest_zz)==1:
        if (a[0] != a[1]):
            longest_zz = a[0:2]
        elif (a[-2] != a[-1]):
            longest_zz = a[-2:]
    return len(longest_zz)


test = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6]
test = [2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4]
test = [1, 3, 2, 3, 4, 5, 1, 4, 2, 3]
test = [1, 2, 2, 2]
zigZag(test)
