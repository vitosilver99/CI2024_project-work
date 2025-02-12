# 📜 Computational Engineering

## 🏗️ Lab 0: Introduction to the Labs

**Task:** The objective of Lab 0 was to understand how future labs would be structured. The task was to create a public GitHub repository named `CI2024_lab0` and add a Markdown file containing a joke or a funny phrase. Additionally, during the review phase, we had to open an issue on GitHub to comment on other students' jokes.

**My Markdown File Content:**

```
Question: Why did the computer go to therapy?

Answer: Because it had too many "bugs"!
```

**Issues Received on My Repository:**

- 📝 *"I might try debugging myself to save the psychiatrist's money"* - by `AbstractBorderStudio`
- 📝 *"Nice irony"* - by `YounessB1`

**My Reviews on Other Students' Repositories:**

- To `LucaMeno`: *"Good joke, it's perfect for the requirement"*
- To `Zurehma`: *"Good job!! I hope it's not necessary, otherwise I'm in trouble too... I'm intolerant to coffee."*

---

## 🔢 Lab 1: Set Cover Problem

**Task:** The Set Cover Problem involves a universe of elements and a collection of sets, where each set contains some of those elements. The goal is to select the smallest number of sets such that their union covers all the elements in the universe.

**My Solution:** I implemented a solution based on the **Tabu Search** algorithm. Below are the best results I obtained:

| Instance | Universe size | Num sets | Density | Result                |
| -------- | ------------- | -------- | ------- | --------------------- |
| 1        | 100           | 10       | 0.2     | -258.7307216591009    |
| 2        | 1,000         | 100      | 0.2     | -6,023.07723283961    |
| 3        | 10,000        | 1,000    | 0.2     | -886,177.5509467437   |
| 4        | 100,000       | 10,000   | 0.1     | -102,783,314.62948833 |
| 5        | 100,000       | 10,000   | 0.2     | -221,073,680.58279872 |
| 6        | 100,000       | 10,000   | 0.3     | -254,549,363.31683755 |

**Review Received:**

- 📝 *"Wow, you did a great job. You are combining most of the approaches seen at lecture. I struggle to find improvements, I really like the combination of multiple tweaks in the tabu search. Maybe you could add an early stopping criteria, since the algorithm runs the established number of times no matter how it is performing. If there are no new improvements for a while, it may reduce the computing time to stop that restart earlier than expected. Comments and the README are much appreciated, thank you."* - by `YounessB1`

**My Reviews on Other Students' Solutions:**

- To `michepaolo`: *"It is a very good solution to the set-cover problem, I think a great job has been done. However, your current implementation uses a fixed factor of increasing/decreasing strength based on the number of best solutions in the buffer. You could make the mutation of the strength variable more sophisticated. For example, the strength could decrease gradually over time, as in a simulated cooling process. This would allow for stronger mutations in the beginning (when exploration is important) and weaker mutations toward the end (when more precision is needed). In this way, I think there could be an improvement in the final result."*

- To `fedefortu8`: *"I think a very good job has been done to solve the set-cover problem. I'm struggling to find improvements to the code. The only thing I can think of is to make the temperature decrement more dynamic, adapting to the execution of the algorithm. For example, measure the distance between the current solution and the best solution found so far and adjust the temperature according to this distance. Anyway, good work!"*

---

## 🚀 Lab 2: Traveling Salesman Problem (TSP)

**Task:** Given a set of cities and the distances between each pair of cities, the goal of the problem is to find the order of city visits that minimizes the total route distance while ensuring that each city is visited only once, ending back at the starting point.

**My Solution:**

| City    | Greedy Algorithm | Evolutionary Algorithm | Shortest tour |
|---------|-----------------|------------------------|--------------|
| Vanuatu | 1345.54km       | 1345.54km              | 1345.54km    |
| Italy   | 4200.89km       | 4193.69km              | 4172.76km    |
| Russia  | 33674.80km      | 33405.30km             | 32722.5km    |
| US      | 40467.57km      | 40234.55km             | -            |
| China   | 54716.28km      | 54565.02km             | -            |

