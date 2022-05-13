from math import sqrt
from operator import itemgetter
import Plotter as plot
import time

def LocalSearch(demand, candidate, prev_of, sf, r, title, p):

    # Starting time of constructive
    s_count = time.time()

    non_covered_points = list(demand)
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
    covered_points = [point for point in demand if point not in non_covered_points]
    non_selected_sites = [site for site in candidate if site not in new_selected_sites]

    print("Selected sites:", new_selected_sites)
    print("Non selected sites:", non_selected_sites)
    print("Covered points:", covered_points)
    print("Non covered points:", non_covered_points)
    print("Objective function:", new_of)
    plot.addCirclesToPlot(demand, candidate, new_selected_sites, new_of, title, p, r, "LocalSearchHeuristicApplied.jpg")
    
    # Showing the running time
    print("-- Running time Local Search: " + str(time.time() - s_count) + " seconds --")

    if new_of > prev_of:
        print("Solution improved")
    else:
        print("Solution not improved")
