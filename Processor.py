from L1Cache import L1Cache


class Processor:

    def __init__(self, Bus, size, associativity, addressWidth):
        self.Bus = Bus
        self.Bus.processors.append(self)
        self.Cache = L1Cache(size, associativity, addressWidth)

    def procRead(self, address):
        ReadData, readMiss = self.Cache.read(address)
        return readMiss

    def procWrite(self, address, value):
        self.Cache.write(address, value)

