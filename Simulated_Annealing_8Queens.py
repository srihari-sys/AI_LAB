import math
import random

def calculate_cost(state):
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def get_random_neighbour(state):
    next_state = list(state)
    col = random.randint(0, len(state) - 1)
    new_row = random.randint(0, len(state) - 1)
    while new_row == state[col]:
        new_row = random.randint(0, len(state) - 1)
    next_state[col] = new_row
    return next_state, col, new_row

def print_grid(state, title=""):
    n = len(state)
    if title:
        print(title)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

def simulated_annealing(initial_state, T_init=10.0, cooling_rate=0.85):
    attempt = 1
    
    while True:
        current = list(initial_state) if attempt == 1 else [random.randint(0, 7) for _ in range(8)]

        T = T_init
        loop_count = 0

        print(f"\n Attempt {attempt} (Initial Cost: {calculate_cost(current)}) ")

        succeeded = False
        while T > 1e-4:
            current_cost = calculate_cost(current)
            if current_cost == 0:
                print(f"\nSUCCESS! Global optimum found on attempt {attempt} in loop {loop_count}.")
                succeeded = True
                break

            loop_count += 1
            next_state, col, new_row = get_random_neighbour(current)
            next_cost = calculate_cost(next_state)
            
            delta_E = current_cost - next_cost

            if delta_E > 0:
                current = next_state
                status = "Accepted "
                prob = 1.0
            else:
                prob = math.exp(delta_E / T)
                if random.random() < prob:
                    current = next_state
                    status = "Accepted "
                else:
                    status = "Rejected"

            print(f"loop {loop_count:2d} | Col {col}->Row {new_row} | Queens: {next_state} | "
                  f"next.cost: {next_cost:2d} | ΔE: {delta_E:2d} | T: {T:6.2f} | p: {prob:.4f} | {status}")

            T *= cooling_rate

        final_cost = calculate_cost(current)
        status_str = "SUCCESS (Goal Reached)" if succeeded else "FAILED (Temperature Depleted)"
        
        print(f"\n---> End of Attempt {attempt} | Final State: {current} | Cost: {final_cost} | {status_str}")
        print_grid(current)

        if succeeded:
            break

        attempt += 1

    return current

if __name__ == "__main__":
    initial_state = [4, 6, 0, 7, 1, 3, 0, 5]
    final_solution = simulated_annealing(initial_state)
    print(f"\nFinal Valid Solution: {final_solution} with Cost: {calculate_cost(final_solution)}")
