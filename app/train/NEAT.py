from __future__ import print_function

import os
from neat import nn, population, statistics
from app.dbconnect import conn
from app import common
import numpy as np
# Network inputs and expected outputs.

cur = conn.cursor()
cur.execute("SELECT * FROM songs")
rv = cur.fetchall()

inputsTrain = np.empty([len(rv), 36])
outputsTrain = np.empty([len(rv), 4])


for i in range(0, len(rv)):
    dict = common.loadDict(os.path.join(common.load('data_dir'),
                           rv[i]['data']))
    arr = common.featureDictToArray(dict)
    # print(arr.shape)
    inputsTrain[i, :] = arr
    temp = np.zeros(4)
    temp[int(rv[i]['genre']) - 1] = 1
    outputsTrain[i, :] = temp

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(inputsTrain)
print(outputsTrain)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def eval_fitness(genomes):
    for g in genomes:
        net = nn.create_feed_forward_phenotype(g)
        # print(g)
        sum_square_error = 0.0
        i = 0
        for inputs, expected in zip(inputsTrain, outputsTrain):
            # Serial activation propagates
            # the inputs through the entire network.
            output = net.serial_activate(inputs)
            # if(i == 0):
                # print(output)
                # print(expected)
                # print((output - expected) ** 2)
            sum_square_error += np.sum((output - expected) ** 2)
            # i += 1
        # When the output matches expected for all inputs, fitness will reach
        # its maximum value of 1.0.
        g.fitness = 1 - sum_square_error


local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'neuron.config')
pop = population.Population(config_path)
pop.run(eval_fitness, 300)

# Log statistics.
statistics.save_stats(pop.statistics)
statistics.save_species_count(pop.statistics)
statistics.save_species_fitness(pop.statistics)

print('Number of evaluations: {0}'.format(pop.total_evaluations))

# Show output of the most fit genome against training data.
winner = pop.statistics.best_genome()
print('\nBest genome:\n{!s}'.format(winner))
print('\nOutput:')
winner_net = nn.create_feed_forward_phenotype(winner)
for inputs, expected in zip(inputsTrain, outputsTrain):
    output = winner_net.serial_activate(inputs)
    print("expected {0:1.5f} got {1:1.5f}".format(expected, output))
