import googlemaps
import numpy as np
import pandas as pd


def find_dists():

	f = open("places.txt", 'r')

	urls = f.readlines()

	f.close()

	urls = [url.rstrip('\n') for url in urls]

	names = []

	for url in urls:

        	url = (url.split('/')[-1]).replace('%27', "'")
        	names.append( url.replace('_', " ") )

	
	f = open('api.key','r')
	# get the api key
	key = f.read()
	key = key.rstrip(' \n')
	f.close()
	# client session
	gcl = googlemaps.Client(key=key)

#	read lat longs scraped from wikipedia	
	lat_lon = pd.read_csv('latlon.txt')

	dist_mat = np.zeros((len(names), len(names)))
	time_mat = np.zeros((len(names), len(names)))


	for i, name1 in enumerate(names):
		# cycle through the names
		print i
	
		for j, name2 in enumerate(names[i:]):
			if name1 == name2:
				dist_mat[i][j] = 0.
			try:
				# get the times and dists
				response = googlemaps.distance_matrix.distance_matrix(
                           gcl, tuple(lat_lon.iloc[i].values), tuple(lat_lon.iloc[i+j].values), mode='driving',language='English', units='metric')
		
				dist_mat[i][i+j] = response["rows"][0]["elements"][0]["distance"]["value"]
				time_mat[i][i+j] = response["rows"][0]["elements"][0]["duration"]["value"]
			except:
				print('No Route found between %s and %s' %(name1, name2))
	# save outputs
	np.savetxt("dist.txt", dist_mat + dist_mat.T)
	np.savetxt("time.txt", time_mat + time_mat.T)

