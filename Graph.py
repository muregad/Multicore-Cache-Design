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
        # print(self.encoding)
        self.graph_arr = [[None, None, None, None, None, None, None, None] for i in range(len(self.state_list))]
        self.graph_wights = [[None, None, None, None, None, None, None, None] for i in range(len(self.state_list))]

    def lst_to_string(self, lst):
        ss = ""
        for elmnt in lst:
            ss += str(int(elmnt))
        return ss

    def update_edge_weights(self, cvg):
        for state_transition in cvg.uncovered2:
            edge_weight = 1
            if cvg.unCovered(state_transition):
                edge_weight = 0
            ind1 = self.encoding[self.lst_to_string(state_transition[0:4])]
            ind2 = self.transitions_encoding[self.lst_to_string(state_transition[4:6])]
            self.graph_wights[ind1][ind2] = edge_weight
        return
    def add_edge(self, state_transition, next_state, edge_weight):
        ind1 = self.encoding[self.lst_to_string(state_transition[0:4])]
        ind2 = self.transitions_encoding[self.lst_to_string(state_transition[4:6])]
        dest = self.encoding[self.lst_to_string(next_state)]
        self.graph_wights[ind1][ind2] = edge_weight
        self.graph_arr[ind1][ind2] = dest
        return

    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = 100000000

        # Search not nearest vertex not in the
        # shortest path tree
        min_index = -1
        for v in range(len(self.state_list)):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def shortest_path(self, destination_node):
        source_node = self.encoding[self.lst_to_string([0, 0, 0, 0])]
        dist = [100000000 for i in range(len(self.state_list))]
        dist[source_node] = 0
        sptSet = [False] * len(self.state_list)
        path = [[]] * len(self.state_list)

        for i in range(len(self.state_list)):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            j = 0
            for idx in range(len(self.graph_arr[u])):
                # print(self.graph_arr[u])
                # print(self.graph_wights[u])
                if self.graph_arr[u][idx] is not None:
                    dest = self.graph_arr[u][idx]
                    edge_weight = self.graph_wights[u][idx]

                    # print(f"{dest} {edge_weight}")
                    if sptSet[dest] == False and dist[u] + edge_weight < dist[dest]:
                        # print(f"{dist[dest]} {dist[u]} {u} {edge_weight}")
                        lst = path[u].copy()
                        lst.append(self.transitions[j])
                        path[dest] = lst.copy()
                        dist[dest] = dist[u] + edge_weight

                j = j + 1

        return path[self.encoding[self.lst_to_string(destination_node)]]

#
# g = Graph([[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1], [0,1,0,0], [0,1,0,1], [0,1,1,0],[0,1,1,1]])
#
# g.add_edge([0,0,0,0,0,0], [0,0,0,1] , 1)
# g.add_edge([0,0,0,1,0,1], [0,0,1,0] , 1)
# g.add_edge([0,0,1,0,1,0], [0,0,1,1] , 1)
# g.add_edge([0,0,1,1,0,1], [0,1,0,0] , 1)
# g.add_edge([0,1,0,0,1,1], [0,1,0,1] , 1)
# g.add_edge([0,1,0,1,0,0], [0,1,1,0] , 1)
# g.add_edge([0,1,1,0,1,0], [0,1,1,1] , 1)
#
#
# # print(g.graph_arr)
# # print(g.graph_wights)
# # #
# print(g.shortest_path([0,1,1,1]))
# #
# # print(dist)
# print(g.state_list[6])
# print(path[6])
# print(dist[6])
# # g.shortest_path(5)
# print(g.encoding)
# print(g.encoded_list)
# print(g.state_list)
#
