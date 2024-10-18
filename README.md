# CIA1
## AI Search Algorithms Implemented in Python

### 1. AOStar.py
- This script implements the AO* algorithm, which is designed for navigating through AND-OR graphs, making it useful for complex decision-making scenarios.
- **Key Features:**
    - Addresses intricate decision-making challenges.
    - Handles both AND and OR nodes effectively.

### 2. AStar.py
- This file contains the implementation of the A* algorithm, a well-known pathfinding and graph traversal technique recognized for its efficiency in determining the shortest path.
- **Key Features:**
    - Combines cost and heuristic assessments (f(n) = g(n) + h(n)).
    - Ensures the shortest path if the heuristic is admissible.

### 3. B&BCwCH.py (Branch and Bound with Cost and Heuristic)
- This implementation of the Branch and Bound algorithm leverages cost and heuristic values to minimize the search area.
- **Key Features:**
    - Merges cost analysis with heuristic strategies for effective pruning.

### 4. B&BwDHP.py (Branch and Bound with Dead Horse Principle)
- This variation of the Branch and Bound approach integrates the Dead Horse Principle, allowing for early elimination of unpromising paths.
- **Key Features:**
    - Facilitates early pruning of non-viable branches.

### 5. Beam.py
- This file implements the Beam Search algorithm, a heuristic-based search method that focuses on a fixed number of the most promising nodes at each level.
- **Key Features:**
    - Uses a defined beam width to restrict the search area.
    - Offers improved memory efficiency compared to exhaustive methods.

### 6. BestFS.py
- This script implements the Best-First Search algorithm, which prioritizes nodes based on a heuristic evaluation.
- **Key Features:**
    - Employs a priority queue to explore the most promising node first.

### 7. BFS.py (Breadth-First Search)
- This file features the Breadth-First Search algorithm, a foundational technique for graph traversal that examines all nodes at the current depth before advancing to the next level.
- **Key Features:**
    - Guarantees the discovery of the shortest path in unweighted graphs.
    - Explores neighbors systematically, level by level.
    - Applicable for both tree and graph traversal scenarios.

### 8. BMS.py (Beam Search)
- This implementation is a specific variant of Beam Search, emphasizing heuristic-driven exploration within a limited beam width.
- **Key Features:**
    - Conducts efficient searches while adhering to the constraints of beam width.

### 9. Branch&Bound.py
- This standard implementation of the Branch and Bound algorithm systematically evaluates all potential solutions while eliminating suboptimal paths.
- **Key Features:**
    - Guarantees identification of the optimal solution.
    - Reduces search time by pruning non-promising options.

### 10. DFS.py (Depth-First Search)
- A basic implementation of the Depth-First Search algorithm, a crucial technique for graph traversal.
- **Key Features:**
    - Explores each branch deeply before backtracking.

### 11. Hill_Climbing.py
- This script implements the Hill Climbing algorithm, a local search method that iteratively enhances the solution by selecting the neighbor with the highest value.
- **Key Features:**
    - May become trapped in local optima.
    - Effective for various optimization tasks.

### 12. Oracle.py
- A straightforward oracle-searching algorithm aimed at identifying the best solution for decision-making problems.
- **Key Features:**
    - Investigates the search space to uncover an optimal oracle.

# CIA2
## Gaming Adversarial Algorithms Implemented in Python

### 1. a-bPrune.py (Alpha-Beta Pruning)
- This script implements the Alpha-Beta Pruning technique, an optimization for the Minimax algorithm that decreases the number of nodes evaluated.
- **Key Features:**
    - Eliminates branches in the game tree that do not impact the final outcome.
    - More efficient than the traditional Minimax approach.
