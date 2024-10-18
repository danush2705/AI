import heapq

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

# Function to determine the least-cost path
def least_cost_path(graph_structure, start_node, target_node):
    priority_queue = [(0, start_node, [start_node])] 
    
    costs = {node: float('inf') for node in graph_structure}
    costs[start_node] = 0
    
    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == target_node:
            return path, current_cost
        
        for neighbor, edge_cost in graph_structure[current_node].items():
            total_cost = current_cost + edge_cost
            
            if total_cost < costs[neighbor]:
                costs[neighbor] = total_cost
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

start = 'Start'
goal = 'NodeG'

result_path, result_cost = least_cost_path(graph_structure, start, goal)

print("Least Cost Path:", result_path)
print("Total Cost:", result_cost)
