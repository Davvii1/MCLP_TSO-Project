from numpy.random import default_rng
import random
import os.path
import time

def runRIG():
    k = int(input("Instances to be generated: "))

    # Asking for items, min and max values 
    p = int(input("Number of demand points:"))
    f = int(input("Number of candidate sites:"))
    sf = int(input("Number of selected candidate sites:"))
    r = int(input("Radius to cover:"))

    # Starting time of file creation
    s_count = time.time()

    for x in range(k):
        # Get new isntance path
        p_files = len(os.listdir(os.path.dirname(__file__) + '/instances'))
        path = os.path.join(os.path.dirname(__file__) + '/instances', 'instance#' + str(p_files + 1) + '.txt')

        # Open instance path
        i_file = open(path, 'w')
        print('instance#' + str(p_files + 1) + '.txt' + " successfully generated")

        # Write first line of file with p, f, sf and r
        i_file.write(str(p) + ' ' + str(f) + ' ' + str(sf) + ' ' + str(r) + '\n')

        # Generate Demand points
        dx_points = default_rng().choice(p, size=(p - f), replace=False)
        dy_points = default_rng().choice(p, size=(p - f), replace=False)

        # Generate candidate sites
        csx_points = default_rng().choice(p, size=(f), replace=False)
        csy_points = default_rng().choice(p, size=(f), replace=False)

        # Store candidate sites and demand points in lists
        demand_points = []
        candidate_sites = []

        for x in range(p - f):
            demand_points.append([dx_points[x], dy_points[x]])

        for x in range(f):
            candidate_sites.append([csx_points[x], csy_points[x]])

        # Write candidate sites and demand points to file
        for candidate in candidate_sites:
            i_file.write(str(candidate[0]) + ' ' + str(candidate[1]) + '\n')

        for point in demand_points:
            i_file.write(str(point[0]) + ' ' + str(point[1]) + '\n')

        # Close file
        i_file.close()

    # Showing the running time OUTPUT
    print("-- Running time: " + str(round(time.time() - s_count)) + " seconds --")

