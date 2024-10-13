import random

# Simple function to simulate finding an optimal solution
def find_optimal_solution(user_input):
    def fitness_function(solution):
        # Hypothetical fitness function for an example optimization problem
        return -abs(solution - 42)  # Example: The optimal solution is 42

    # Create a random population and find the best solution
    population = [random.randint(1, 100) for _ in range(10)]
    best_solution = max(population, key=fitness_function)

    return f"The optimal solution found is {best_solution}"
