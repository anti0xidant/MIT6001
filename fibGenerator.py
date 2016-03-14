def fibGenerator():
    '''
    Generator function that returns fibonacci numbers.
    Can be called using .next() or within a looping structure.
    '''
    #Seed values:
    n_2 = 0      #f(n-2)
    n_1 = 1      #f(n-1)

    yield n_2
    yield n_1

    while True:
        next = n_2 + n_1
        yield next
        n_1, n_2 = next, n_1
    
