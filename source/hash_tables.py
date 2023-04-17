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
        hash_idx = initial_hash_idx = self.slots[hash]
        mod_trigger = False

        while True:
            slot = self.slots[hash_idx]
            if slot is None:
                return hash_idx
            hash_idx += self.step
            if hash_idx >= self.size:
                mod_trigger = True
                hash_idx = (hash_idx + self.step) % self.size
            if mod_trigger and hash_idx >= initial_hash_idx:
                return None

        #   0   1   2   3   4   5   6   7   8   9
        #   -       -       -       -       -
        return None

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        return None

    def find(self, value):
        # находит индекс слота со значением, или None
        return None
