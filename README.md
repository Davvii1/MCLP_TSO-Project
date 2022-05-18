# Maximal Covering Location Problem
Seeks to maximize the population covered within a desired service distance by locating a fixed number of facilities, provide opportunities to resolve the questions raised.

## Description of the project
We want to maximize the amount of covered sites of different instances with a Constructive Heuristic then improve the solution obtained using a Local Search Algorithm.

## Constructive Heuristic No. 1
In this case, we start with an empty solution and iterate the search until a feasible solution is obtained.

(1) The iteration will stop until it is greater than the desired number of facilities.
(2) Compare the distance of a pair of coordinates of the candidate sites, this is done with one point and the next that is within the set, that is, the first with the second, second with the third, so on until the end of reading all points.
(3) In case the desired number of sites is a prime number, the last points that fit within this value will be added, since remembering that pairs of coordinates are taken into account to evaluate which is the furthest.

This implementation of the Greedy Algorithm (GA) receives as input:
* The demand points.
* The number of candidate sites.
* The desired sites to be selected.
* The coverage radius.

## Constructive Heuristic No. 2
As same as the previous heuristic, we start with an empty solution and iterate it by searching the Euclidean distance for every site to every demand point, so given a radius it will return all the points that one of the candidate facilities can cover, this will iterate until we satisfy the amount of desired facilities. 

In this Constructive Heuristic, we get the first selected facilities regardless of the number of sites covered, then get the total and return it as the objective function (feasible solution of covering).   

This implementation receives the same input as Constructive Heuristic No. 1:
* The demand points as I.
* The number of candidate sites as J
* The desired sites to be selected as S
* The coverage radius

## Local Search
The first thing the algorithm does is analyze a site and calculate how many population or demand points cover. Then, when the calculus is done the covered demand points are removed from the non-covered sites set so for the next iteration these sites won’t be calculated. Then, it will iterate until all the sites are covered.

Once this is ended, it is important to sort, from the largest to the smallest amount,  all the amount of population covered and select the first selected sites by the size of the input of this. To finish this algorithm, we compare the previously selected sites with the sorted new selected sites, replacing the previously selected site if the new sorted site covers more demand points.


