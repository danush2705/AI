import random

# Define the graph structure
graph_structure = {
    'Start': {'NodeA': 6, 'NodeB': 5},  
    'NodeA': {'NodeB': 5, 'NodeD': 1},  
    'NodeB': {'NodeC': 8, 'NodeA': 6},
    'NodeC': {'NodeE': 9},
    'NodeD': {'NodeG': 2},  
    'NodeE': {},  
    'NodeG': {}   
}

# Heuristic values
heuristic_values = {
    'Start': 7,
    'NodeA': 6,
    'NodeB': 5,
    'NodeC': 8,
    'NodeD': 1,
    'NodeE': 9,
    'NodeG': 0
}

def greedy_step(graph_structure, heuristic_values, start_node, target_node):
    current_node = start_node
    path = [current_node]
    
    while current_node != target_node:
        neighbors = graph_structure[current_node]
        if not neighbors:
            break
        next_node = min(neighbors, key=lambda n: heuristic_values[n])
        if next_node not in path:  # Avoid cycles
            path.append(next_node)
        current_node = next_node
    
    return path

def calculate_path_cost(heuristic_values, path):
    return sum([heuristic_values[node] for node in path])

def generate_path_neighbors(path):
    neighbors = []
    for i in range(1, len(path) - 1):  # Exclude start and goal
        for j in range(i + 1, len(path) - 1):
            new_neighbor = path.copy()
            new_neighbor[i], new_neighbor[j] = new_neighbor[j], new_neighbor[i]  # Swap nodes
            neighbors.append(new_neighbor)
    return neighbors

def find_best_neighbor(graph_structure, heuristic_values, current_path):
    neighbors = generate_path_neighbors(current_path)
    
    best_neighbor = current_path
    best_cost = calculate_path_cost(heuristic_values, current_path)
    
    for neighbor in neighbors:
        neighbor_cost = calculate_path_cost(heuristic_values, neighbor)
        if neighbor_cost < best_cost:
            best_cost = neighbor_cost
            best_neighbor = neighbor
    
    return best_neighbor, best_cost

# Hill Climbing Algorithm
def hill_climbing_algorithm(graph_structure, heuristic_values, start_node, target_node):
    current_path = greedy_step(graph_structure, heuristic_values, start_node, target_node)
    current_cost = calculate_path_cost(heuristic_values, current_path)
    
    while True:
        neighbor, neighbor_cost = find_best_neighbor(graph_structure, heuristic_values, current_path)
        
        if neighbor_cost >= current_cost:
            print(f"Reached local optimum at {current_path} with cost {current_cost}")
            break
        
        current_path = neighbor
        current_cost = neighbor_cost
    
    return current_path, current_cost

start_node = 'Start'
target_node = 'NodeG'
final_solution, final_cost = hill_climbing_algorithm(graph_structure, heuristic_values, start_node, target_node)

print("Final Solution Path:", final_solution)
print("Final Path Cost:", final_cost)
