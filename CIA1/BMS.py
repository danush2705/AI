# Define the graph structure
graph_structure = {
    'Start': ['NodeA', 'NodeB'],
    'NodeA': ['NodeB', 'NodeD'],
    'NodeB': ['NodeC', 'NodeA'],
    'NodeC': ['NodeE'],
    'NodeD': ['NodeG'],
    'NodeE': [],
    'NodeG': []
}

def find_all_paths(graph_structure, current_node, target_node, current_path=[]):
    current_path = current_path + [current_node]
    
    if current_node == target_node:
        return [current_path]
    
    if current_node not in graph_structure:
        return []
    
    possible_paths = []
    
    for neighbor in graph_structure[current_node]:
        if neighbor not in current_path:
            new_paths = find_all_paths(graph_structure, neighbor, target_node, current_path)
            possible_paths.extend(new_paths)
    
    return possible_paths

start_node = 'Start'
goal_node = 'NodeG'
all_possible_paths = find_all_paths(graph_structure, start_node, goal_node)

print("All Possible Paths from", start_node, "to", goal_node, ":")
for path in all_possible_paths:
    print(path)
