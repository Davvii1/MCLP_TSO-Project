from math import sqrt
import time
import Plotter as plot
from operator import itemgetter

def Constructive(candidate, demand, p, f, sf, r):

    print("-- Initial Plot --")
    title = "p=" + str(p) + " f=" + str(f) + " sf=" + str(sf) + " r=" + str(r)
    plot.showInitialPlot(demand, candidate, p, title, "InitialPlot.jpg")

    print("-- Constructive Heuristic 1 --")
    # Starting time of constructive
    s_count = time.time()

    # Data to analize
    demand_points = demand
    candidate_sites = candidate

    of = 0
    covered_points = []
    individual_covered = []

    # Mayor distance sites
    sites_to_count = []
    for x in range(0, len(candidate_sites)-1, 1):
        d = sqrt((candidate_sites[x][0] - candidate_sites[x+1][0]) ** 2 + (candidate_sites[x][1] - candidate_sites[x+1][1]) ** 2)
        sites_to_count.append([candidate_sites[x], candidate_sites[x+1], d])
    
    sites_to_count.sort(key=itemgetter(2), reverse=True)
    # print(sites_to_count)

    sites_to_analize = []
    for y in range(len(candidate_sites)):
        if len(sites_to_analize)<sf and sites_to_count[y][0] not in sites_to_analize:
            sites_to_analize.append(sites_to_count[y][0])
            if len(sites_to_analize)<sf and sites_to_count[y][1] not in sites_to_analize:
                sites_to_analize.append(sites_to_count[y][1])

    for site in sites_to_analize:
        count = 0
        for point in demand_points:
            d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
            if d <= r and point not in covered_points:
                # print(site, "covers point:", point, ", distance =", d)
                covered_points.append(point)
                count += 1
        individual_covered.append([site, count])
        of += count  
    
    print("Objective function:", of)
    print("Selected sites with count of covered points:", individual_covered)
    plot.addCirclesToPlot(demand_points, candidate_sites, sites_to_analize, of, title, p, r, "Constructive2HeuristicApplied.jpg")

    # Showing the running time
    print(" -- Running time:" + str(time.time() - s_count) + " --")

    return demand_points, candidate_sites, of, sf, r, title, p, individual_covered