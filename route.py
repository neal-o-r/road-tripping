
Point = complex

with open('data/time.txt') as f:
        contents = f.read().splitlines()

times = [list(map(float, c.split())) for c in contents]

with open('data/names.txt') as f:
        names = f.read().splitlines()

def irish_points():
        with open('data/latlon.txt') as f:
                contents = f.read().splitlines()

        split_line = lambda x: reversed(list(map(float, x.split(','))))
        pts = [Point(*split_line(l)) for l in contents[1:]]
        return pts

ipts = irish_points()
inds = {p:i for i, p in enumerate(ipts)}

class Route(object):

        def __init__(self, path):
                self.path = list(path)

        def length(self):
                return sum(abs(self.path[i - 1] - self.path[i])
                                for i in range(len(self.path)))
        def time(self):
                return sum(times[inds[self.path[i-1]]][inds[self.path[i]]]
                                for i in range(len(self.path)))

        def __len__(self):
                return len(self.path)

        def __getitem__(self, key):
                return self.path[key]

        def __repr__(self):
                return str(self.path)

        def __str__(self):
                return self.path

        def __eq__(self, other):
                if not isinstance(self, other.__class__):
                        return False

                if not self.path[0] in other.path:
                        return False

                i = other.path.index(self.path[0])
                rotate = other.path[i:] + other.path[:i]
                return (self.path == rotate or
                        self.path == [rotate[0]] + rotate[1:][::-1])
