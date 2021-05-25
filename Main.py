from CPU import CPU
from random import randint
import numpy as np
from Coverage import Coverage
from Neuralnet import Neuralnet
from Graph import Graph
# I ===> 0
# S ===> 1
# E ===> 2
# M ===> 3


encode = {"I": 0, "S": 1, "E": 2, "M": 3}


num_of_cores = 4

cpu = CPU(num_of_cores=num_of_cores)
t = 250

x = np.zeros((t, 6))
y = np.zeros((t, 4))
cvg = Coverage()
for i in range(t):
    x[i, 0:4] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)], encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
    processor = np.random.randint(0, 4)
    r_w = np.random.randint(0, 2)
    x[i, 4] = processor
    x[i, 5] = r_w
    # if(r_w == 2):
    #     cpu.processors[0].Cache.reset()
    #     cpu.processors[1].Cache.reset()
    #     cpu.processors[2].Cache.reset()
    #     cpu.processors[3].Cache.reset()
    # else:
    print(x[i,0:4])
    cvg.sample(x[i])
    print(f"Iteration {i} ===> Coverage: {cvg.get_coverage()}")
    cpu.bus.instruction(processor=processor, r_w=r_w, address=8, value=randint(0, 15))
    cpu.printStatus()
    y[i] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)], encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
    print(y[i])
    print("------------------------------")

# print(cvg.get_coverage())
# print(cvg.uncoveredMapped)
# print(x)
# print(y)
nn= Neuralnet(x, y)

graph = Graph(cvg.uncovered)

for state_transition in cvg.uncovered2:
    next_state = nn.pred(state_transition)
    print(f"{state_transition} {next_state[0]}\n-------------------------------------")

    graph.add_edge(state_transition, next_state[0], 1)

print(f"Graph arr : {graph.graph_arr}")

# print(str(x[20]))
# print("x original is " + str(x[20]))
# print("neural net pred: " + str(nn.pred(x[20])))
# print("real no : " + str(y[20]))
