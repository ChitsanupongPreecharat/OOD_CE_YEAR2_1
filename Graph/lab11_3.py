def create_graph(each_list):
    graph = {}
    for each in each_list:
        n1, dis, n2 = each.split()
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []
        graph[n1].append((n2, int(dis)))
    for node in graph:
        graph[node].sort()
    return graph

def dijkstra(graph, start, end):
    unvisited = set(graph.keys())
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    previous = {node: None for node in graph}

    while unvisited:
       
        current = None
        min_dist = float('inf')
        for node in unvisited:
            if distance[node] < min_dist:
                min_dist = distance[node]
                current = node

        if current is None: 
            break

        unvisited.remove(current)

        for neighbor, weight in graph[current]:
            if neighbor in unvisited:
                new_dist = distance[current] + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = current


    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = previous[node]

    if distance[end] == float('inf'):
        return None  

    return path


input_list, question = input("Enter : ").split('/')
input_list = input_list.split(',')
question = question.split(',')
graph = create_graph(input_list)

for q in question:
    start, end = q.split()
    if start not in graph or end not in graph:
        print(f"Not have path : {start} to {end}")
        continue
    path = dijkstra(graph, start, end)
    if path is None or len(path) == 0:
        print(f"Not have path : {start} to {end}")
    else:
        print(f"{start} to {end} : {'->'.join(path)}")
