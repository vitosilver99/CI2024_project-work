from node import Node
import random
import math
import operator
from typing import List, Callable, Dict
import numpy as np
import copy
from multiprocessing import Pool

def generate_random_tree(variables, depth, ensure_operator=True):
    if depth == 0 or (depth > 1 and random.random() < 0.3):
        # If an operator must be ensured, do not create a leaf
        if ensure_operator:
            if random.random() < 0.3:  # Unary operator
                operation = random.choice([math.sin, math.cos, math.tan, math.log, math.sqrt])
                return Node(operation, [generate_random_tree(variables, depth - 1, ensure_operator=False)])  # One child
            else:  # Binary operator
                operation = random.choice([operator.add, operator.sub, operator.mul, operator.truediv])
                return Node(operation, [generate_random_tree(variables, depth - 1, ensure_operator=False) for _ in range(2)])
        else:
            # Leaf (variable or constant)
            if random.random() < 0.5:
                return Node(random.choice(variables))  # Variable
            else:
                return Node(random.uniform(1e-3, 20))  # Constant
    else:
        # Node with an operator
        if random.random() < 0.5:  # Unary operator
            operation = random.choice([math.sin, math.cos, math.tan, math.log, math.sqrt])
            return Node(operation, [generate_random_tree(variables, depth - 1, ensure_operator=False)])  # One child
        else:  # Binary operator
            operation = random.choice([operator.add, operator.sub, operator.mul, operator.truediv])
            return Node(operation, [generate_random_tree(variables, depth - 1, ensure_operator=False) for _ in range(2)])

