# Selected sites: [[8, 47], [24, 21], [19, 27], [3, 17], [6, 30]]
# Non selected sites [[48, 13], [15, 29], [0, 3], [21, 24], [5, 19]]
# Covered points: [[9, 43], [5, 49], [25, 23], [23, 29], [2, 19], [4, 31]]
# Non covered points: [[21, 16], [43, 25], [12, 11], [3, 36], [0, 42], [18, 3], [19, 47], [16, 18], [47, 27], [30, 15],
# [24, 10], [34, 13], [31, 0], [37, 45], [42, 6], [14, 24], [10, 2], [27, 28], [29, 14], [13, 40], [11, 32], [20, 9], [7, 12],
# [45, 48], [17, 39], [22, 8], [36, 7], [6, 41], [39, 34], [41, 26], [28, 4], [33, 21], [1, 37], [32, 20]]
# Objective function: 6

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from operator import itemgetter
from numpy.random import default_rng


demand_points = [[27, 21], [29, 24], [19, 20], [31, 27], [16, 22], [24, 28], [37, 17], [21, 0], [18, 3], [12, 41], [11, 44], [3, 40], [32, 7], [38, 47], [39, 5], [25, 45], [33, 37], [13, 16], [0, 8], [
    1, 4], [8, 10], [36, 39], [44, 12], [30, 49], [6, 1], [9, 34], [10, 35], [46, 31], [43, 42], [42, 14], [4, 6], [45, 19], [40, 18], [7, 25], [35, 48], [14, 23], [28, 46], [17, 13], [47, 43], [49, 15]]

candidate_sites = [[24, 20], [30, 19], [16, 3], [3, 45], [
    27, 4], [20, 36], [7, 15], [42, 5], [17, 24], [0, 41]]

non_covered_points = list(demand_points)
covered_points = []

selected_sites = []
non_selected_sites = list(candidate_sites)
new_individual_covered = []
individual_covered = [[[24, 20], 6], [[30, 19], 1],
                      [[16, 3], 2], [[3, 45], 3], [[27, 4], 1]]
prev_objective_function = 13
sf = 5
r = 10
new_of = 0
completed = True

title = "p = " + str(50) + " f = " + str(10) + \
    " sf = " + str(sf) + " r  =" + str(r)

S = len(new_individual_covered)
cs = len(candidate_sites)

while S < cs:
    for site in candidate_sites:
        count = 0
        for point in demand_points:
            d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
            if d <= r:
                count += 1
                non_selected_sites.remove(point)
                selected_sites.append(point)
        new_individual_covered.append([site, count])
        break



print("Selected sites:", selected_sites)
print("Non selected sites:", non_selected_sites)
print("Covered points:", covered_points)
print("Non covered points:", non_covered_points)
print("Objective function:", new_of)
print("Number of points covered by every site:", individual_covered)
print("New SELECTED SITES:", new_individual_covered)
