class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        byte_string = value.encode()
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

    def put(self, value):
        slot_idx = self.seek_slot(value)
        if slot_idx is not None:
            self.slots[slot_idx] = value
        return slot_idx

    def find(self, value):
        return self.seek_slot(value)
