import heapq

# Define the graph structure
graph_data = {
    'Start': {'NodeA': 6, 'NodeB': 5},  
    'NodeA': {'NodeB': 5, 'NodeD': 1},  
    'NodeB': {'NodeC': 8, 'NodeA': 6},
    'NodeC': {'NodeE': 9},
    'NodeD': {'NodeG': 0},  
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

# Best First Search Algorithm with cost calculation
def best_first_search_algorithm(start_node, target_node, graph_data, heuristics):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start_node], start_node, [start_node], 0))
    
    explored_nodes = set()
    
    while priority_queue:
        h_value, current_node, path, current_cost = heapq.heappop(priority_queue)
        
        if current_node == target_node:
            return path, current_cost
        
        explored_nodes.add(current_node)
        
        for neighbor, edge_weight in graph_data[current_node].items():
            if neighbor not in explored_nodes:
                new_cost = current_cost + edge_weight
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, path + [neighbor], new_cost))
    
    return None, None 

start = 'Start'
goal = 'NodeG'
solution_path, total_cost = best_first_search_algorithm(start, goal, graph_data, heuristics)

print("Best First Search Solution Path:", solution_path)
print("Total Cost:", total_cost)
