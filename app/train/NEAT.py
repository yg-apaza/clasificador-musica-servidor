import os
from neat import nn, population
from app.dbconnect import conn
from app import common
import numpy as np
import pickle
from app.train.reporte import NEATReporter


def entrenar():
    cur = conn.cursor()
    cur.execute("SELECT * FROM songs")
    rv = cur.fetchall()

    inputsTrain = np.empty([len(rv), 36])
    outputsTrain = np.empty([len(rv), 4])

    def eval_fitness(genomes):
        for g in genomes:
            net = nn.create_feed_forward_phenotype(g)
            sum_square_error = 0.0
            for inputs, expected in zip(inputsTrain, outputsTrain):
                output = net.serial_activate(inputs)
                sum_square_error += np.mean((output - expected) ** 2)
            g.fitness = -sum_square_error

    for i in range(0, len(rv)):
        dict = common.loadDict(os.path.join(common.load('data_dir'),
                               rv[i]['data']))
        arr = common.featureDictToArray(dict)
        inputsTrain[i, :] = arr
        temp = np.zeros(4)
        temp[int(rv[i]['genre']) - 1] = 1
        outputsTrain[i, :] = temp

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neuron.config')
    pop = population.Population(config_path)
    reporte = NEATReporter()
    pop.add_reporter(reporte)
    pop.run(eval_fitness, 300)

    winner = pop.statistics.best_genome()
    pickle.dump(winner, open(os.path.join(common.load('data_dir'),
                             'redNeuronal.p'), 'w'))
    return winner
