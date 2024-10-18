import math

def alpha_beta_search(current_depth, index, is_max_player, leaf_values, alpha, beta, max_depth):
    # Check if we have reached a terminal node
    if current_depth == max_depth:
        print(f"Reached leaf at depth {current_depth}, returning value: {leaf_values[index]}")
        return leaf_values[index]

    if is_max_player:
        best_value = -math.inf
        print(f"Max player at depth {current_depth}, alpha: {alpha}, beta: {beta}")
        
        for i in range(2):
            evaluated_value = alpha_beta_search(current_depth + 1, index * 2 + i, False, leaf_values, alpha, beta, max_depth)
            print(f"Max player at depth {current_depth}, evaluating value: {evaluated_value} against best: {best_value}")
            best_value = max(best_value, evaluated_value)
            alpha = max(alpha, best_value)
            print(f"Max player updated alpha: {alpha}")

            # Prune the tree
            if beta <= alpha:
                print(f"Pruning at max node at depth {current_depth}, alpha: {alpha}, beta: {beta}")
                break
        
        print(f"Max player at depth {current_depth}, selected best value: {best_value}")
        return best_value
    else:
        best_value = math.inf
        print(f"Min player at depth {current_depth}, alpha: {alpha}, beta: {beta}")

        for i in range(2):
            evaluated_value = alpha_beta_search(current_depth + 1, index * 2 + i, True, leaf_values, alpha, beta, max_depth)
            print(f"Min player at depth {current_depth}, evaluating value: {evaluated_value} against best: {best_value}")
            best_value = min(best_value, evaluated_value)
            beta = min(beta, best_value)
            print(f"Min player updated beta: {beta}")

            # Prune the tree
            if beta <= alpha:
                print(f"Pruning at min node at depth {current_depth}, alpha: {alpha}, beta: {beta}")
                break
        
        print(f"Min player at depth {current_depth}, selected best value: {best_value}")
        return best_value

# Define the maximum depth of the game tree
max_depth = 3

# Leaf node values
leaf_values = [-1, 4, 2, 6, -3, -5, 0, 7]

# Initialize alpha and beta
alpha_initial = -math.inf
beta_initial = math.inf

# Execute the alpha-beta pruning algorithm
optimal_result = alpha_beta_search(0, 0, True, leaf_values, alpha_initial, beta_initial, max_depth)

print("\nThe optimal value is:", optimal_result)
