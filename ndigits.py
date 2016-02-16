def ndigits(x):
    '''
    x: an integer of any sign.

    Returns number of digits in x.
    '''

    # Base case: Positive x input will converge to x = 0
    #            Negative x input will converge to x = -1
    if x == 0 or x == -1:
        return 0

    # Recursive case: Total length of x is the length of
    # the left-most digit + the length of the remaining digits.
    # Remove the left-most digit of x using x/10.
    else:
        return 1 + ndigits(x/10)
