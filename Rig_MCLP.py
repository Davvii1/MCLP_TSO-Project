import numpy as np
import random
import os.path
import time


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

    for y in range(p):
        p_ix = random.randint(0, p)
        p_iy = random.randint(0, p)
        i_file.write(str(p_ix) + ' ' + str(p_iy) + '\n')
    i_file.close()

# Showing the running time OUTPUT
print("-- Running time: " + str(round(time.time() - s_count)) + " seconds --")

