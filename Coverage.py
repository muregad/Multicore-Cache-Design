class Coverage:
    def __init__(self):

        # I ===> 0
        # S ===> 1
        # E ===> 2
        # M ===> 3

        self.uncovered = []
        self.uncovered2 = []
        self.uncovered.append([0, 0, 0, 2])
        self.uncovered.append([0, 0, 2, 0])
        self.uncovered.append([0, 2, 0, 0])
        self.uncovered.append([2, 0, 0, 0])
        self.uncovered.append([0, 0, 0, 3])
        self.uncovered.append([0, 0, 3, 0])
        self.uncovered.append([0, 3, 0, 0])
        self.uncovered.append([3, 0, 0, 0])

        for i in [0, 1]:
            for j in [0, 1]:
                for k in [0, 1]:
                    for m in [0, 1]:
                        if (i + j + k + m) != 1:
                            self.uncovered.append([i, j, k, m])

        for state in self.uncovered:
            for proc in range(4):
                ss = state.copy()
                ss.append(proc)
                for j in range(2):
                    sss = ss.copy()
                    sss.append(j)
                    self.uncovered2.append(sss)

        self.uncoveredMapping = {}
        self.uncoveredMapped = []
        cnt = 0
        for state in self.uncovered2:
            self.uncoveredMapping[self.lst_to_string(state)] = cnt
            self.uncoveredMapped.append(cnt)
            cnt += 1

        self.total = len(self.uncoveredMapped)


    def lst_to_string(self, lst):
        ss = ""
        for elmnt in lst:
            ss += str(int(elmnt))
        return ss

    def sample(self, state):
        encodedState = self.uncoveredMapping[self.lst_to_string(state)]
        if encodedState in self.uncoveredMapped:
            self.uncoveredMapped.remove(encodedState)
        return

    def get_coverage(self):
        return (1.0 - len(self.uncoveredMapped) / self.total) * 100.0

    def unCovered(self, state):
        return self.uncoveredMapping[self.lst_to_string(state)] in self.uncoveredMapped

#
# tst = Coverage()
#
#
# print(tst.uncoveredMapped)