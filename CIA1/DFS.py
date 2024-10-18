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

def depth_first_search(graph_structure, current_node, target_node, visited_nodes=None, current_path=None):
    if visited_nodes is None:
        visited_nodes = set()  
    if current_path is None:
        current_path = []  
    
    visited_nodes.add(current_node)  
    current_path.append(current_node)  
    print(f"Exploring: {current_node}")

    if current_node == target_node:
        print(f"Target {target_node} found!")
        print("Path:", " -> ".join(current_path))
        return True 

    for neighbor in graph_structure[current_node]:
        if neighbor not in visited_nodes:
            if depth_first_search(graph_structure, neighbor, target_node, visited_nodes, current_path):  
                return True  

    current_path.pop()  
    return False  

depth_first_search(graph_structure, 'Start', 'NodeG')
