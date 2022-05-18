from math import sqrt
from operator import itemgetter
import time
import Plotter as plot

def LocalSearch(demand, candidate, prev_of, sf, r, title, p, prev_selected):

    print("-- Local Search Heuristic --")
    # Starting time of constructive
    s_count = time.time()

    covered_points = []
    non_covered_points = list(demand)
    new_individual_covered = []
    selected_to_compare = prev_selected
    moves = 0

    coord_prev_selected = [site[0] for site in selected_to_compare]
    non_selected_sites = [site for site in candidate if site not in coord_prev_selected]

    for site in non_selected_sites:
        count = 0
        for point in non_covered_points:
            d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
            if d <= r and point not in covered_points:
                covered_points.append(point)
                count += 1
                print(site, "covers point:", point, ", distance =", d)
        new_individual_covered.append([site, count])
        for x in range(len(coord_prev_selected)):
            if count>selected_to_compare[x][1]:
                moves += 1
                selected_to_compare[x] = [site, count]
                break

    total_obj = sum(site[1] for site in selected_to_compare)
    covered_points = [point for point in demand if point not in non_covered_points]
    new_selected_sites = [site[0] for site in selected_to_compare]
    non_selected_sites = [site for site in demand if site not in new_selected_sites]


    print("Objective function:", total_obj)
    print("New selected sites with count of covered points:", selected_to_compare)
    print("Moves:", moves)
    plot.addCirclesToPlotLS(demand, candidate, new_selected_sites, coord_prev_selected, total_obj, title, p, r, "LocalSearchHeuristicApplied.jpg")
    
    # Showing the running time
    print(str(time.time() - s_count))
    print(" ")
    # if total_obj > prev_of:
        # print("Solution improved")
    # else:
        # print("Solution not improved")
