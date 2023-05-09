class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitmask = 0

    def _common_hash(self, random_value, string):
        result = 0
        for c in string:
            code = ord(c)
            result = result * random_value + code
        return result % self.filter_len

    def _set_bit(self, idx):
        self.bitmask = self.bitmask | (1 << idx)
        return self.bitmask

    def _check_bit(self, idx):
        result = (self.bitmask >> idx) & 1
        return result == 1

    def hash1(self, str1):
        rand_val = 17
        return self._common_hash(rand_val, str1)

    def hash2(self, str1):
        rand_val = 223
        return self._common_hash(rand_val, str1)

    def add(self, str1):
        idx_1 = self.hash1(str1)
        idx_2 = self.hash2(str1)
        self._set_bit(idx_1)
        self._set_bit(idx_2)

    def is_value(self, str1):
        idx_1 = self.hash1(str1)
        idx_2 = self.hash2(str1)
        return self._check_bit(idx_1) and self._check_bit(idx_2)
