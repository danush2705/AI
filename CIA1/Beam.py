import heapq

# Define the graph structure
graph_data = {
    'Start': {'NodeA': 6, 'NodeB': 5},  
    'NodeA': {'NodeB': 5, 'NodeD': 1},  
    'NodeB': {'NodeC': 8, 'NodeA': 6},
    'NodeC': {'NodeE': 9},
    'NodeD': {'NodeG': 2},  
    'NodeE': {},  
    'NodeG': {}   
}

# Heuristic values
heuristics = {
    'Start': 7,
    'NodeA': 6,
    'NodeB': 5,
    'NodeC': 8,
    'NodeD': 1,
    'NodeE': 9,
    'NodeG': 0
}

# Function to retrieve successors of the current node
def find_successors(graph_data, node):
    return graph_data[node].keys()

# Beam Search Algorithm
def beam_search_algorithm(graph_data, heuristics, start_node, target_node, beam_width=2):
    current_beam = [(heuristics[start_node], [start_node])] 
    
    while current_beam:
        next_beam = []
        
        for cost, path in current_beam:
            current_node = path[-1]
            
            if current_node == target_node:
                return path, cost
            
            for neighbor in find_successors(graph_data, current_node):
                if neighbor not in path: 
                    extended_path = path + [neighbor]
                    new_cost = cost + heuristics[neighbor]  
                    
                    next_beam.append((new_cost, extended_path))
        
        current_beam = heapq.nsmallest(beam_width, next_beam, key=lambda x: x[0])
        
    return None, float('inf')

start = 'Start'
goal = 'NodeG'
solution_path, path_cost = beam_search_algorithm(graph_data, heuristics, start, goal, beam_width=2)

print("Beam Search Solution Path:", solution_path)
print("Beam Search Path Cost:", path_cost)
