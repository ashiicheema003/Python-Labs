graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {'-1', '4'},
    'E': {'2', '6'},
    'F': {'-3', '-5'},
    'G': {'0', '7'},
    '-1': {},
    '4': {},
    '2': {},
    '6': {},
    '-3': {},
    '-5': {},
    '0': {},
    '7': {}
}

def minimax(node, graph, max_func):
    if not graph[node]:  # Terminal condition (leaf node)
        return int(node)  # Directly return the node as an integer value
    
    if max_func:
        max_value = float('-inf')
        for child in graph[node]:
            value = minimax(child, graph, False)
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for child in graph[node]:
            value = minimax(child, graph, True)
            min_value = min(min_value, value)
        return min_value    

# Run Minimax Algorithm
result = minimax('A', graph, True)
print("The optimal value is:", result)
