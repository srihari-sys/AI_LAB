def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3) 
    
    moves = {
        'RIGHT': (row, col + 1),
        'LEFT': (row, col - 1),
        'RIGHT': (row, col + 1),
        'UP': (row - 1, col),
        'DOWN': (row + 1, col),
    }
    
    for action, (r, c) in moves.items():
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), action))
            
    return neighbors

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()
    
    while stack:
        current, path = stack.pop()
        
        if current == goal_state:
            return path
            
        if current not in visited:
            visited.add(current)
            
            for neighbor, action in reversed(get_neighbors(current)):
                if neighbor not in visited:
                    stack.append((neighbor, path + [action]))
                    
    return None

def depth_limited_search(start_state, goal_state, limit):
    stack = [(start_state, [], 0)]
    visited = {start_state: 0} 
    cutoff_occurred = False
    
    while stack:
        current, path, depth = stack.pop()
        
        if current == goal_state:
            return path
            
        if depth == limit:
            cutoff_occurred = True
            continue
            
        for neighbor, action in reversed(get_neighbors(current)):
            if neighbor not in visited or visited[neighbor] > depth + 1:
                visited[neighbor] = depth + 1
                stack.append((neighbor, path + [action], depth + 1))
                
    return "CUTOFF" if cutoff_occurred else None

def ids(start_state, goal_state, max_depth=50):
    for limit in range(max_depth):
        result = depth_limited_search(start_state, goal_state, limit)
        if result != "CUTOFF" and result is not None:
            return result
    return None

if __name__ == "__main__":
    initial = (1, 2, 3, 
               4, 5, 6, 
               0, 7, 8)
               
    goal = (1, 2, 3, 
            4, 5, 6, 
            7, 8, 0)
    
    print("Initial State:", initial)
    print("Goal State:", goal)
    
    print("\nRunning DFS...")
    dfs_path = dfs(initial, goal)
    if dfs_path is not None or len(dfs_path)==0:
        print(f"DFS Solution found in {len(dfs_path)} moves.")
        print("Path:", dfs_path)
    else:
        print("DFS could not find a solution.")
        
    print("\nRunning IDS...")
    ids_path = ids(initial, goal)
    if ids_path is not None or len(ids_path)==0:
        print(f"IDS Solution found in {len(ids_path)} moves.")
        print("Path:", ids_path)
    else:
        print("IDS could not find a solution.")
