# This program is for Dijkstra
graph = {}
graph['s'] = {}
graph['s']['a'] = 3
graph['s']['b'] = 4
graph['s']['c'] = 2
graph['a'] = {}
graph['a']['d'] = 3
graph['b'] = {}
graph['b']['a'] = 1
graph['c'] = {}
graph['c']['b'] = 1
graph['c']['d'] = 5

time = {}
time['a'] = 3
time['b'] = 4
time['c'] = 2
time['d'] = float('inf')

road = {}
road['a'] = 's'
road['b'] = 's'
road['c'] = 's'
road['d'] = None

flag = []

def find_least_time_node(time):
    least_time = float('inf')
    least_time_node = None
    for node in time:
        if time[node] < least_time and node not in flag:
            least_time = time[node]
            least_time_node = node
    return least_time_node, least_time


for i in range(3):
    node, least_time = find_least_time_node(time)
    nb = graph[node]
    for nb_node in nb.keys():
        t_time = least_time + nb[nb_node]
        if time[nb_node] > t_time:
            time[nb_node] = t_time
            road[nb_node] = node
    flag.append(node)
print('最短时间为：', time['d'])

road_line = []
road_line.append('d')
t_node = road['d']
road_line.append(t_node)
while road[t_node] != 's':
    t_node = road['t_node']
    road_line.append(t_node)
road_line.append('s')
road_line.reverse()

print('最短时间路径为：',end='')
for i in range(len(road_line)):
    if road_line[i] != 'd':
        print(road_line[i],"->",end='')
    else:
        print('d')
