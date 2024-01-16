import random


class RandomizedSet:
    
    def __init__(self):
        self.list = []
        self.map = {}
    
    def search(self, val:int) -> bool :
        return val in self.map
    
    def insert(self, val: int) -> bool:
        if(self.search(val)) :
            return False
        self.map[val]=len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(not self.search(val)) :
            return False
        idx = self.map[val]
        self.list[idx] = self.list[-1]
        
        self.map[self.list[idx]]=idx
        del self.map[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()