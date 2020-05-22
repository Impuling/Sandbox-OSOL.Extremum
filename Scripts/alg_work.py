import numpy
from OSOL.Extremum.Tools.OptimizationTools import create_algorithm_from_json
from OSOL.Extremum.Applications.tools import create_task_from_json
from OSOL.Extremum.Tools.Encoders import CustomEncoder as encoder 
from OSOL.Extremum.Numerical_Objects.Vector import Vector

from OSOL.Extremum.Optimization.Terminators.MaxTimeTerminator import MaxTimeTerminator

from os.path import exists
import json

def main():
	output = 'result.txt'
	path_to_task = './Config/config_task.json'
	task = create_task_from_json(json.load(open(path_to_task, 'r')))
	path_to_algorithm = './Config/config_alg.json'
	algorithm = create_algorithm_from_json(json.load(open(path_to_algorithm, 'r')))
	terminator = MaxTimeTerminator('s:150')

	print('Processing')

	seed = './Config/seed_values.json'
	if exists(seed):
		seed_values = [Vector.from_json(json.load(open(f, 'r')))
                       for f in seed.split(',')]
		x = algorithm.work(task['f'], task['area'], terminator, seed_values)
	else:
		x = algorithm.work(task['f'], task['area'], terminator)

	json.dump(x, open(output, 'w'), cls=encoder, indent=2)

	print('Done')

if __name__ == '__main__':
	main()
