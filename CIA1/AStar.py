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

# A* Search Algorithm Function
def a_star_search(graph_data, heuristics, start_node, target_node):
    priority_queue = [(heuristics[start_node], 0, start_node, [start_node])]
    visited_nodes = {}
    
    while priority_queue:
        estimated_cost, current_cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == target_node:
            return path, current_cost
        
        if current_node in visited_nodes and visited_nodes[current_node] <= current_cost:
            continue
        
        visited_nodes[current_node] = current_cost
        
        for neighbor, edge_weight in graph_data[current_node].items():
            new_cost = current_cost + edge_weight 
            estimated_total_cost = new_cost + heuristics[neighbor] 
            
            heapq.heappush(priority_queue, (estimated_total_cost, new_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

start = 'Start'
goal = 'NodeG'

solution_path, total_cost = a_star_search(graph_data, heuristics, start, goal)

print("A* Algorithm Solution Path:", solution_path)
print("Total Path Cost:", total_cost)