**Review Received:**

#### 📝 by `GiorgioBongiovanni`:
First of all, I want to congratulate you on the excellent results you have achieved.
I haven’t read a description from you but I believe you implemented the order crossover as the type of crossover operator and I think this was a key choice in achieving such high accuracy compared to the optimal results for the following reasons.
The TSP imposes specific constraints that any solution must adhere to:
- Valid Permutation: Each city must be visited exactly once.
- Adjacency: The order in which cities are visited determines the solution's quality since it affects the total distance.
- Cyclic Structure: The first and last cities must be connected to close the cycle.

The Order Crossover is designed to respect these constraints making it a natural choice for the TSP.
Order Crossover operates in two stages:
1) Preservation of Partial Order: A segment from the first parent is copied into the child at the same position.
2) Filling Missing Positions: The child is completed with the remaining cities from the second parent maintaining their relative order.
This strategy ensures that the cities copied from the first parent maintain their order and local adjacencies and the cities from the second parent contribute diversity by introducing new connections.
Order Crossover is particularly well-suited for the TSP for several reasons, explained in relation to the problem's constraints and goals:
Firstly, the segment copied from the first parent remains intact in the child preserving local adjacencies.
This is crucial in the TSP because good solutions often emerge from configurations that retain favorable connections between neighboring cities.
Secondly, by filling the remaining positions with cities from the second parent, Order Crossover introduces new connections and increases diversity.
This balance between exploitation (preserving good structures) and exploration (introducing new configurations) helps avoid local optima.
Thirdly, Order Crossover always produces valid permutations, where each city appears exactly once and, while the TSP requires a cyclic structure, Order Crossover inherently manages the connection between the first and last cities, as the child is constructed to respect the parents' relative order.

A suggestion I would like to propose to improve the computation time of the genetic algorithm is the following:
Introducing an early stopping criterion based on the stagnation of the best individual's fitness is a practical strategy to improve the efficiency of the genetic algorithm. 
If the fitness improvement stalls, the algorithm is likely close to a local minimum or the optimal solution thus continuing to generate new populations may not yield significant benefits.
For this reason, lack of fitness improvement over several generations is a sign that the population has reached a stable state.
This approach could avoid wasting computational resources on unnecessary iterations, especially for complex problems like the TSP.
The idea is to monitor the fitness improvement of the best individual. If the fitness does not improve for a predetermined number of consecutive generations (for example, 50 generations), the algorithm terminates:
``` python
no_improvement_count = 0
max_no_improvement = 50  # Maximum generations without fitness improvement

best_fitness = float('-inf')  # Initialize best fitness to the lowest possible value

for generation in range(MAX_GENERATIONS):
    # Execute the steps of the genetic algorithm
    # (e.g., selection, crossover, mutation, and fitness evaluation)
    ...

    # Find the fitness of the best individual in the current generation
    current_best_fitness = max(individual.fitness for individual in population)

    # Check if there is an improvement in the best fitness
    if current_best_fitness > best_fitness:  # Fitness must increase to improve
        best_fitness = current_best_fitness  # Update the best fitness
        no_improvement_count = 0  # Reset the no improvement counter
        print(f"Generation {generation}: Fitness improved to {best_fitness:.2f}")
    else:
        no_improvement_count += 1  # Increment the no improvement counter
        print(f"Generation {generation}: No improvement for {no_improvement_count} generations.")

    # Terminate if no improvement has been observed for the specified limit
    if no_improvement_count >= max_no_improvement:
        print(f"Terminating early at generation {generation} due to stagnation.")
        break

# Final output of the best solution
print(f"Algorithm terminated. Best fitness found: {best_fitness:.2f}")

```
From my point of view, instead of only tracking the best individual, you could also monitor the average fitness improvement of the entire population. This provides a more comprehensive picture of the algorithm's convergence.


