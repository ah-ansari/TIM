import numpy as np
import tools
import TIM
import time

start_time = time.time()

k = 25
data_set = "datasets/"+"p2p-Gnutella08.txt"
is_directed = True

file = open("graph/result.txt", "w")
file.write("data set:" + data_set + "\n")
file.write("is_directed: " + str(is_directed) + "\n")
file.write("k: " + str(k) + "\n")


def load_graph():
    if is_directed:
        g = tools.load_graph_directed(data_set)
    else:
        g = tools.load_graph_undirected(data_set)
    return g


g = load_graph()
theta = TIM.calculate_theta(g, k)
file.write("theta: " + str(theta) + "\n")

g = load_graph()
seed_set = TIM.node_selection(g, k, theta)
np.savetxt("graph/seed_set.txt", seed_set)
file.close()

end_time = time.time()
print(data_set)
print("time: "+str(end_time-start_time))
