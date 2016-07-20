from __future__ import print_function

from neat.reporting import BaseReporter
from app.websocket import clientes
import time
from neat.math_util import mean, stdev


class NEATReporter(BaseReporter):
    def __init__(self):
        self.generation = None
        self.generation_start_time = None

    def start_generation(self, generation):
        self.generation = generation
        self.generation_start_time = time.time()
        [cl.write_message('\n********* Generacion {0} *********\n'
                          .format(generation)) for cl in clientes]

    def end_generation(self):
        [cl.write_message("\n     Tiempo de la generacion: {0:.3f} segundos\n\n"
                          .format(time.time() - self.generation_start_time))
         for cl in clientes]

    def loading_checkpoint(self, filename):
        print('Resuming from a previous point: ' + filename)

    def saving_checkpoint(self, checkpoint_type, filename):
        print('Creating {0} checkpoint file {1} at generation: {0}'.format(
            checkpoint_type, filename, self.generation))

    def post_evaluate(self, population, species, best):
        fit_mean = mean([c.fitness for c in population])
        fit_std = stdev([c.fitness for c in population])
        print('Population\'s average fitness: {0:3.5f} stdev: {1:3.5f}'
              .format(fit_mean, fit_std))
        print('Best fitness: {0:3.5f} - size: {1!r} - species {2} - id {3}'
              .format(best.fitness, best.size(), best.species_id, best.ID))
        print('Species length: {0:d} totaling {1:d} individuals'
              .format(len(species), sum([len(s.members) for s in species])))
        print('Species ID       : {0!s}'.format([s.ID for s in species]))
        print('Species size     : {0!s}'
              .format([len(s.members) for s in species]))
        print('Species age      : {0}'.format([s.age for s in species]))

        [cl.write_message(('\n     Fitness promedio de la poblacion: {0:3.5f}'
                           + ' Desviacion: {1:3.5f}')
                          .format(fit_mean, fit_std)) for cl in clientes]

        [cl.write_message(
         '\n     Mejor fitness: {0:3.5f} - size: {1!r} - Especie {2} - ID {3}\n'
         .format(best.fitness, best.size(),
                 best.species_id, best.ID)) for cl in clientes]

    def complete_extinction(self):
        [cl.write_message("\nTodas las especies se han extinguido.")
         for cl in clientes]

    def found_solution(self, generation, best):
        print('\nBest individual in generation {0} meets fitness threshold - complexity: {1!r}'.format(
            self.generation, best.size()))

    def species_stagnant(self, species):
        print("\nSpecies {0} with {1} members is stagnated: removing it"
              .format(species.ID, len(species.members)))

    def info(self, msg):
        print(msg)
        # [cl.write_message(msg) for cl in clientes]
