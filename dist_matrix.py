import wikipedia
import googlemaps
import numpy as np
import seaborn as sns; sns.set()


f = open("places.txt", 'r')

urls = f.readlines()

f.close()

urls = [url.rstrip('\n') for url in urls]

names = []
latlon = []
for url in urls:
	
	url = (url.split('/')[-1]).replace('%27', "'")
	name = url.replace('_', " ") 
	names.append(name)
	a = wikipedia.page(name)
	try:
		latlon.append((a.coordinates))
	except:
		latlon.append(None)
		continue 
	print name
