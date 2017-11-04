import random
import copy

graph = dict()
file = open('mincut.txt', 'r')
for line in file:
    a = line.split('\t')
    a.pop()
    graph[int(a[0])] = [int(node) for node in a[1:]]
# print(graph)

def contract_edge(graph, a, b):
    graph[a][:] = (value for value in graph[a] if value != b)
    graph[b][:] = (value for value in graph[b] if value != a)
    graph[a].extend(graph[b])
    del graph[b]
    for node in graph:
        for id, adj in enumerate(graph[node]):
            if adj == b:
                graph[node][id] = a

min_count = 1000
for i in range(200):
    # print(i)
    graph_copy = copy.deepcopy(graph)
    while (len(graph_copy) > 2):
        a = random.choice(list(graph_copy.keys()))
        b = graph_copy[a][random.randint(0, len(graph_copy[a]) - 1)]
        contract_edge(graph_copy, a, b)
    count = len(list(graph_copy.values())[0])
    if count < min_count:
        print("# of cuts: ", count)
        min_count = count