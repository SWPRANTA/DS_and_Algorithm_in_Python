class MyHashMap(object):

    def __init__(self):
        self.size = 10
        self.bucket = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self.hash(key)
        print(f"Hash for {key} is {h}")
        if h<=self.size:
            print("inside if")
            for index, keyValPair in enumerate(self.bucket[h]):
                if key == keyValPair[0]:
                    self.bucket[h][index] = (key, value)
                    return
            self.bucket[h].append((key, value)) 


    def get(self, key):
        h = self.hash(key)
        if h<=self.size:
            for index, keyValPair in enumerate(self.bucket[h]):
                if key == keyValPair[0]:
                    return keyValPair[1]
        
        return -1

    def remove(self, key):
        h = self.hash(key)
        if h<=self.size:
            for index, keyValPair in enumerate(self.bucket[h]):
                if key == keyValPair[0]:
                    self.bucket[h].remove(keyValPair)
                    return
    def printMyMap(self):
        for bucket in self.bucket:
            print(bucket)
myHashMap = MyHashMap()
myHashMap.put(1, 1); # The map is now [[1,1]]
myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]

myHashMap.printMyMap()
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
