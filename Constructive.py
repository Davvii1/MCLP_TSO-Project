from math import sqrt
import Plotter as plot
import time

def Constructive(candidate, demand, p, f, sf, r):

    # Starting time of constructive
    s_count = time.time()

    # Data to analize
    demand_points = demand
    candidate_sites = candidate

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

    title = "p =" + str(p) + " f =" + str(f) + " sf =" + str(sf) + " r  =" + str(r)

    plot.showInitialPlot(demand_points, candidate_sites, p, title, "InitialPlot.jpg")
    print("Selected sites:", selected_sites)
    print("Non selected sites", non_selected_sites)
    print("Covered points:", covered_points)
    print("Non covered points:", non_covered_points)
    print("Objective function:", of)
    plot.addCirclesToPlot(demand_points, candidate_sites, selected_sites, of, title, p, r, "ConstructiveHeuristicApplied.jpg")

    # Showing the running time
    print("-- Running time Constructive: " + str(round(time.time() - s_count)) + " seconds --")

    return demand_points, candidate_sites, of, sf, r, title, p