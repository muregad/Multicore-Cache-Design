from CPU import CPU
from random import randint
import numpy as np
from Coverage import Coverage
from Neuralnet import Neuralnet
from Graph import Graph
import matplotlib.pyplot as plt

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
cvg_arr = []
for i in range(t):
    rest = np.random.randint(0, 8)

    if rest == 7:
        cpu.processors[0].Cache.reset()
        cpu.processors[1].Cache.reset()
        cpu.processors[2].Cache.reset()
        cpu.processors[3].Cache.reset()

    x[i, 0:4] = [encode[cpu.processors[0].Cache.getState(address=8)],
                 encode[cpu.processors[1].Cache.getState(address=8)],
                 encode[cpu.processors[2].Cache.getState(address=8)],
                 encode[cpu.processors[3].Cache.getState(address=8)]]
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
    print(x[i, 0:4])
    cvg.sample(x[i])
    cvg_arr.append(cvg.get_coverage())
    cpu.bus.instruction(processor=processor, r_w=r_w, address=8, value=randint(0, 15))
    cpu.printStatus()
    y[i] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)],
            encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
    print(y[i])
    print("------------------------------")

# print(cvg.get_coverage())
# print(cvg.uncoveredMapped)
# print(x)
# print(y)
nn = Neuralnet(x, y, cvg.uncovered)

graph = Graph(cvg.uncovered)

for state_transition in cvg.uncovered2:
    next_state = nn.pred(state_transition)
    print(f"{state_transition} {next_state}\n-------------------------------------")
    edge_weight = 1
    if cvg.unCovered(state_transition):
        edge_weight = 0

    graph.add_edge(state_transition, next_state, edge_weight)

for i in range(200):

    cpu.processors[0].Cache.reset()
    cpu.processors[1].Cache.reset()
    cpu.processors[2].Cache.reset()
    cpu.processors[3].Cache.reset()

    if len(cvg.uncoveredMapped) == 0:
        print(cvg.get_coverage())
        break
    state_transition = cvg.uncovered2[cvg.uncoveredMapped[np.random.randint(0, len(cvg.uncoveredMapped))]]
    transactions = graph.shortest_path(state_transition[0:4])
    print(f"destination: {state_transition} Source: {[cpu.processors[0].Cache.getState(8), cpu.processors[1].Cache.getState(8), cpu.processors[2].Cache.getState(8), cpu.processors[3].Cache.getState(8)]} Transaction: {transactions}")
    if len(transactions) == 0:
        continue

    for proc_num, r_w in transactions:
        cvg.sample([encode[cpu.processors[0].Cache.getState(address=8)],
                    encode[cpu.processors[1].Cache.getState(address=8)],
                    encode[cpu.processors[2].Cache.getState(address=8)],
                    encode[cpu.processors[3].Cache.getState(address=8)],
                    proc_num, r_w])
        cpu.bus.instruction(processor=proc_num, r_w=r_w, address=8, value=15)

    cvg.sample([encode[cpu.processors[0].Cache.getState(address=8)],
                encode[cpu.processors[1].Cache.getState(address=8)],
                encode[cpu.processors[2].Cache.getState(address=8)],
                encode[cpu.processors[3].Cache.getState(address=8)],
                state_transition[4], state_transition[5]])
    cpu.bus.instruction(processor=state_transition[4], r_w=state_transition[5], address=8, value=15)
    graph.update_edge_weights(cvg)
    cvg_arr.append(cvg.get_coverage())

random_cvg = []
cvg_random = Coverage()
cpu_random = CPU(num_of_cores=4)

for i in range(10000):
    # print(i)
    if(cvg_random.get_coverage() == 100):
        break
    rest = np.random.randint(0, 8)

    if rest == 7:
        cpu_random.processors[0].Cache.reset()
        cpu_random.processors[1].Cache.reset()
        cpu_random.processors[2].Cache.reset()
        cpu_random.processors[3].Cache.reset()
    tmp = [0]*6
    tmp[0:4] = [encode[cpu_random.processors[0].Cache.getState(address=8)],
                 encode[cpu_random.processors[1].Cache.getState(address=8)],
                 encode[cpu_random.processors[2].Cache.getState(address=8)],
                 encode[cpu_random.processors[3].Cache.getState(address=8)]]
    processor = np.random.randint(0, 4)
    r_w = np.random.randint(0, 2)
    tmp[4] = processor
    tmp[5] = r_w
    # if(r_w == 2):
    #     cpu.processors[0].Cache.reset()
    #     cpu.processors[1].Cache.reset()
    #     cpu.processors[2].Cache.reset()
    #     cpu.processors[3].Cache.reset()
    # else:
    cvg_random.sample(tmp)
    random_cvg.append(cvg_random.get_coverage())
    cpu_random.bus.instruction(processor=processor, r_w=r_w, address=8, value=randint(0, 15))



plt.plot(range(1, len(random_cvg)+1), random_cvg, range(1, len(cvg_arr)+1), cvg_arr)
plt.show()

# print(str(x[20]))
# print("x original is " + str(x[20]))
# print("neural net pred: " + str(nn.pred(x[20])))
# print("real no : " + str(y[20]))
