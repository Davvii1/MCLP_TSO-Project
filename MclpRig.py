import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
from math import sqrt

p = 500
p_min = 1
p_max = 300
f = 50
sf = 10
r = 10

# Demand Points
xg_points = np.random.randint(low=p_min, high=p_max, size=(p - f))
yg_points = np.random.randint(low=p_min, high=p_max, size=(p - f))
# Facility Points
xc_points = np.random.randint(low=p_min, high=p_max, size=f)
yc_points = np.random.randint(low=p_min, high=p_max, size=f)

plt.title("p = 500, p_min = 1, p_max = 300, f = 50, sf = 10, r = 10")
plt.suptitle('Random Generated Demand and Candidate Points')
if p >= 100:
    ms = 5
else:
    ms = 30
plt.scatter(xg_points, yg_points, c='black', s=ms)
plt.scatter(xc_points, yc_points, c='red', s=ms + 10)
plt.savefig("firstg.png")
plt.show()

selected = []
covered = []
e_point = False
of = 0
for site in range(f):
    of = len(covered)
    if of <= p:
        c1 = True
    else:
        c1 = False
    if len(selected) < sf:
        c2 = True
    else:
        c2 = False
    for y in range(p - f):
        d = sqrt((xc_points[site] - xg_points[y]) ** 2 + (yc_points[site] - yg_points[y]) ** 2)
        print('analizing: ' + str(xc_points[site]) + ',' + str(yc_points[site]) + ': ' + str(d))
        if d <= r:
            e_point = True
            if [xg_points[y], yg_points[y]] in covered:
                pass
            else:
                covered.append([xg_points[y], yg_points[y]])
    if c1 and c2 and e_point:
        selected.append([int(xc_points[site]), int(yc_points[site])])

xsf, ysf = zip(*selected)
ax = plt.gca()
plt.title("p = 500, p_min = 1, p_max = 300, f = 50, sf = 10, r = 10")
plt.suptitle('Random Generated Demand and Candidate Points')
plt.scatter(xg_points, yg_points, c='black', s=ms, label='Demand Points')
plt.scatter(xc_points, yc_points, c='red', s=ms + 10, label='Facility Points')
for i in range(len(selected)):
    x = xsf[i]
    y = ysf[i]
    circle = plt.Circle((x, y), r, color='blue', fill=False, lw=2)
    ax.add_artist(circle)
    ax.axis('equal')
# plt.scatter(xsf, ysf, marker='o', edgecolors='blue', facecolors="none", s=)
plt.xlabel('Objective Function: ' + str(of))
plt.savefig("secondg.png")
plt.show()
print(selected)
print(of)
