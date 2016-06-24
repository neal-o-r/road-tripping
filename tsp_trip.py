import numpy as np
import random as rd

def length_of_trip(order, dists):
	# given a distance matrix and an ordered route
	# this function returns the distance travelled

	distance_travelled = 0.
	for i in range(len(order)):
	
		from_stop = order[i][0]
		to_stop	  = order[i][1]
		distance_travelled += dists[from_stop][to_stop]

	
	return distance_travelled
		

def randomise_all():
	# create a random cycle
	# all cycles visit each landmark once
	stops = range(52)
	order = []
	rd.shuffle(stops)

	stop = stops[0]
	for s in stops:
		
		stops.remove(stop)
		next_stop = rd.choice(stops)
		
		order.append([stop,next_stop])	
		stop = next_stop

	return set(tuple(x) for x in order)


def swap_pair(order_set, number=3):
	# switches "number" pairs in order
	order = list(order_set) 
	order = [list(x) for x in order]

	for i in range(number):

		point = rd.randrange(0, len(order)-1)
		
		order[point][1], order[point-2][0]   = order[point-2][0], order[point][1]
		order[point-1][1], order[point-3][0] = order[point-3][0], order[point-1][1]

	return order




f = open("places.txt", 'r')

urls = f.readlines()

f.close()

urls = [url.rstrip('\n') for url in urls]

names = []

for url in urls:

        url = (url.split('/')[-1]).replace('%27', "'")
        names.append( url.replace('_', " ") )


dists = np.loadtxt("dist.txt") / 1000. # km
times = np.loadtxt("time.txt")




