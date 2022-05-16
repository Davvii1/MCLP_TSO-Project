from math import sqrt
from operator import itemgetter
import time
import Plotter as plot

def LocalSearch(demand, candidate, prev_of, sf, r, title, p):

    # Starting time of constructive
    s_count = time.time()

    covered_points = []
    non_covered_points = list(demand)
    non_selected_sites = list(candidate)
    new_individual_covered = []

    for site in non_selected_sites:
        count = 0
        for point in non_covered_points:
            d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
            if d <= r and point not in covered_points:
                covered_points.append(point)
                count += 1
                print(site, "covers point:", point, ", distance =", d)
        new_individual_covered.append([site, count])

    new_individual_covered.sort(key=itemgetter(1), reverse=True)
    new_selected_sites_w_count = [new_individual_covered[x] for x in range(sf)]
    new_selected_sites = [site[0] for site in new_selected_sites_w_count]
    new_selected_w_obj = [site[1] for site in new_selected_sites_w_count]
    total_obj = sum(new_selected_w_obj)
    covered_points = [point for point in demand if point not in non_covered_points]
    non_selected_sites = [site for site in candidate if site not in new_selected_sites]

    print(total_obj)
    print("New selected sites with count of covered points:", new_selected_sites_w_count[:sf])
    plot.addCirclesToPlot(demand, candidate, new_selected_sites, total_obj, title, p, r, "LocalSearchHeuristicApplied.jpg")
    
    # Showing the running time
    print(str(time.time() - s_count))
    print(" ")
    if total_obj > prev_of:
        print("Solution improved")
    else:
        print("Solution not improved")
