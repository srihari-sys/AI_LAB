import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

GOAL_POSITIONS = {}
for r in range(3):
    for c in range(3):
        val = GOAL_STATE[r][c]
        if val != 0:
            GOAL_POSITIONS[val] = (r, c)

class Node:
    def __init__(self, state, parent=None, action=None, g=0):
        self.state = state        
        self.parent = parent      
        self.action = action      
        self.g = g                
        self.h = self.heuristic() 
        self.f = self.g + self.h 

    def heuristic(self):
        total_distance = 0
        for r in range(3):
            for c in range(3):
                tile = self.state[r][c]
                if tile != 0:
                    target_r, target_c = GOAL_POSITIONS[tile]
                    total_distance += abs(r - target_r) + abs(c - target_c)
        return total_distance

    def __lt__(self, other):
        return self.f < other.f

def find_blank(state):

    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def get_neighbors(node):
    neighbors = []
    r, c = find_blank(node.state)
    moves = {
        'UP': (r - 1, c),
        'DOWN': (r + 1, c),
        'LEFT': (r, c - 1),
        'RIGHT': (r, c + 1)
    }

    for action, (nr, nc) in moves.items():
        if 0 <= nr < 3 and 0 <= nc < 3:
            grid = [list(row) for row in node.state]
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            new_state = tuple(tuple(row) for row in grid)
            neighbors.append(Node(new_state, parent=node, action=action, g=node.g + 1))
            
    return neighbors

def solve_8_puzzle(initial_state):
    start_node = Node(initial_state)
    
    open_list = []
    heapq.heappush(open_list, start_node)
    
    g_costs = {initial_state: 0}

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == GOAL_STATE:
            path = []
            curr = current_node
            while curr:
                path.append(curr)
                curr = curr.parent
            return path[::-1]

        for neighbor in get_neighbors(current_node):
            if neighbor.state not in g_costs or neighbor.g < g_costs[neighbor.state]:
                g_costs[neighbor.state] = neighbor.g
                heapq.heappush(open_list, neighbor)

    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return

    print(f"Goal reached in {len(path) - 1} steps!\n")
    for step, node in enumerate(path):
        if step == 0:
            print("--- Initial State ---")
        else:
            print(f"--- Step {step}: Move Blank {node.action} ---")
            
        for row in node.state:
            print(" ".join(str(tile) if tile != 0 else "_" for tile in row))
        print(f"g = {node.g}, h = {node.h}, f = {node.f}")
        print()

if __name__ == "__main__":
    initial_state = (
        (0, 2, 3),
        (1, 5, 6),
        (4, 7, 8)
    )

    path = solve_8_puzzle(initial_state)
    print_solution(path)
