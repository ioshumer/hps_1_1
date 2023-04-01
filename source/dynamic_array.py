import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.default_capacity = 16

        self._iterator_pointer = 0

    def __len__(self):
        return self.count

    def as_list(self):
        return [self.array[idx] for idx in range(self.count)]

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # В тестах используется схема, когда увеличение буфера происходит в два раза,
        # Увеличение буфера выполняем, когда он весь полностью заполнен, и выполняется попытка добавления.
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        new_array_capacity = 2 * self.capacity if self.count == self.capacity else self.capacity
        new_array_len = self.count + 1
        new_array = self.make_array(new_array_capacity)

        new_array_pointer = 0
        old_array_pointer = 0

        while new_array_pointer < new_array_len:
            if new_array_pointer == i:
                new_array[new_array_pointer] = itm
            else:
                new_array[new_array_pointer] = self.array[old_array_pointer]
                old_array_pointer += 1
            new_array_pointer += 1

        self.array = new_array
        self.capacity = new_array_capacity
        self.count = new_array_len

    def delete(self, i):
        # а уменьшение в полтора раза.
        # (текущее значение размера буфера делится на 1.5, и результат приводится к целому типу, никаких округлений!).
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        array_pointer = 0

        while array_pointer < self.count:
            if array_pointer >= i:
                try:
                    self.array[array_pointer] = self.array[array_pointer+1]
                except (ValueError, IndexError):
                    self.array[array_pointer] = None
            array_pointer += 1

        self.count -= 1

        capacity_bound = int((self.count / self.capacity) * 100)
        if (capacity_bound < 50) and (capacity_bound > self.default_capacity):
            new_capacity = int(self.capacity / 1.5)
            new_capacity = new_capacity if new_capacity > self.default_capacity else self.default_capacity
            self.resize(new_capacity)
            self.capacity = new_capacity
