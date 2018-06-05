from route import Route, Point, ipts, times, inds, names
import random
from itertools import permutations
import matplotlib.pyplot as plt

n = 10

def rand_points(n):
        return [Point(random.randint(0, 100),
                      random.randint(0, 100)) for i in range(n)]

def nonred_permutations(pts):
        head, *tail = pts
        return [[head] + list(p) for p in permutations(tail)]

def exhaustive(pts):
        return min((Route(i) for i in nonred_permutations(pts)),
                        key=lambda x: x.length())

def greedy(pts, route):
        if not pts:
                return route

        #p = min(pts, key=lambda x: abs(route[-1] - x))
        p = min(zip(pts, times[inds[route[-1]]]), key=lambda x: x[1])[0]
        i = pts.index(p)
        return greedy(pts[:i] + pts[i+1:], route + [p])


def plot_path(route):
        for i in range(len(route)):
                plt.plot(route[i].real, route[i].imag, 'ok', zorder=10)
                plt.plot((route[i].real, route[i-1].real),
                         (route[i].imag, route[i-1].imag), c='0.8', alpha=0.8)
        plt.axis('off')
        plt.show()


def subsegments(N):
    return [(i, i + length)
            for length in reversed(range(2, N))
            for i in reversed(range(N - length + 1))]


def try_swaps(route_in):
        post_swap = swap_points(route_in)
        if post_swap == route_in:
                return post_swap
        else:
                return try_swaps(post_swap)


def swap_points(r):
        min_l = r.length()
        p = r.path[:]
        for s in swaps:
                i, j = s
                j = j % len(p)
                p[i:j] = reversed(p[i:j])
                if Route(p).length() < min_l:
                        r = Route(p)
                        min_l = r.length()
                else:
                        p = r.path[:]

        return r
pts = rand_points(9)
swaps = subsegments(9)
o = try_swaps(Route(pts))
'''
g = Route(greedy(ipts[1:], [ipts[0]]))
swaps = subsegments(len(ipts))
opt = try_swaps(g)
plot_path(opt)
with open('optimal_route_time.txt', 'w') as f:
        for p in opt:
                f.write(f'"{p.imag},{p.real}",\n')
'''
