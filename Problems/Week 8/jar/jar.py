class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size == self.capacity:
            raise ValueError("can't add any more cookies to the jar")
        if n <= 0:
            raise ValueError("expected a non-negative int")
        if n > self.capacity:
            raise ValueError("can't be greater than capacity")
        self.size += n

    def withdraw(self, n):
        if self.size == 0:
            raise ValueError("non cookies in jar")
        if n <= 0:
            raise ValueError("expected a non-negative int")
        if n > self.capacity:
            raise ValueError("can't be greater than capacity")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("expected a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Expected a non-negative int")
        self._size = size

# jar = Jar(12)
# print(jar.size)
# jar.deposit(3)
# print(jar.size)
# print(jar)
