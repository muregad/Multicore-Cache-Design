from random import randint


class Memory:

    def __init__(self, addressWidth):
        self.data = [randint(0, 1000) for i in range(2 ** addressWidth)]

    def read(self, ReadAddress):
        return self.data[ReadAddress]

    def write(self, WriteAddress, WriteData):
        self.data[WriteAddress] = WriteData


# mem = Memory(addressWidth=2)
# print(mem.data)
#
# print(mem.read(0))
# print(mem.data)
# print(mem.read(3))
# print(mem.data)
# mem.write(0, 12)
# print(mem.data)
# print(mem.read(0))
