def create_graph(edge_list):
    graph = {}
    for edge in edge_list:
        a,b = edge.split()
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    for node in graph:
        graph[node].sort()
    return graph

def dfs(graph,start):
    visit = set()
    result = []
    
    def _dfs(v):
        visit.add(v)
        result.append(v)
        for neighbor in sorted(graph.get(v, [])):
            if neighbor not in visit:
                _dfs(neighbor)
    
    _dfs(start)
    
    for node in sorted(graph.keys()):
        if node not in visit:
            _dfs(node)
    
    return result


def bfs(graph, start):
    visited = set()
    queue = [start]
    result = [start]
    visited.add(start)

    while queue:
        v = queue.pop(0)
        for neighbor in sorted(graph.get(v, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                result.append(neighbor)

    
    for node in sorted(graph.keys()):
        if node not in visited:
            visited.add(node)
            queue.append(node)
            result.append(node)
            while queue:
                v = queue.pop(0)
                for neighbor in sorted(graph.get(v, [])):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        result.append(neighbor)

    return result
    
input_list = input("Enter : ").split(',')
graph = create_graph(input_list)


start = min(graph.keys())
dfs_result = dfs(graph,start)
print(f"Depth First Traversals : {' '.join(dfs_result)}")
bfs_result = bfs(graph,start)
print(f"Bredth First Traversals : {' '.join(bfs_result)}")