def longestRun(L):
    #For every sublist leng beginning from length fo L down to 1
    for i in range(len(L), 0, -1):

        #Generate all the sublsits of that level
        sublists = getSublists(L, i)

        #For each sublist of the sublsits generated
        for sublist in sublists:

            #Test if it is monotonic
            for e in range(1, len(sublist)):
                if sublist[e] < sublist[e-1]:
                    break
                
            #Return the level number if it is monotonic
            else:
                return i

    #Return 0 (didn't find any monotonic sublists)
    return 0

def getSublists(L, n):
    '''
    L: list of integers.
    n: length of sublist to return
    Returns a list of all possible subsets in L of length n
    '''
    sublists = []

    begin = 0
    end = n - 1

    while end < len(L):
        # generate sublist from begin to end
        sublist = L[begin:end+1]
        
        # add it to the sublist
        sublists.append(sublist)

        #shift begin and end up by 1
        begin += 1
        end += 1

    return sublists
