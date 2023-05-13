import sys


class NativeCache:
    def __init__(self, sz):
        self.step = 1
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        byte_string = str(key).encode()
        hash_sum = sum(byte_string) % self.size
        return hash_sum

    def seek_slot(self, value):
        hash = self.hash_fun(value)
        hash_idx = initial_hash_idx = hash
        mod_trigger = False

        while True:
            slot = self.slots[hash_idx]
            if slot is None:
                return hash_idx
            hash_idx += self.step
            if hash_idx >= self.size:
                mod_trigger = True
                hash_idx = hash_idx % self.size
            if mod_trigger and hash_idx >= initial_hash_idx:
                return None

    def remove_unpopular(self):
        min_hit_value = sys.maxsize
        min_hit_idx = None
        for idx, hits_amount in enumerate(self.hits):
            if hits_amount < min_hit_value:
                min_hit_value = hits_amount
                min_hit_idx = idx
        self.slots[min_hit_idx] = None
        self.values[min_hit_idx] = None
        self.hits[min_hit_idx] = 0
        return min_hit_idx

    def is_key(self, key):
        if key is None:
            return False
        for item in self.values:
            if item == key:
                return True
        return False

    def put(self, key, value):
        idx_of_value = self.seek_slot(value)
        if idx_of_value is None:
            self.remove_unpopular()
            idx_of_value = self.seek_slot(value)

        self.values[idx_of_value] = key
        self.slots[idx_of_value] = value

    def find_key_idx(self, key):
        if key is None:
            return None
        for idx, item in enumerate(self.values):
            if item == key:
                return idx
        return None

    def get(self, key):
        key_idx = self.find_key_idx(key)

        if key_idx is None:
            return None

        self.hits[key_idx] += 1
        return self.slots[key_idx]
