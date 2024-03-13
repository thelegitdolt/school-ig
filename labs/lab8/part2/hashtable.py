class Hashtable:
    def __init__(self, size=8):
        self.size = size
        self.values = [[] for _ in range(size)]
    
    
    def get(self, key):
        for pair in self.get_bucket(key):
            if pair[0] == key:
                return pair[1]
        
    
    def get_size(self):
        return self.size
    
    def add(self, key, value):
        self.get_bucket(key).append((key, value))
    
    def remove(self, key):
        bucket = self.get_bucket(key)
        try:
            ind = [pair[0] for pair in bucket].index(key)
        except ValueError:
            return None
        
        return bucket.pop(ind)
    
    def is_empty(self):
        for bucket in self.values:
            if len(bucket) > 0:
                return False
            
        return True
    
    def __len__(self):
        return sum([len(a) for a in self.values])
    
    def get_bucket(self, key):
        char_sum = 0
        for char in key:
            char_sum += ord(char)
            
        hashed_str = char_sum % self.size
        return self.values[hashed_str % self.size]
    