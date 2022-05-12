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
import returnF as defa

demand_points, candidate_sites, prev_objective_function, sf, r = defa.returnCS()


non_covered_points = list(demand_points)
covered_points = []

selected_sites = []
non_selected_sites = list(candidate_sites)
new_individual_covered = []
new_of = 0
completed = True

for site in non_selected_sites:
    count = 0
    for point in non_covered_points:
        d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
        if d <= r:
            count += 1
            non_covered_points.remove(point)
    new_individual_covered.append([site, count])
    new_of += count

new_individual_covered.sort(key=itemgetter(1), reverse=True)

print("Selected sites:", selected_sites)
print("Non selected sites:", non_selected_sites)
print("Covered points:", covered_points)
print("Non covered points:", non_covered_points)
print("Objective function:", new_of)
print("New SELECTED SITES:", [new_individual_covered[x] for x in range(sf)])
