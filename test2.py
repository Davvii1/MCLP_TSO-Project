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


demand_points = [[26, 40], [22, 43], [37, 13], [20, 41], [7, 15], [14, 23], 
[49, 8], [34, 29], [1, 33], [4, 7], [28, 17], [11, 36], [19, 30], [31, 39], [9, 34], 
[0, 14], [8, 42], [40, 1], [30, 25], [44, 19], [41, 38], [3, 46], [12, 32], [38, 16], 
[39, 26], [42, 45], [23, 4], [45, 5], [18, 44], [6, 37], [16, 10], [35, 20], [32, 0], 
[46, 11], [36, 27], [33, 21], [48, 49], [25, 9], [15, 35], [10, 47]]

candidate_sites = [[25, 40], [40, 10], [22, 41], [11, 15], [10, 21], [32, 44], [15, 16], [46, 37], [2, 33], [13, 48]]

non_covered_points = list(demand_points)
covered_points = []

selected_sites = [[25, 40], [40, 10], [22, 41], [11, 15], [10, 21]]
non_selected_sites = [[32, 44], [15, 16], [46, 37], [2, 33], [13, 48]]
new_selected_sites = []
individual_covered = [[[25, 40], 2], [[40, 10], 1], [[22, 41], 1], [[11, 15], 1], [[10, 21], 1]]
prev_objective_function = 6
sf = 5
r = 5
new_of = 0
completed = True

title = "p = " + str(50) + " f = " + str(10) + " sf = " + str(sf) + " r  =" + str(r)

for x in range(sf):
    for selected in individual_covered:
        if len(new_selected_sites)>=sf:
            completed = False
        count = 0
        for no_selected in non_selected_sites:
            for point in non_covered_points:
                d = sqrt((point[0] - no_selected[0]) ** 2 + (no_selected[1] - point[1]) ** 2)
                if d <= r and completed:
                    covered_points.append(point)
                    non_covered_points.remove(point)
                    count += 1
            if count > selected[1] and completed:
                non_selected_sites.append(selected[0])
                selected_sites.remove(selected[0])
                selected_sites.append(no_selected)
                new_selected_sites.append(no_selected)
                non_selected_sites.remove(no_selected)
                new_of += count
                break


print("Selected sites:", selected_sites)
print("Non selected sites:", non_selected_sites)
print("Covered points:", covered_points)
print("Non covered points:", non_covered_points)
print("Objective function:", new_of)
print("Number of points covered by every site:", individual_covered)
print("New SELECTED SITES:", new_selected_sites)