In conclusion, it is likely that Order Crossover played a key role in preserving and combining the essential properties of the parents, leading to high-quality solutions. Good job!

**My Reviews on Other Students' Solutions:**

#### To `MartinaPlumari`: 
#### General
I think an excellent job has been done in addressing the TSP problem. The comments throughout the code were very helpful in understanding the functionality of the proposed algorithms.  
The use of NetworkX and Matplotlib to visualize the graph and the fitness trend offers a very clear way to analyze the results.


#### Evolutionary Algorithm (EA)
I really appreciated the implementation of the two greedy algorithms and their comparison. The choice of using an adaptive mutation probability is an excellent idea to balance exploration and exploitation during the evolutionary process.  
The stopping criterion based on the number of generations without improvement is also very interesting, as it increases efficiency by avoiding unnecessary iterations.

The configurations showcase the trade-off between solution quality and computational time very well. More explorative configurations (2 and 3) achieve better results for large instances but at a high computational cost. Leaner configurations (1 and 4) are ideal for smaller instances or obtaining quick solutions.


#### Greedy + 2-opt
The variant that selects a random starting city for each iteration is interesting, as it ensures greater diversity in the initial solutions compared to the version that uses lexicographical order.  
The use of the `stationary` counter to determine the stopping criterion is, in my opinion, a simple but effective solution. However, a dynamic or more adaptive parameter could further accelerate convergence.

The results highlight the ability of the 2-opt algorithm to significantly improve the initial greedy solution. For example, for Vanuatu, the improvement is from 1536.86 km (greedy) to 1420.31 km (2-opt).  
However, as noted, the results can vary significantly due to the stochastic nature of the algorithm, as demonstrated by the case of Russia, where an optimal result was obtained only once.  
The algorithm performs better on small and medium-sized instances but tends to require more iterations for very large instances (e.g., China and the USA).

### Conclusion
Overall, I think you've done an extraordinary job!!


#### To `hllqna`:
The code represents an excellent implementation of the TSP problem using various strategies (Greedy, Tabu Search, Evolutionary Strategy). Each approach is well-defined and offers valuable insights: the Greedy algorithm is fast but not scalable for large datasets; the "Greedier" version enhances random exploration but remains limited for larger instances. Tabu Search incorporates memory to avoid cycles but could benefit from convergence monitoring and more sophisticated diversity management. The Evolutionary Strategy is well-designed, with effective mutation and crossover operators, showcasing a strong balance between exploration and exploitation.

To conclude, I recommend adding a comparative analysis of the results across the different algorithms in future implementations. This would make the work even more comprehensive. Great job overall!

---
## 🧩 Lab 3: n²-1 Puzzle

**Task:** The **n²-1 puzzle** consists of a square grid filled with numbers from 1 to \( n^2-1 \) and a blank tile represented by 0. The objective is to arrange the numbers in ascending order by shifting tiles adjacent to the blank space. To tackle this problem, I implemented two pathfinding algorithms: **A-Star** and **Greedy Best-First Search**.

### **Description of the algorithms I used**

#### **A\***
The A\* algorithm selects the next state based on:
- **g(n):** The cumulative cost from the initial state to the current state.
- **h(n):** A heuristic estimating the cost to reach the goal state.

By using \( f(n) = g(n) + h(n) \), A\* ensures both optimality and efficiency.

#### **Greedy Best-First Search**
This algorithm evaluates states solely on the heuristic function \( h(n) \), choosing states that seem closer to the goal. However, it does not guarantee an optimal solution. To prevent excessive depth exploration, I introduced a depth limit.

### **Implementation Details**
- **Heuristic:** I used the **Manhattan distance**, which sums the horizontal and vertical distances of each tile from its target position.
- **State Tracking:** To enhance efficiency, I implemented a mechanism that prevents revisiting already explored states.


