

class Route(object):

	def __init__(self, input_list, distance_matrix):
		
		self.dist_mat = distance_matrix
		self.route    = _make_route(input_list)
	
	def _make_route(self, input_list):

		route = []
		for index, place in enumerate(input_list):

			segment = [place, input_list[index-1]]

			route.append(segment)
		
		return route
		
	def length_of_route(self):

		self.distance_travelled = 0.
		for i in range(len(self.route)):
	
			from_stop = self.route[i][0]
			to_stop	  = self.route[i][1]
			self.distance_travelled += self.dist_mat[from_stop][to_stop]

		return self.distance_travelled

	def check_equality(self, other_list):

		other_route = _make_route(other_list)
		
		

