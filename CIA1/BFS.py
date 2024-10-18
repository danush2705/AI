from collections import deque

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

def breadth_first_search(graph_structure, start_node, target_node):
    visited_nodes = set()  
    search_queue = deque([(start_node, [start_node])])
    
    while search_queue:
        current_node, path = search_queue.popleft()
        print(f"Exploring: {current_node}")

        if current_node == target_node:
            print(f"Target {target_node} found!")
            print("Path:", " -> ".join(path))
            return True  

        if current_node not in visited_nodes:
            visited_nodes.add(current_node)  

            for neighbor in graph_structure[current_node]:
                if neighbor not in visited_nodes:
                    search_queue.append((neighbor, path + [neighbor])) 
                    
    print("Target not found")
    return False 

breadth_first_search(graph_structure, 'Start', 'NodeG')
