class Hand(object):
	def __init__(self, n):
		'''
		Initializes Hand.

		n(int): size of the hand.
		'''
		assert type(n) == int
		self.HAND_SIZE = n
		self.VOWELS = 'aeiou'
		self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

		# Deal a new hand
		self.dealNewHand()

	def dealNewHand(self):
		'''
		Deals a new hand, and sets the hand attribute to the new hand.
		'''
		# Set self.hand to a new, empty dictionary.
		self.hand = {}

		# Build the hand
		import random

		numVowels = self.HAND_SIZE / 3

		for i in range(numVowels):
			x = self.VOWELS[random.randrange(0, len(self.VOWELS))]	
			self.hand[x] = self.hand.get(x, 0) + 1

		for i in range(numVowels, self.HAND_SIZE):
			x = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
			self.hand[x] = self.hand.get(x, 0) + 1

	def setDummyHand(self, handString):
		'''
		Allows you to set a dummy hand. 

		handString(str): A string of letters you wish to be in your hand. Length of this
		string must be equal to self.HAND_SIZE.
		'''
		assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal lenth of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
		self.hand = {}
		for char in handString:
			self.hand[char] = self.hand.get(char, 0) + 1

	def calculateLen(self):
		'''
		Calculate length of the hand.
		'''
		sum = 0
		for i in self.hand:
			sum += self.hand[i]
		return sum

	def __str__(self):
		'''
		Displays string representation of hand.
		'''
		output = ''
		keys = self.hand.keys()
		keys.sort()
		for letter in keys:
			output += self.hand[letter] * letter
		return otuput
