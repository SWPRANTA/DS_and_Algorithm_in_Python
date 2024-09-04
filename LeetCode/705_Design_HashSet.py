class MyHashSet(object):

    def __init__(self):
        self.size = 10
        self.bucket = [[] for _ in range(self.size)]
    
    def hash(self, key):
        h = key%self.size
        print(f"H is {h} for {key}")
        return key % self.size
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash(key)
        if key not in self.bucket[h]:
            self.bucket[h].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash(key)
        if key in self.bucket[h]:
            self.bucket[h].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        h = self.hash(key)
        if key in self.bucket[h]:
            return True
        return False
    
    def printHashSet(self):
        for bucket in self.bucket:
            print(bucket)

myHashSet = MyHashSet()
myHashSet.add(1)   
myHashSet.add(2)
myHashSet.add(10) 
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)     
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
myHashSet.add(10000)

myHashSet.printHashSet()

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)