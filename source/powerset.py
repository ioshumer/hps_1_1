class PowerSet:

    def __init__(self):
        self.data = []
        self.counter = 0

    def size(self):
        return self.counter

    def put(self, value):
        if not value in self.data:
            self.data.append(value)
            self.counter += 1

    def get(self, value):
        try:
            self.data.index(value)
        except ValueError:
            return False
        else:
            return True

    def remove(self, value):
        try:
            self.data.remove(value)
        except ValueError:
            return False
        else:
            self.counter -= 1
            return True

    def intersection(self, set2):
        intersected = PowerSet()
        for item in self.data:
            if set2.get(item):
                intersected.put(item)
        return intersected

    def union(self, set2):
        union = PowerSet()
        for item in self.data:
            union.put(item)
        for item in set2.data:
            union.put(item)
        return union

    def difference(self, set2):
        diff = PowerSet()
        for item in self.data:
            if not set2.get(item):
                diff.put(item)
        for item in set2.data:
            if not self.get(item):
                diff.put(item)
        return diff

    def issubset(self, set2):
        for item in set2.data:
            if not self.get(item):
                return False
        return True
