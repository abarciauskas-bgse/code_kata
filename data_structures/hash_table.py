class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data  = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # else linear probe
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots != key:
                nextslot = self.rehash(nextslot)
            # fill in the next empty place
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot]  = data
            # REPLACE existing data associated with key
            else:
                self.data[nextslot] = data

    def hashfunction(self, key):
        return key%self.size

    def rehash(self, oldhash):
        return (oldhash+1)%self.size
