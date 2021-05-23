from random import randint
from math import log2


class L1Cache:

    def __init__(self, size, associativity, addressWidth):
        self.addressWidth = addressWidth
        self.associativity = associativity
        self.size = size
        self.CachedData = [[None for i in range(size // associativity)] for i in range(associativity)]
        self.CacheState = [["I" for i in range(size // associativity)] for i in range(associativity)]
        self.BlockTag = [[None for i in range(size // associativity)] for i in range(associativity)]

    def read(self, ReadAddress):
        readMiss = True
        RdAddress_bin = ("{0:0>%s}" % self.addressWidth).format(bin(ReadAddress & int("1" * self.addressWidth, 2))[2:])
        addressIndex = int(RdAddress_bin[-int(log2(self.associativity)):], 2)
        addressTag = int(RdAddress_bin[: self.addressWidth - int(log2(self.associativity))], 2)

        ReadData = None

        for i in range(self.size // self.associativity):
            if addressTag == self.BlockTag[addressIndex][i]:
                if self.CacheState[addressIndex][i] != "I":
                    ReadData = self.CachedData[addressIndex][i]
                    readMiss = False
                break

        return ReadData, readMiss

    def write(self, WriteAddress, WriteData):  # Take Care of the method of replacement in case of Conflicts
        RdAddress_bin = ("{0:0>%s}" % self.addressWidth).format(bin(WriteAddress & int("1" * self.addressWidth, 2))[2:])
        addressIndex = int(RdAddress_bin[-int(log2(self.associativity)):], 2)
        addressTag = int(RdAddress_bin[: self.addressWidth - int(log2(self.associativity))], 2)
        written = False
        for i in range(self.size // self.associativity):
            if addressTag == self.BlockTag[addressIndex][i]:
                self.CachedData[addressIndex][i] = WriteData
                written = True
                break

        if not written:
            full = True
            for i in range(self.size // self.associativity):
                if self.BlockTag[addressIndex][i] == None:
                    self.BlockTag[addressIndex][i] = addressTag
                    self.CachedData[addressIndex][i] = WriteData
                    full = False
                    break
            if full:
                randIdx = randint(0, (self.size // self.associativity) - 1)  # Need to write the value of the overthrown value to the main Memory if needed
                self.BlockTag[addressIndex][randIdx] = addressTag
                self.CachedData[addressIndex][randIdx] = WriteData
        return

    def getState(self, address):
        RdAddress_bin = ("{0:0>%s}" % self.addressWidth).format(bin(address & int("1" * self.addressWidth, 2))[2:])
        addressIndex = int(RdAddress_bin[-int(log2(self.associativity)):], 2)
        addressTag = int(RdAddress_bin[: self.addressWidth - int(log2(self.associativity))], 2)
        state = "I"
        for i in range(self.size // self.associativity):
            if addressTag == self.BlockTag[addressIndex][i]:
                state = self.CacheState[addressIndex][i]
                break

        return state

    def updateState(self, address, newState):
        RdAddress_bin = ("{0:0>%s}" % self.addressWidth).format(bin(address & int("1" * self.addressWidth, 2))[2:])
        addressIndex = int(RdAddress_bin[-int(log2(self.associativity)):], 2)
        addressTag = int(RdAddress_bin[: self.addressWidth - int(log2(self.associativity))], 2)

        for i in range(self.size // self.associativity):
            if addressTag == self.BlockTag[addressIndex][i]:
                self.CacheState[addressIndex][i] = newState
                break

        return


# testCache = L1Cache(size=8, associativity=4, addressWidth=8)
# testCache.write(WriteAddress=16, WriteData=6464)
# testCache.write(WriteAddress=20, WriteData=5152)
# print(testCache.CacheState)
# print(testCache.CachedData)
# testCache.write(WriteAddress=24, WriteData=232)
# testCache.updateState(16 , "E")
# print(testCache.CacheState)
# print(testCache.CachedData)
