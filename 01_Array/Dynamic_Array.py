import ctypes


class MyList:
    def __init__(self):
        self.size = 1  # How many times u can store
        self.n = 0  # Now how many items are there
        self.A = self.__make__array(self.size)

    def __make__array(self, capacity):
        return (ctypes.py_object * capacity)()  # creates a ctype array with size capacity

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create new array with new capacity
        B = self.__make__array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    # Print the array
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    # Indexing
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    # Pop
    def pop(self):
        if self.n == 0:
            return 'Empty List'

        print(self.A[self.n - 1])
        self.n = self.n - 1

    # Clear : cleans all the elements present in the array
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'

    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        self.A[pos] = item
        self.n = self.n + 1

    # deletes the element based on the position mentioned
    def __delete__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1

    # removes the element based on the value mentioned
    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delete__(pos)
            return None
        else:
            return pos


L = MyList()
L.append(10)
L.append(20)
L.append(30)
print(L.__str__())
print(L.__len__())

L.insert(2, 'hello')
print(L.__str__())
print(L.__len__())

#L.__delete__(2)
L.remove(20)
print(L.__str__())
print(L.__len__())
