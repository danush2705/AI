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

# Define heuristic values
heuristics = {
    'Start': 7,
    'NodeA': 6,
    'NodeB': 5,
    'NodeC': 8,
    'NodeD': 1,
    'NodeE': 9,
    'NodeG': 0
}

# Branch and Bound Algorithm with Heuristics
def branch_and_bound(graph_data, heuristics, start_node, target_node):
    priority_queue = [(0 + heuristics[start_node], 0, start_node, [start_node])]
    
    explored = {}
    
    optimal_cost = float('inf')
    optimal_path = None
    
    while priority_queue:
        estimated_cost, current_cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == target_node and current_cost < optimal_cost:
            optimal_cost = current_cost
            optimal_path = path
            continue
        
        if current_node in explored and explored[current_node] <= current_cost:
            continue 
        
        explored[current_node] = current_cost
        
        for neighbor, edge_weight in graph_data[current_node].items():
            new_cost = current_cost + edge_weight
            estimated_neighbor_cost = new_cost + heuristics[neighbor]
            
            if new_cost < optimal_cost:
                heapq.heappush(priority_queue, (estimated_neighbor_cost, new_cost, neighbor, path + [neighbor]))
    
    return optimal_path, optimal_cost

start = 'Start'
goal = 'NodeG'

solution_path, total_cost = branch_and_bound(graph_data, heuristics, start, goal)

print("Optimal Path Found (Branch and Bound with Heuristics):", solution_path)
print("Total Path Cost:", total_cost)
