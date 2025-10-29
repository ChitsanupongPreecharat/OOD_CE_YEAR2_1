def create_graph(each_list):
    graph = {}
    for each in each_list:
        a, b = each.split()
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
    return graph

def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


each_list = input("Enter : ").split(',')
graph = create_graph(each_list)

if has_cycle(graph):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
