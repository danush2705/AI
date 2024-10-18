import math

# Define the graph as a dictionary
graph_structure = {
    'Start': {'NodeA': 6, 'NodeB': 5},  
    'NodeA': {'NodeB': 5, 'NodeD': 1},  
    'NodeB': {'NodeC': 8, 'NodeA': 6},
    'NodeC': {'NodeE': 9},
    'NodeD': {'NodeG': 2},  
    'NodeE': {},  
    'NodeG': {}   
}

# Heuristic values for each node
heuristic_values = {
    'Start': 7,
    'NodeA': 6,
    'NodeB': 5,
    'NodeC': 8,
    'NodeD': 1,
    'NodeE': 9,
    'NodeG': 0
}

# AO* algorithm implementation
def ao_star_algorithm(current_node, graph_structure, heuristic_values, target, visited_nodes):
    if current_node == target:
        return 0, [target]
    
    if current_node in visited_nodes:
        return math.inf, []
    
    visited_nodes.add(current_node)
    
    minimum_cost = math.inf
    optimal_path = []

    for neighbor, cost in graph_structure[current_node].items():
        cost_of_subtree, path_of_subtree = ao_star_algorithm(neighbor, graph_structure, heuristic_values, target, visited_nodes)
        total_cost = cost + cost_of_subtree

        if total_cost < minimum_cost:
            minimum_cost = total_cost
            optimal_path = [current_node] + path_of_subtree
    
    visited_nodes.remove(current_node)

    return minimum_cost, optimal_path

def execute_ao_star(start, goal):
    visited_nodes = set()
    total_cost, path_to_solution = ao_star_algorithm(start, graph_structure, heuristic_values, goal, visited_nodes)
    return path_to_solution, total_cost

initial_node = 'Start'
target_node = 'NodeG'
solution_path, total_cost = execute_ao_star(initial_node, target_node)

print("AO* Solution Path:", solution_path)
print("Total Cost to Goal:", total_cost)
