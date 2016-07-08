# Road Tripping
Travelling salesman around Irish landmarks based on Randal Olson's U.S. road trip code.

This code computes an optimal route around 51 Irish landmarks, chosen from here: https://en.wikipedia.org/wiki/List_of_tourist_attractions_in_Ireland. I scraped wikipedia for the latitudes and longitudes of the locations, and then fed those into the Google Maps API to get the distances between all of the locations.

I wanted to get the optimal (minimum) distance for a closed path that visited every site once, which is the classic Travelling Salesman Problem. The core of this problem is that for even a modest number of destinations checking all of the paths between them to find the minimum is infeasible. In this case, for 51 locations, there are ~10<sup>64</sup> differnt possible paths. This is a pretty similar order of magnitude to the number of atoms in all of the stars in the Milky Way. So it's a too many to check, is the point. 

To get around this I began with the simplest solution, the so-called 'greedy' path. That is, beginning from a given place, go to the nearest place that hasn't yet been visited, and repeat this until you're back at the start again. I did this for 50 of the locations, giving 50 different paths. I then passed these into an evolutionary algorithm. This took the best five paths, and generated 10 random offspring from each, where each of the offspring has a random mutation in it. This gave a new 50 paths from which we take the top five again, mutate them, and around and around we go. I did this 5000 times to try to get a decent path. There's not guarantee that this path will be the actual minimum, but it should be pretty good.

The final output can be visualised here: http://www.n-o-r.xyz/road-tripping.html. And here are the places visited in order (the path is a closed loop, so when you get to 51 you can go back to the start, and you can also start anywhere you like):

1. Enniscorthy
2. Avoca
3. Glendalough
4. Wicklow Mountains
5. Dublin
6. Belvedere House and Gardens
7. Strokestown Park
8. Athlone
9. Clonmacnoise
10. Birr Castle
11. Rock of Cashel
12. Cobh
13. Cork
14. Blarney
15. Mizen Head
16. Killarney National Park
17. Dingle
18. Adare
19. Limerick
20. Cliffs of Moher
21. The Burren
22. Galway
23. Connemara
24. Croagh Patrick
25. Sligo
26. Bundoran
27. Lough Erne
28. Enniskillen Castle
29. Ulster American Folk Park
30. Killybegs
31. Glenveagh National Park
32. Malin Head
33. Derry
34. Giant's Causeway
35. Belfast
36. Downpatrick
37. Mourne Mountains
38. Carlingford, County Louth
39. St Patrick's Cathedral, Armagh
40. Monaghan Town
41. Tayto Park
42. Monasterboice
43. The Boyne
44. Newgrange
45. Hill of Tara
46. Russborough House
47. Kildare
48. Rock of Dunamase
49. Brownshill Dolmen
50. Kilkenny
51. Waterford

So there we go. Anyone got a car?
