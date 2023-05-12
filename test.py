
import pygad
import numpy
import sys


def fitness_func(solutions, _):
    x = int(solutions[0])
    y = int(solutions[1])

    add = x + y
    if (add != 7):
        return 1.0/sys.maxsize
    output = numpy.power(x , 2) + numpy.power(y, 2)
    return 1.0/numpy.abs(output)

# Parameters
fitness_function = fitness_func

gene_space = [{'low': 1, 'high': 16}, {'low': 3, 'high': 50}]

ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=2,
                       fitness_func=fitness_function,
                       sol_per_pop=100,
                       num_genes=2,
                       gene_space=gene_space,
                       parent_selection_type="rank",
                       keep_parents=3,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=0.01)

ga_instance.run()

# ga_instance.plot_result()

print("-------------------------------Result--------------------------------")

solution, solution_fitness, solution_idx = ga_instance.best_solution()

print ( "solution " , solution)