import numpy as np
import random as rd
import routes as rt
import pandas as pd

			
def greedy_path(dists, start=0):
# function to compute the greedy path (from any point
# go to nearest that hasn't been visited) from a given starting point	
	path=[start]
	for i in range(50):
		
		dist_from = dists[path[-1]]

	 	points = range(51)
		points.remove(i)		
		for j in path:
			if j in points:
				points.remove(j) 
		
		dist_from_sub = dist_from[points]
		index = np.where(dist_from == np.min(dist_from_sub))		
		path.append(index[0][0])

	return path

def swap_pair(input_list1, n=3):
	# given a list, do n pair swaps
	input_list = list(input_list1) # this copy is a bit shit,
				# but it's necessary to stop in place shuffling
	for i in range(n):

		index = rd.randrange(len(input_list) - 1)
		input_list[index], input_list[index-1] = \
		input_list[index-1], input_list[index]

	return input_list

def move_section(input_list1):
	# move a section of the route to somewhere else

	input_list = list(input_list1)
	start_index = rd.randint(0, len(input_list) - 1)
	length = rd.randint(2, 20)
    
	subset = input_list[start_index:start_index + length]
	input_list = input_list[:start_index] + input_list[start_index + length:]
    
	insert_index = rd.randint(0, len(input_list) + len(subset) - 1)
	output_list = input_list[:insert_index] + subset + input_list[insert_index:]
    	return output_list

def fitness_func(path, dists):
	# get the length of a path.
	path = rt.Route(path) 	
	fitness = path.length_of_route(dists)
	
	return fitness

def run_algo(dists, gens=5000, pop_size=50):
	# run evolutionary algorithm
	pop_subset_size = int(pop_size / 10.)
        gen_10pct = int(gens / 10.)

	population = []
	best = None
	best_len = 1e10 # dummy value to start
	for i in range(pop_size):
		population.append(greedy_path(dists, start=i))
	
	for gen in range(gens):

		fitness = []
		for p in population:
			fitness.append(fitness_func(p, dists))

		if min(fitness) < best_len:
			best = rt.Route(population[fitness.index(min(fitness))])		
			best_len = best.length_of_route(dists)
	
		new_pop = []
		for rank, index in enumerate(np.argsort(fitness)[:pop_subset_size]):

			if (gen % gen_10pct == 0 or gen == gen - 1) and rank == 0:
                		print("Generation %d" %gen)
                		print(population[index])
                		print("Length: %f" %fitness[index])
				print("")

            # Create 1 exact copy of each of the top road trips
            		new_pop.append(population[index])

            # Create 2 offspring with 1-3 point mutations
            		for i in range(2):
                		new_pop.append(swap_pair(population[index]))
                
            # Create 7 offspring with a single shuffle mutation
            		for i in range(7):
                		new_pop.append(move_section(population[index]))

        # Replace the old population with the new population of offspring 
        	for i in range(len(population))[::-1]:
            		del population[i]
		#return population, new_pop
        	population = new_pop
	return best

f = open("places.txt", 'r')

urls = f.readlines()

f.close()

urls = [url.rstrip('\n') for url in urls]

names = []

for url in urls:

        url = (url.split('/')[-1]).replace('%27', "'")
        names.append( url.replace('_', " ") )
# get names and lat-lons

df = pd.read_csv("latlon.txt")

dists_in = np.loadtxt("dist.txt") / 1000. # km
times_in = np.loadtxt("time.txt")

dists1 = np.delete(dists_in, (41), axis=1)
dists = np.delete(dists1, (41), axis=0)

times1 = np.delete(times_in, (41), axis=1)
times  = np.delete(times1, (41), axis=0)
# because i'm an idiot places 41 & 42 were the same place,
# so there are duplicate distances. this deletes them.

best = run_algo(dists)

print("Length of best route", best.length_of_route(dists))
indices = [x[0] for x in best.route]

for i in indices:

	print( '"' + str(df.Latitude[i]) + ',' + str(df.longitude[i]) + '"' + ',')


for i, j in enumerate(indices):
	print(str(i+1) + ". " + names[j])


