from math import sqrt
import time
import Plotter as plot

def Constructive(candidate, demand, p, f, sf, r):

    print("-- Constructive Heuristic 2 --")
    # Starting time of constructive
    s_count = time.time()

    # Data to analize
    demand_points = demand
    candidate_sites = candidate

    of = 0
    selected_sites = []
    covered_points = []
    individual_covered = []

    iteration = 0

    while len(selected_sites)<sf and iteration < len(demand)*100:
        for site in candidate:
            if len(selected_sites)>=sf:
                break
            count = 0
            for point in demand:
                d = sqrt((point[0] - site[0]) ** 2 + (site[1] - point[1]) ** 2)
                if d <= r and point not in covered_points:
                        covered_points.append(point)
                        print(site, "covers point:", point, ", distance =", d)
                        count += 1
            if count > 0 and site not in selected_sites:
                selected_sites.append(site)
                individual_covered.append([site, count])
                of += count
            else:
                iteration += 1

    title = "p=" + str(p) + " f=" + str(f) + " sf=" + str(sf) + " r=" + str(r)

    print("Objective function:", of)
    print("Selected sites with count of covered points:", individual_covered)
    plot.addCirclesToPlot(demand_points, candidate_sites, selected_sites, of, title, p, r, "ConstructiveHeuristicApplied.jpg")

    # Showing the running time
    print(" -- Running time:" + str(time.time() - s_count) + " --")

    return demand_points, candidate_sites, of, sf, r, title, p, individual_covered