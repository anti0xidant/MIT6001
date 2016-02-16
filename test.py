def isPalindrome(aString):
    return palindrome(stringPrep(aString))

def stringPrep(aString):
    '''
    aString: a string

    Returns a string void of any non-alphabetical characters
    '''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''

    for element in aString:
        if element in ALPHABET:
            output = output + element

    return output

def palindrome(aString):
    '''
    aString: a string

    Return True if Palindrome; False otherwise.   
    '''
    # Base case: If string length is less than 2:
    if len(aString) < 2:

        # It is a palindrome
        return True

    # Else (string has length greater than 1)
    else:

        # return Assessment of first and last and inner string
        return aString[0] == aString[-1] and isPalindrome(aString[1:-1])

def stringPrepTest():
    # case[0] = string
    # case[1] = expected
    cases = (('', ''),
             (' ', ''),
             ('a', 'a'),
             ('aa', 'aa'),
             ('lkjsdfoiwuerlkhsdfWEFGRsdfsdf', 'lkjsdfoiwuerlkhsdfWEFGRsdfsdf'),
             ('owiehf23oihgWOIE!A', 'owiehfoihgWOIEA'))

    print 'Testing function: stringPrep()'
    print 'Number of test cases:', len(cases), '\n'

    for i in range(len(cases)):
        actual = stringPrep(cases[i][0])
        expected = cases[i][1]
        if actual == expected:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case', i + 1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print '\nEnd of tests.'

def palindromeTest():
    # case[0] = string
    # case[1] = expected
    cases = (('', True),
             ('aba', True),
             ('a', True),
             ('aa', True),
             ('lkjsdfoiwuerlkhsdfWEFGRsdfsdf', False),
             ('asdfghjkjhgfdsa', True))

    print 'Testing function: palindrome()'
    print 'Number of test cases:', len(cases), '\n'

    for i in range(len(cases)):
        actual = palindrome(cases[i][0])
        expected = cases[i][1]
        if actual == expected:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case', i + 1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print '\nEnd of tests.'
