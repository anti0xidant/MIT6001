class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        '''
        Returns number of elements in intSet
        '''
        return len(self.vals)

    def intersect(self, other):
        '''
        Returns a new intSet containing common elements of self
            and other.
        Returns empty intSet if there are no common elements.
        '''
        # Create new intSet object
        intSetNew = intSet()

        # Find the shorter intSet
        if len(self) < len(other):
            shorter = self
            longer = other
        else:
            shorter = other
            longer = self

        # For every element in shorter intSet
        for e in shorter.vals:

            print e
            # If element exists in other
            if longer.member(e):

                # Add that element to intSetNew
                intSetNew.insert(e)
                print intSetNew
            
        # Return new intSet
        return intSetNew
