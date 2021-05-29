from CPU import CPU
from random import randint
import numpy as np
from Coverage import Coverage
from Neuralnet import Neuralnet
import matplotlib.pyplot as plt
import csv
from Graph_RTL import Graph
from analyze_cov import *

# I ===> 0
# S ===> 1
# E ===> 2
# M ===> 3

def read_x_y(t): #To-Do ===> Read Input/Output CSVs (For Training NN)
    x_train = np.zeros((t, 6))
    y_train = np.zeros((t, 4))

    with open("x.csv", "r") as f:
        data = csv.reader(f)
        i = 0
        for row in data:
            x_train[i] = row
            i += 1

    with open("y.csv", "r") as f:
        data = csv.reader(f)
        i = 0
        for row in data:
            y_train[i] = row
            i += 1

    return x_train, y_train
#
# def read_covered():
#
#     with open("y.csv", "r") as f:
#         data = csv.reader(f)
#         i = 0
#         for row in data:
#             y_train[i] = row
#             i += 1



encode = {"I": 0, "S": 1, "E": 2, "M": 3}

num_of_cores = 4

cpu = CPU(num_of_cores=num_of_cores)
t = 250 #size Of trainig set

x = np.zeros((t, 6))
y = np.zeros((t, 4))


#The first few lines were used to generate the trainig test (Redundant)

# for i in range(t):
#     rest = np.random.randint(0, 8)
#
#     if rest == 7:
#         cpu.processors[0].Cache.reset()
#         cpu.processors[1].Cache.reset()
#         cpu.processors[2].Cache.reset()
#         cpu.processors[3].Cache.reset()
#
#     x[i, 0:4] = [encode[cpu.processors[0].Cache.getState(address=8)],
#                  encode[cpu.processors[1].Cache.getState(address=8)],
#                  encode[cpu.processors[2].Cache.getState(address=8)],
#                  encode[cpu.processors[3].Cache.getState(address=8)]]
#     processor = np.random.randint(0, 4)
#     r_w = np.random.randint(0, 2)
#     x[i, 4] = processor
#     x[i, 5] = r_w
#     # if(r_w == 2):
#     #     cpu.processors[0].Cache.reset()
#     #     cpu.processors[1].Cache.reset()
#     #     cpu.processors[2].Cache.reset()
#     #     cpu.processors[3].Cache.reset()
#     # else:
#     print(x[i, 0:4])
#     cvg.sample(x[i])
#     cvg_arr.append(cvg.get_coverage())
#     cpu.bus.instruction(processor=processor, r_w=r_w, address=8, value=randint(0, 15))
#     cpu.printStatus()
#     y[i] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)],
#             encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
#     print(y[i])
#     print("------------------------------")

# print(cvg.get_coverage())
# print(cvg.uncoveredMapped)
# print(x)
# print(y)
graph = Graph();

nn = Neuralnet(x, y, graph.allStates)


covered = getCoveredCrosses()

for state_transition in graph.allStatesTransactions:
    next_state = nn.pred(state_transition)
    print(f"{state_transition} {next_state}\n-------------------------------------")
    graph.add_edge(state_transition, next_state, 0) #Need to check if it works

graph.update_edge_weights(covered) #Generally update_edge_weights is used to update the weights

for i in range(200):

    #get uncoverd state_transition
    #shortes path
    #write the generarted sequence to a csv file
    #simulate the RTL with the sequence and analyze the coverage
    #Load the new covered
    #update weights

    state_transition = graph.getUncoveredState()

    transactions = graph.shortest_path(state_transition[0:4])

    if len(transactions) == 0:
        continue
    transactions.append([state_transition[5], state_transition[6]])
    covered = getCoveredCrosses()
    graph.update_edge_weights(covered)


# print(str(x[20]))
# print("x original is " + str(x[20]))
# print("neural net pred: " + str(nn.pred(x[20])))
# print("real no : " + str(y[20]))
