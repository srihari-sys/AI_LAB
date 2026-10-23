def calculate_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_best_neighbor(current_state):
    n = len(current_state)
    best_state = None
    min_cost = float('inf')
    best_swap = None

    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(current_state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            
            cost = calculate_cost(neighbor)
            
            print(f"  Swap (x_{i}, x_{j}) -> {neighbor} | Cost: {cost}")
            
            if cost < min_cost:
                min_cost = cost
                best_state = neighbor
                best_swap = (i, j)

    return best_state, min_cost, best_swap

def hill_climbing(initial_state):
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    step = 1

    print("=" * 55)
    print(f"INITIAL STATE: {current_state} | Cost: {current_cost}")
    print("=" * 55)

    while True:
        if current_cost == 0:
            print("\nGoal state reached!")
            break

        print(f"\n--- STEP {step} ---")
        print(f"Current State: {current_state} | Cost: {current_cost}")
        print("Evaluating Neighbors:")
        
        best_neighbor, neighbor_cost, best_swap = get_best_neighbor(current_state)

        if neighbor_cost >= current_cost:
            print(f"\nAlgorithm terminated: Local maximum reached at state {current_state}.")
            break

        print(f"\n-> Chosen Swap: (x_{best_swap[0]}, x_{best_swap[1]})")
        print(f"-> Moving to State: {best_neighbor} with Cost: {neighbor_cost}")

        current_state = best_neighbor
        current_cost = neighbor_cost
        step += 1

    print("=" * 55)
    print(f"FINAL STATE: {current_state} | Cost: {current_cost}")
    print("=" * 55)
    return current_state


if __name__ == "__main__":
    initial_state = [3, 1, 2, 0] 
    hill_climbing(initial_state)
