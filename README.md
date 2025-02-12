# 📜 Computational Engineering
# 🚀 Project
This project implements a **symbolic regression** algorithm using **genetic programming (GP)** to evolve a mathematical expression that approximates a target function based on a dataset.

The algorithm uses **syntax trees** to represent mathematical expressions and applies **selection, crossover, and mutation** to optimize the solutions. The error is measured using the **Mean Squared Error (MSE)**.

## Algorithm Workflow
The algorithm follows these main steps:

1. **Population Initialization**: Generates random trees representing mathematical equations.
2. **Evaluation**: Each tree is evaluated by calculating the error against real values.
3. **Selection**: The best individuals are chosen for reproduction.
4. **Crossover**: Two trees are combined to generate new expressions.
5. **Mutation**: Some formulas are randomly modified to introduce variability.
6. **Elitism**: Some of the best trees are kept unchanged for the next generation.
7. **Iteration**: The process continues until reaching the maximum number of generations or finding a satisfactory solution.

## Function Implementations

### 1. `generate_random_tree`
Generates a **random tree** of mathematical expressions.
- If the depth is 0, a leaf is created:
  - A **variable** (e.g., `x`) or a **random constant** is selected.
- If an operator is needed:
  - It can be a **unary operator** (sin, cos, log) with one child.
  - Or a **binary operator** (+, -, *, /) with two children.

### 2. `SymbolicRegression.__init__`
Initializes symbolic regression with various parameters:
- `variables`: available variables (e.g., `['x', 'y']`).
- `operators`: allowed operators.
- `population_size`: number of individuals in the population.
- `generations`: number of generations for evolution.
- `mutation_rate` and `crossover_rate`: probability of mutation and crossover.
- `elitism_rate`: percentage of top individuals preserved.
- `tournament_size`: size of the tournament in selection.
- `max_depth`: maximum depth of trees.
- `seed`: value to ensure reproducibility.

### 3. `initialize_population`
Generates an initial population of random trees.

### 4. `evaluate_population`
Evaluates the population using **MSE** between predictions and real values.
- Uses **parallel programming** (`multiprocessing.Pool`) to speed up calculations.
- Reuses already computed results through a **cache**.

### 5. `evaluate_individual`
Evaluates a single individual against the dataset.

### 6. `validate_tree`
Checks if a tree is valid.

### 7. `hybrid_selection`
Selects an individual for reproduction by combining:
- **Tournament**: Encourages diversity in early stages.
- **Roulette wheel**: In later stages, it favors the best individuals.

### 8. `roulette_wheel_selection`
Selects an individual with probability proportional to the inverse of its MSE.

### 9. `tournament_selection`
Selects the best individual from a random group.

### 10. `elitism_dynamic`
Keeps a variable percentage of top individuals from one generation to another.

### 11. `tree_depth`
Computes the depth of a tree.

### 12. `simplify_tree`
Simplifies trees by replacing constant sub-expressions with a precomputed value.  
This method significantly improved performance by reducing the creation of excessively deep trees.

### 13. `crossover`
Swaps subtrees between two individuals to generate new expressions.
- Randomly selects a node in both parents.
- Swaps the corresponding subtrees.
- Simplifies the result using the `simplify_tree` function.

### 14. `mutate`
Modifies a tree by replacing a subtree with a new random one.

### 15. `collect_nodes`
Returns all nodes of a tree.

### 16. `evolve`
The core of the genetic algorithm:
1. **Initializes the population**.
2. **Iterates through generations**:
   - Evaluates the population.
   - Retains the best individuals (elitism).
   - Selects parents.
   - Applies crossover and mutation.
   - Reinitializes 10% of the population every 10 generations.
3. **Returns the best formula found**.

### 17. `fit`
Starts the model evolution based on the data.

## Collaborations
During the implementation of this project, I collaborated with Andrea Bioddo, exchanging information and feedback on the written code, which helped us achieve better results.  
In particular, we worked together on implementing tree simplification functions and designing tournament and roulette selection methods.

## Conclusion
This implementation of symbolic regression combines **advanced genetic algorithms** with **dynamic selection techniques** and **tree simplification**, making it both efficient and effective. It successfully finds formulas that minimize MSE as much as possible.  
Below, you can see the results obtained for various datasets.

| Problem | MSE                |
|---------|--------------------|
| 1       | 7.125940794232773e-34|
| 2       | 9909848386207.594 |
| 3       | 0.600              |
| 4       | 0.095              |
| 5       | 9.883570418267258e+44|
| 6       | 0.004311656386509286|
| 7       | 256.63535635927843|
| 8       | 1194339.3546052114|
