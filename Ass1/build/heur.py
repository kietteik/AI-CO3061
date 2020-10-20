# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:23:36 2020

@author: saguilark
"""
# Install library
# !pip install mlrose
# Import necessary libraries
import mlrose
import numpy as np
import random as rd


# Defining the objective function
def queens_max(position):

    # We start the count
    no_attack_on_j = 0
    queen_not_attacking = 0
    # Compare for each pair of queens
    for i in range(len(position) - 1):
        no_attack_on_j = 0
        for j in range(i + 1, len(position)):

            # Check if there is any diagonal or horizontal attack.
            # Iterative process for each column
            if (position[j] != position[i]) and (position[j] != position[i] + (j - i)) and (position[j] != position[i] - (j - i)):

                """If there isn't any attack on the evaluated column.
                The count is increased by one. 
                This counter is only used as a reference ."""
                no_attack_on_j += 1

                """If there is no attack on all the columns.
                The general counter is increased by one.
                This counter indicates the number of queens that are correctly
                positioned."""
                if(no_attack_on_j == len(position)-1-i):
                    queen_not_attacking += 1
                """The return number is the number of queens not attacking each
                other if this number is 7 we add one cause it means the last
                queen is also free of attack."""
    if(queen_not_attacking == 7):
        queen_not_attacking += 1
    return queen_not_attacking


_n = int(input("insert n:"))
# Assign the objective function to "CustomFitness" method.
objective = mlrose.CustomFitness(queens_max)

# Description of the problem
problem = mlrose.DiscreteOpt(
    length=_n, fitness_fn=objective, maximize=True, max_val=_n)


# Define decay schedule
T = mlrose.ExpDecay()
# Define initial state
initial_position = np.array([rd.randrange(0, _n, 1)]*_n)
# Solve problem using simulated annealing
best_position, best_objective = mlrose.simulated_annealing(problem=problem, schedule=T,
                                                           max_attempts=1000000, max_iters=100000,
                                                           init_state=initial_position)
print('The best position found is: ', best_position)
print('The number of queens that are not attacking each other is: ', best_objective)
