import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline() # reads a single line. entire file is one line
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read()) # read() returns a string. not sure if type conversion is needed
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text # just to house the input text. can be text to encrypt (taken in by PlaintextMessage)
                                 # or can be encrypted text (taken in by CyphertextMessage)
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        # ok to return original object because it is immutable
        # accessing the object through a get method prevents
        # users from re-binding the internal data attribute
        return self.message_text 

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        # returns a copy because lists are mutable.
        # would be bad to return the original because
        # user may accidentally mutate it, causing mutation
        # of internal data object as well
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        import string
        
        # Build ascii lowercase list
        lowercaseList = []
        for letter in string.ascii_lowercase:
            lowercaseList.append(letter)

        # Build uppercase list
        uppercaseList = []
        for letter in string.ascii_uppercase:
            uppercaseList.append(letter)

        # For each shift round:
        for cycle in range(shift):

            # Shift adjacent indexes of lowercase
            for i in range(len(lowercaseList)-1):
                lowercaseList[i], lowercaseList[i+1] = lowercaseList[i+1], lowercaseList[i]
            # Shift adjacent indexes of uppercase
            for i in range(len(uppercaseList)-1):
                uppercaseList[i], uppercaseList[i+1] = uppercaseList[i+1], uppercaseList[i]

        shiftdict = {}
        # For every letter in ascii lowercase:
        for i in range(len(string.ascii_lowercase)):

            # Create dictionary element
            shiftdict[string.ascii_lowercase[i]] = lowercaseList[i]
            
        # For every letter in ascii uppercase:
        for i in range(len(string.ascii_uppercase)):

            # Create dictionary element
            shiftdict[string.ascii_uppercase[i]] = uppercaseList[i]

        return shiftdict 

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # Build encryption dictionary
        shiftdict = self.build_shift_dict(shift)

        outputMessage = ''
        # For every letter in self.message_text:
        for letter in self.message_text:

            # Get the letter from the dictionary
            # If letter does not have conversion, use original letter.
            l = shiftdict.get(letter, letter)
    
            # Add it to the output Message
            outputMessage = outputMessage + l

        # Return output message
        return outputMessage

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text) # Initializes self.message_text and self.valid_words
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift) # doesn't find that method in PaintextMessage so looks in superclass Message
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return dict(self.encrypting_dict) # dict() makes a copy, just as list() does

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # If shifting backwards
        if shift < self.shift:

            # Shift to zero first, then to new position
            newPosition = 26 - self.shift + shift

        # Elese (not shifting backwards)
        else:

            # Shift forward to the new p
            newPosition = shift - self.shift

        # Apply the shifts
        self.encrypting_dict = self.build_shift_dict(newPosition)
        self.message_text_encrypted = self.apply_shift(newPosition)
        self.shift = shift
            
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Create variables for max matched and it's shifted string
        bestShiftValue = 0
        bestShiftMessage = ''
        bestMatchCount = 0

        # For each shift from 0 to 25
        for shift in range(26):

            # Run the shift
            shiftedMessage = self.apply_shift(shift)

            # Count the number of matches
            matches = 0
            shiftedMessageList = shiftedMessage.split()
            for word in shiftedMessageList:
                if word in self.valid_words:
                    matches += 1

            # If the number of matches is greater than current max
            if matches > bestMatchCount or bestMatchCount == 0:

                # Store the max value and the shifted string.
                bestShiftValue = shift
                bestShiftMessage = shiftedMessage
                bestMatchCount = matches

        # Return tuple (best shift value, decrypted message)
        return (bestShiftValue, bestShiftMessage)

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()