## **Results**

#### **Performance Comparison for a 3×3 Grid**

| Algorithm                  | Number of Steps | Total Cost  | Execution Time |
|----------------------------|-----------------|-------------|----------------|
| **A\***                   | 26              | 2,028       | 0s         |
| **Greedy Best-First Search** | 34              | 297         | 0s         |

- **A\*** found an optimal solution but took slightly longer.
- **Greedy Best-First Search** was faster but found a suboptimal solution.

#### **Performance Comparison for a 4×4 Grid**

| Algorithm                  | Number of Steps | Total Cost  | Execution Time  |
|----------------------------|-----------------|-------------|-----------------|
| **A\***                    | 58              | 6,473,212   | 1m 32.7 s       |
| **Greedy Best-First Search** | 154             | 9,561       | 0.1 s           |

- **A\*** ensured optimality but required significant computational resources.
- **Greedy Best-First Search** produced a faster but suboptimal solution.

### **Analysis and Discussion**
- **A\*** is optimal but memory-intensive, making it impractical for larger grids.
- **Greedy Best-First Search** is significantly faster but fails to guarantee optimality.

### **Conclusions**
- **A\*** is preferable for scenarios requiring optimality but has high computational demands.
- **Greedy Best-First Search** is useful when speed is prioritized over optimality.
- Potential improvements:
  - Implementing more advanced heuristics.
  - Memory optimization techniques.


### **Reviews Received:**

- 📝 *"Well done. I appreciate the implementation of two different algorithms and the comparison between them. The README with the tables is really clear. Well done implementing a mechanism to track previously visited states for both algorithms. An improvement I suggest is implementing another algorithm for 5x5 puzzle dimensions, for example, IDA*. A* algorithm really struggles with bigger dimensions, so using another algorithm could be an interesting way to solve those puzzles. Overall, a well-done job with a really concise and clear explanation! Good job."* - by `AlesoGio`

- 📝 *"This project is well-designed and demonstrates a solid understanding of algorithmic problem-solving. The code is clear and well-structured, with functions that make the logic behind each step easy to follow. The choice of the Manhattan distance as the heuristic is both standard and effective, ensuring that the algorithms operate consistently and predictably.

    The implementation of A* is precise, showcasing its ability to find optimal solutions. The Greedy Best-First Search, while less sophisticated, is handled thoughtfully; the addition of a depth limit enhances its reliability despite its heuristic-driven nature. These decisions reflect a careful consideration of the trade-offs between the two algorithms.

    The README is another strength of the project. The algorithms are explained in a concise yet comprehensive manner, and the analysis of results highlights the differences in terms of execution time, number of steps, and computational cost. The trade-offs between optimality and efficiency are well-documented.

    Overall, this project demonstrates a strong grasp of the subject matter and effectively communicates the findings. Well done!"* - by `andreazenotto`


### **My Reviews on Other Students' Solutions:**

- To `andreabioddo`: *"I think a good job has been done for this lab. The code is solid and effectively implements A* with a good choice of data structures such as heapq for edge exploration and nametuple to represent actions. The modularity and clarity of the functions improve the readability and reusability of the code. To further improve the work, I could suggest trying other simpler solutions of A-star to compare various implementations. But as I said at the beginning, great work!"*

- To `FruttoCheap`: *"I think a very good job has been done for this work. I like the well-structured implementation to solve the n²-1 puzzle using different search techniques (BFS, DFS, Iterative Deepening DFS, UCS, and A*). Each algorithm is clear and modular, with dedicated functions to generate initial states, check solvability, and compute neighbors. A suggestion to further improve the work would be to add a README file with a comparative analysis of the different algorithms, including metrics such as execution time and nodes explored in relation to the puzzle size. This would allow for a deeper analysis of the impact of different techniques and enrich the project documentation. But overall, great work!"*

---
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
