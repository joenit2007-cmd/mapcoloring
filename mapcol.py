
import random

neighbors = {
    'UP': ['UK', 'HR', 'DL', 'RJ', 'MP', 'BR'],
    'UK': ['UP', 'HP'],
    'HR': ['DL', 'UP', 'RJ', 'HP'],
    'DL': ['UP', 'HR'],
    'RJ': ['HR', 'UP', 'MP', 'GJ'],
    'MP': ['UP', 'RJ', 'CG', 'MH'],
    'BR': ['UP', 'JH', 'WB'],
    'JH': ['BR', 'WB', 'OD'],
    'WB': ['BR', 'JH', 'OD'],
    'OD': ['JH', 'WB', 'CG', 'MH'],
    'CG': ['MP', 'OD', 'MH'],
    'MH': ['MP', 'CG', 'GJ', 'OD'],
    'GJ': ['RJ', 'MH'],
    'HP': ['UK', 'HR']
}

colors = ['Red', 'Green', 'Blue', 'Yellow']

def count_conflicts(assignment, neighbors):
    conflicts = 0
    for state in neighbors:
        for neighbor in neighbors[state]:
            if assignment[state] == assignment.get(neighbor):
                conflicts += 1
    return conflicts // 2

def hill_climbing(neighbors, colors, max_steps=2000):
    assignment = {state: random.choice(colors) for state in neighbors}
    for step in range(max_steps):
        current_conflicts = count_conflicts(assignment, neighbors)
        if current_conflicts == 0:
            return assignment
        conflicted_states = [
            s for s in neighbors if any(assignment[s] == assignment[n] for n in neighbors[s] if n in assignment)
        ]
        if not conflicted_states:
            continue
        state = random.choice(conflicted_states)
        best_color = assignment[state]
        min_conflict = current_conflicts
        for color in colors:
            if color == assignment[state]:
                continue
            old_color = assignment[state]
            assignment[state] = color
            temp_conflicts = count_conflicts(assignment, neighbors)
            if temp_conflicts < min_conflict:
                best_color = color
                min_conflict = temp_conflicts
            assignment[state] = old_color
        assignment[state] = best_color
    if count_conflicts(assignment, neighbors) == 0:
        return assignment
    return None

solution = hill_climbing(neighbors, colors)

if solution:
    print("\nHill-Climbing Map Coloring Solution (North India):\n")
    for state in sorted(solution):
        print(f"{state}: {solution[state]}")
else:
    print("\nNo valid solution found (stuck in local maximum).")
