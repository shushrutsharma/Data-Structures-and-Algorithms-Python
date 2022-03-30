# hashset | leetcode 705 | https://leetcode.com/problems/design-hashset/

class HashSet:

    # constructor
    def __init__ (self, hash_set = None):
        '''initialize a hash set'''
        self.hash_set: dict = {} if hash_set == None else hash_set
        self.size: int = len(self.hash_set.keys())

    # initialize iterator for __iter__
    def __iter__ (self):
        self.n = 0
        return self
    
    # return next element for __next__
    def __next__ (self):
        if self.n < self.size:
            result = list(self.hash_set.keys())[self.n]
            self.n = self.n + 1
            return result
        else:
            raise StopIteration

    def add (self, key) -> None:
        '''add element to hash set'''
        self.hash_set[key] = True
        self.size = self.size + 1

    def contains (self, key) -> bool:
        '''does hash set contain element'''
        return True if self.hash_set.get(key) else False

    def remove (self, key) -> None:
        '''remove element from hash set'''
        if self.contains(key):
            self.hash_set.pop(key)
            self.size = self.size - 1

# initialize a new hashset
hashSet = HashSet()

# add values to a hash set
hashSet.add('first')
hashSet.add('second')
hashSet.add('third')
hashSet.add('fourth')

# remove from a hash set
hashSet.remove('fourth')

# check if value exists in a hash set
print(hashSet.contains('first'))
print(hashSet.contains('fourth'))

# iterate through a hash set
for element in hashSet:
    print(element)