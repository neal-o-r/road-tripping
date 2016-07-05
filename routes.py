

class Route(object):

	def __init__(self, input_list):
		
		self.route = self._make_route(input_list)
	
	def _make_route(self, input_list):

		route = []
		for index, place in enumerate(input_list):

			segment = [place, input_list[index-1]]

			route.append(segment)
		
		return route
		
	def length_of_route(self, dist_mat):

		distance_travelled = 0.
		for i in range(len(self.route)):
	
			from_stop = self.route[i][0]
			to_stop	  = self.route[i][1]
			distance_travelled += dist_mat[from_stop][to_stop]

		return distance_travelled

	def check_equality(self, other_list):

		other_route = self._make_route(other_list)

		if len(other_route) != len(self.route):
			return False

		set1 = []
		set2 = []
		for index, segment in enumerate(self.route):

			set1.append(frozenset(segment))
			set2.append(frozenset(other_route[index]))

		set1 = set(set1)
		set2 = set(set2)

		return set1 == set2
			

