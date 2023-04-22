class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        byte_string = key.encode()
        hash_sum = sum(byte_string) % self.size
        return hash_sum

    def is_key(self, key):
        idx_of_slot = self.hash_fun(key)
        if self.values[idx_of_slot] is not None:
            return True
        return False

    def put(self, key, value):
        idx_of_key = self.hash_fun(key)
        idx_of_value = self.hash_fun(value)
        self.values[idx_of_key] = idx_of_value
        self.slots[idx_of_value] = value

    def get(self, key):
        idx_of_key = self.hash_fun(key)
        if self.values[idx_of_key] is not None:
            idx_of_value = self.values[idx_of_key]
            return self.slots[idx_of_value]
        return None
