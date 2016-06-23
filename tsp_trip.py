import numpy as np


def length_of_trip(order, dists):

	distance_travelled = 0.
	for i in range(len(order)):
		
		distance_travelled += dists[order[i]][order[i-1]]

	
	return distance_travelled
		


f = open("places.txt", 'r')

urls = f.readlines()

f.close()

urls = [url.rstrip('\n') for url in urls]

names = []

for url in urls:

        url = (url.split('/')[-1]).replace('%27', "'")
        names.append( url.replace('_', " ") )

dists = np.loadtxt("dists.txt") / 1000.
times = np.loadtxt("times.txt")

print length_of_trip(range(52), dists)

