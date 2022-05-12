import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from operator import itemgetter
from numpy.random import default_rng

def returnCS():
    p = 50
    f = 10
    sf = 5
    r = 5


    # Generate Demand points
    dx_points = default_rng().choice(p, size=(p - f), replace=False)
    dy_points = default_rng().choice(p, size=(p - f), replace=False)

    # Generate candidate sites
    csx_points = default_rng().choice(p, size=(f), replace=False)
    csy_points = default_rng().choice(p, size=(f), replace=False)

    # Data to analize
    demand_points = []
    candidate_sites = []

    for x in range(p - f):
        demand_points.append([dx_points[x], dy_points[x]])

    for x in range(f):
        candidate_sites.append([csx_points[x], csy_points[x]])


    # Divide data
    non_selected_sites = list(candidate_sites)
    non_covered_points = list(demand_points)

    of = 0
    selected_sites = []
    covered_points = []
    individual_covered = []

    while len(selected_sites)<sf:
        for site in non_selected_sites:
            if len(selected_sites)>=sf:
                break
            count = 0
            for point in non_covered_points:
                d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
                if d <= r:
                        covered_points.append(point)
                        non_covered_points.remove(point)
                        count += 1
            if count > 0:
                    selected_sites.append(site)
                    non_selected_sites.remove(site)
                    individual_covered.append([site, count])
                    of += count
                    break

    print("Selected sites:", selected_sites)
    print("Non selected sites", non_selected_sites)
    print("Covered points:", covered_points)
    print("Non covered points:", non_covered_points)
    print("Objective function:", of)
    print("Number of points covered by every site:", individual_covered)
    return demand_points, candidate_sites, of, sf, r