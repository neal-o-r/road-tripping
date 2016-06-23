import googlemaps
import numpy as np
import seaborn as sns; sns.set()
import pandas as pd

f = open("places.txt", 'r')

urls = f.readlines()

f.close()

urls = [url.rstrip('\n') for url in urls]

names = []

for url in urls:

	url = (url.split('/')[-1]).replace('%27', "'")
	names.append( url.replace('_', "+") )


f = open('api.key','r')

key = f.read()
key = key.rstrip(' \n')
f.close()

gcl = googlemaps.Client(key=key)


lat_lon = pd.read_csv('latlon.txt')

dist_mat = np.zeros((len(names), len(names)))
time_mat = np.zeros((len(names), len(names)))

for i, name1 in enumerate(names):

	print i / float(len(names))

	for j, name2 in enumerate(names[i:]):

		if name1 == name2:
			dist_mat[i][j] = 0.

		try:
			response = googlemaps.distance_matrix.distance_matrix(
                            gcl, name1, name2, mode='driving',language='English', units='metric')
		
			dist_mat[i][i+j] = response["rows"][0]["elements"][0]["distance"]["value"]
			time_mat[i][i+j] = response["rows"][0]["elements"][0]["duration"]["value"]

		except Exception:

			if (lat_lon.iloc[i].values[0] != None):
	
				try:
					response = googlemaps.distance_matrix.distance_matrix(
                            gcl, tuple(lat_lon.iloc[i].values), tuple(lat_lon.iloc[i+j].values), mode='driving',language='English', units='metric')
		
					dist_mat[i][i+j] = response["rows"][0]["elements"][0]["distance"]["value"]
					time_mat[i][i+j] = response["rows"][0]["elements"][0]["duration"]["value"]
				except:
					pass
			else:
				print('No Route found between %s and %s' %(name1, name2))


np.savetxt("output.txt", dist_mat)