class SymbolicRegression:
    def __init__(
        self, 
        variables: List[str], 
        operators: List[Callable], 
        population_size: int = 100, 
        generations: int = 50, 
        mutation_rate: float = 0.2, 
        crossover_rate: float = 0.7, 
        elitism_rate: float = 0.05,
        turnament_size: int = 3,
        max_depth: int = 10, 
        seed: int = 41
    ):
        self.variables = variables
        self.operators = operators
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_rate = elitism_rate
        self.max_depth = max_depth
        self.random = random.Random(seed)
        self.tournament_size = turnament_size
        self.population = []
        self.cache: Dict[str, float] = {}

    def initialize_population(self):
        self.population = [
            generate_random_tree(self.variables, depth=self.max_depth, ensure_operator=True) 
            for _ in range(self.population_size)
        ]
        assert all(isinstance(ind, Node) for ind in self.population), "Population not valid!"
    
    def evaluate_population(self, X: np.ndarray, y: np.ndarray) -> List[float]:
        fitness = []
        X_transposed = X.T

        for individual in self.population:
            tree_repr = individual.long_name  # Unique representation of the tree

            #If the tree has already been evaluated, it uses the value from the cache otherwise it calculates it
            if tree_repr in self.cache:
                fitness.append(self.cache[tree_repr])
            else:
                predictions = []
                for sample in X_transposed:
                    prediction = individual.evaluate(dict(zip(self.variables, sample)))
                    predictions.append(prediction)

                predictions = np.array(predictions)
                mse = np.mean((predictions - y) ** 2)
                fitness.append(mse)
                self.cache[tree_repr] = mse  # Cache the fitness value

        return fitness
    
    def validate_tree(self, tree):
        if tree is None or not isinstance(tree, Node):
            return False
        if callable(tree.value):
            return all(self.validate_tree(child) for child in tree.children)
        return True

    def hybrid_selection(self, fitness: List[float], generation: int) -> Node:
        # Dynamic weighting based on the current generation
        progress = generation / self.generations
        if random.random() < (1 - progress):  # More tournament in early generations
            return self.tournament_selection(fitness, self.tournament_size)
        else:  # More roulette in later generations
            return self.roulette_wheel_selection(fitness)
        
    def roulette_wheel_selection(self, fitness: List[float]) -> Node:
        inverted_fitness = [1 / (f + 1e-6) for f in fitness]
        total_fitness = sum(inverted_fitness)
        probabilities = [f / total_fitness for f in inverted_fitness]
        selected_idx = np.random.choice(range(len(self.population)), p=probabilities)
        return self.population[selected_idx]
    
    def tournament_selection(self, fitness: List[float], tournament_size) -> Node:
        selected_indices = random.sample(range(len(self.population)), tournament_size)
        best_index = min(selected_indices, key=lambda idx: fitness[idx])  # Minimisation of fitness
        return self.population[best_index]

    def elitism_dynamic(self, fitness: List[float], current_generation: int) -> List[Node]:
        max_elitism = self.elitism_rate  # Maximum percentage of elites
        min_elitism = 0.05  # Minimum percentage of elites
        dynamic_rate = min_elitism + (max_elitism - min_elitism) * (current_generation / self.generations)
        num_elites = max(1, int(dynamic_rate * self.population_size))
        elite_indices = np.argsort(fitness)[:num_elites]
        return [self.population[i] for i in elite_indices]

    # recusion in order to count tree depth
    def tree_depth(self, tree):
        if not tree.children:
            return 1
        return 1 + max(self.tree_depth(child) for child in tree.children)
    
    def simplify_tree(self, tree):
        """
        Simplifies a tree by evaluating constant subtrees.
        """
        if tree is None or not tree.children:
            return tree

        # Simplify children first
        simplified_children = [self.simplify_tree(child) for child in tree.children]
        tree.children = simplified_children

        # Check if all children are constants
        if all(child.children == [] and not callable(child.value) for child in tree.children):
            try:
                # Evaluate the subtree
                values = [child.value for child in tree.children]
                result = tree.value(*values)
                return Node(result)  # Replace subtree with a constant node
            except Exception:
                pass  # If evaluation fails, leave the tree as is

        return tree

    def crossover(self, tree1, tree2):
        tree1_copy = copy.deepcopy(tree1)
        tree2_copy = copy.deepcopy(tree2)

        nodes1 = self.collect_nodes(tree1_copy)
        nodes2 = self.collect_nodes(tree2_copy)

        if not nodes1 or not nodes2:
            return tree1_copy, tree2_copy

        node1 = random.choice(nodes1)
        node2 = random.choice(nodes2)

        def replace_node(tree, target_node, new_subtree):
            if tree is target_node:
                return new_subtree
            for i, child in enumerate(tree.children):
                tree.children[i] = replace_node(child, target_node, new_subtree)
            return tree

        tree1_copy = replace_node(tree1_copy, node1, node2)
        tree2_copy = replace_node(tree2_copy, node2, node1)

        return self.simplify_tree(tree1_copy), self.simplify_tree(tree2_copy)

    def mutate(self, tree, mutation_rate):
        """
        Mutates a tree by replacing a randomly selected subtree with a new random subtree.
        """
        if random.random() > mutation_rate:
            return tree

        # Deep copy to avoid modifying the original tree
        mutated_tree = copy.deepcopy(tree)

        # Collect all nodes in the tree
        nodes = self.collect_nodes(mutated_tree)
        if not nodes:
            return mutated_tree

        # Randomly select a node to replace
        node_to_replace = random.choice(nodes)

        # Generate a new random subtree
        new_depth = max(1, min(self.max_depth - self.tree_depth(node_to_replace), self.max_depth))
        new_subtree = generate_random_tree(self.variables, depth = new_depth, ensure_operator=True)

        # Replace the selected node
        def replace_node(tree, target_node, new_subtree):
            if tree is target_node:
                return new_subtree
            for i, child in enumerate(tree.children):
                tree.children[i] = replace_node(child, target_node, new_subtree)
            return tree

        return self.simplify_tree(replace_node(mutated_tree, node_to_replace, new_subtree))

    def collect_nodes(self, tree):
        """
        Recursively collects all nodes in the tree.
        """
        nodes = [tree]
        for child in tree.children:
            nodes.extend(self.collect_nodes(child))
        return nodes

    def evolve(self, X: np.ndarray, y: np.ndarray):
        self.initialize_population()

        best_fitness_so_far = None
        best_tree_so_far = None

        for generation in range(self.generations):
            fitness = self.evaluate_population(X, y)
            elites = self.elitism_dynamic(fitness, generation)
            
            # Find the best fitness and the best tree of the current generation
            best_index = np.argmin(fitness)  # Find the index of the best fitness
            best_fitness = fitness[best_index]
            best_tree_current = self.population[best_index]

            # Update the global best tree if necessary
            if best_fitness_so_far is None or best_fitness < best_fitness_so_far:
                best_fitness_so_far = best_fitness
                best_tree_so_far = best_tree_current
            
            print(f"Generation {generation}: Best MSE = {best_fitness:}, Tree Depth = {self.tree_depth(best_tree_so_far)}")
            print("Formula = " + str(best_tree_so_far))

            if best_fitness_so_far == 0:
                    return best_tree_so_far

            # Partial population reinitialization
            if generation % 10 == 0:
                # Number of individuals to reinitialize
                num_to_reinitialize = int(self.population_size * 0.1)
                # Population indices sorted by fitness
                sorted_indices = np.argsort(fitness)
                # Exclude elites
                non_elite_indices = sorted_indices[len(elites):]
                # Randomly select the worst individuals
                indices_to_reinitialize = random.sample(list(non_elite_indices), num_to_reinitialize)
                for idx in indices_to_reinitialize:
                    self.population[idx] = generate_random_tree(self.variables, self.max_depth, ensure_operator=True)

            new_population = elites[:]

            while len(new_population) < self.population_size:
                parent1 = self.hybrid_selection(fitness, generation)
                parent2 = self.hybrid_selection(fitness, generation)
                if random.random() < self.crossover_rate:
                    child1, child2 = self.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1, parent2
                
                if random.random() < self.mutation_rate: 
                    new_population.extend([self.mutate(child1, self.mutation_rate), self.mutate(child2, self.mutation_rate)]) 
                else: 
                    new_population.extend([child1, child2])

            self.population = new_population[:self.population_size]
            self.population = [tree for tree in self.population if self.validate_tree(tree)]

        return best_tree_so_far


    def fit(self, X: np.ndarray, y: np.ndarray) -> Node:
        return self.evolve(X, y)
