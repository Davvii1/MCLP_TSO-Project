from hashlib import new
from math import sqrt
from operator import itemgetter
import Constructive as constructive
import Plotter as plot

def LocalSearch(demand, candidate, prev_of, sf, r, title, p):

    non_covered_points = list(demand)
    covered_points = []

    selected_sites = []
    non_selected_sites = list(candidate)
    new_individual_covered = []
    new_of = 0

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

    new_selected_sites_w_count = [new_individual_covered[x] for x in range(sf)]
    new_selected_sites = [site[0] for site in new_selected_sites_w_count]
    print("Selected sites:", new_selected_sites)
    print("Non selected sites:", non_selected_sites)
    print("Covered points:", covered_points)
    print("Non covered points:", non_covered_points)
    print("Objective function:", new_of)
    print("Number of points covered by every site:", new_selected_sites_w_count)
    plot.addCirclesToPlot(demand, candidate, new_selected_sites, new_of, title, p, r, "Local Search Heuristic Applied")
    

    if new_of > prev_of:
        print("Solution improved")
    else:
        print("Solution not improved")
