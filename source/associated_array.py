class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        byte_string = str(key).encode()
        hash_sum = sum(byte_string) % self.size
        return hash_sum

    def is_key(self, key):
        if key is None:
            return False
        for item in self.values:
            if item == key:
                return True
        return False

    def put(self, key, value):
        if type(key) is not str:
            return None
        idx_of_value = self.hash_fun(value)
        self.values[idx_of_value] = key
        self.slots[idx_of_value] = value

    def get(self, key):
        if key is None:
            return None
        for idx, item in enumerate(self.values):
            if item == key:
                return self.slots[idx]
        return None
