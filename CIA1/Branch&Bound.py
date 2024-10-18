import heapq

# Define the graph structure
graph_structure = {
    'Start': {'NodeA': 6, 'NodeB': 5},  
    'NodeA': {'NodeB': 5, 'NodeD': 1},  
    'NodeB': {'NodeC': 8, 'NodeA': 6},
    'NodeC': {'NodeE': 9},
    'NodeD': {'NodeG': 0},  
    'NodeE': {},  
    'NodeG': {}   
}

# Branch and Bound Algorithm
def branch_and_bound_search(graph_structure, start_node, target_node):
    priority_queue = [(0, start_node, [start_node])]  
    
    optimal_cost = float('inf')
    optimal_path = None
    
    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)
    
        if current_node == target_node and current_cost < optimal_cost:
            optimal_cost = current_cost
            optimal_path = path
        
        for neighbor, edge_weight in graph_structure[current_node].items():
            new_total_cost = current_cost + edge_weight
            
            if new_total_cost < optimal_cost:
                heapq.heappush(priority_queue, (new_total_cost, neighbor, path + [neighbor]))
    
    return optimal_path, optimal_cost

start = 'Start'
goal = 'NodeG'

solution_path, solution_cost = branch_and_bound_search(graph_structure, start, goal)

print("Optimal Path Found (Branch and Bound):", solution_path)
print("Total Path Cost:", solution_cost)
