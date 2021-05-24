from Memory import Memory
from BUS import Bus
from Processor import Processor


class CPU:

    def __init__(self, num_of_cores):
        self.memory = Memory(addressWidth=8)
        self.bus = Bus(self.memory)
        self.processors = []

        for i in range(num_of_cores):
            self.processors.append(Processor(Bus=self.bus, size=8, associativity=4, addressWidth=8))

    def printStatus(self):

        if self.bus.instruction_processor != None:
            if self.bus.instruction_type == 0:
                print("Instruction -> Processor_" + str(self.bus.instruction_processor) + " reads from address:" + str(self.bus.instruction_address))
            else:
                print("Instruction -> Processor_" + str(self.bus.instruction_processor) + " writes " + "value:" + str(
                    self.bus.instruction_value) + " to address:" + str(self.bus.instruction_address))
            # for i in range(4):
            #     print(self.processors[i].Cache.CacheState)
            # print("----------------------------------")

        # print(" ")
        # for processor in range(len(self.bus.processors)):
        #     print("Processor number: " + str(processor))
        #     print("Cache State: " + self.bus.processors[processor].cache.state)
        #
        #     if (self.bus.processors[processor].cache.address == null):
        #         print("Cache memory address: " + "empty")
        #     else:
        #         print("Cache memory address: " + str(self.bus.processors[processor].cache.address))
        #
        #     if (self.bus.processors[processor].cache.value == null):
        #         print("Cache memory value: " + "empty")
        #     else:
        #         print("Cache memory value: " + str(self.bus.processors[processor].cache.value))
        #
        #     print(" ")
