
class Bus:

    def __init__(self, Memory):
        self.Memory = Memory
        self.processors = []
        self.instruction_processor = None
        self.instruction_type = None
        self.instruction_address = None
        self.instruction_value = None

    def instruction(self, processor, r_w, address, value):
        self.instruction_processor = processor
        self.instruction_address = address
        self.instruction_value = value
        self.instruction_type = r_w

        if r_w == 0: # Reading
            readMiss = self.processors[processor].procRead(address)

            if readMiss:
                flag = 0
                for proc in range(len(self.processors)):
                    if proc != processor:
                        if self.processors[proc].Cache.getState(address) == "M":
                            self.Memory.write(address, self.processors[proc].Cache.read(address)[0])
                            self.processors[proc].Cache.updateState(address, "S")
                            flag = 1
                        elif self.processors[proc].Cache.getState(address) == "E":
                            self.processors[proc].Cache.updateState(address, "S")
                            flag = 1
                        elif self.processors[proc].Cache.getState(address) == "S":
                            self.processors[proc].Cache.updateState(address, "S")
                            flag = 1

                self.processors[processor].procWrite(address, self.Memory.read(address))
                if flag == 1:
                    self.processors[processor].Cache.updateState(address, "S")
                else:
                    self.processors[processor].Cache.updateState(address, "E")

        else: # Writing
            self.processors[processor].procWrite(address, value)
            for proc in range(len(self.processors)):
                if proc != processor:
                    self.processors[proc].Cache.updateState(address, "I")
                else:
                    self.processors[proc].Cache.updateState(address, "M")
        return
