# Maximal Covering Location Problem
Seeks to maximize the population covered within a desired service distance by locating a fixed number of facilities, provide opportunities to resolve the questions raised.

## Description of the project
We want to maximize the amount of covered sites of different instances with a Constructive Heuristic then improve the solution obtained using a Local Search Algorithm.

## Constructive Heuristic
In this case, we start with an empty solution and iterate the search until a feasible solution is obtained. This implementation of the Greedy Algorithm (GA) receives as input:
* The demand points.
* The number of candidate sites.
* The desired sites to be selected.
* The coverage radius.

## Local Search
First thing the algorithm does is analyze a random site and calculate how many population or demand points cover. Then, when the calculus is done the covered demand points are removed from the non-covered sites set (this is not established in the mathematical model because it was used in this algorithm to improve previous one) so for the next iteration these sites won’t be shown. 

Then, it will iterate until all the sites are covered
Once this is ended, it is important to sort, from the largest to the smallest amount,  all the amount of population covered and select the first selected sites by the size of the input of this. For example, if we want five selected facilities the algorithm only returns the first five largest covered amount of these sites. 

