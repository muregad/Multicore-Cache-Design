

class Graph:

    def __init__(self, states_list):
        self.state_list = states_list
        self.encoding = {}
        self.encoded_list = []
        self.transitions = []
        self.transitions_encoding = {}
        self.transitions_encoded = []

        for i in range(4):
            for j in range(2):
                self.transitions.append([i, j])

        for i in range(len(self.transitions)):
            self.transitions_encoding[self.lst_to_string(self.transitions[i])] = i
            self.transitions_encoded.append(i)


        for i in range(len(states_list)):
            self.encoded_list.append(i)
            self.encoding[self.lst_to_string(self.state_list[i])] = i
        print(self.encoding)
        self.graph_arr = [[[], [], [], [], [], [], [], []] for i in range(len(self.state_list))]

    def lst_to_string(self, lst):
        ss = ""
        for elmnt in lst:
            ss += str(int(elmnt))
        return ss

    def add_edge(self, state_transition, next_state, edge_weight):
        ind1 = self.encoding[self.lst_to_string(state_transition[0:4])]
        ind2 = self.transitions_encoding[self.lst_to_string(state_transition[4:6])]
        dest = self.encoding[self.lst_to_string(next_state)]

        print(f"{ind1} {ind2} {dest}")
        self.graph_arr[ind1][ind2].append([dest, edge_weight])
        return

    def shortest_path(self, destination_node):
        pass


# g = Graph([[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1]])
#
# print(g.encoding)
# print(g.encoded_list)
# print(g.state_list)



