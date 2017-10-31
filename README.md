# Mathspace Challenge
### Problem
> A robot which can move down and right is traversing some terrain that can be represented as a hex grid. Find the least > cost path from top left to bottom right through such a grid. Return the path for the robot to follow.

#### Sample input
46B E59 EA C1F 45E 63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9C1 461 F74 D05
EDD E94 5F4 D1D D03 DE3
89 925 CF9 CA0 F18 4D2

### Sample output
R,R,D,D,R,D,D,R,R,D

### Approach to solve

At first, I have implemented a recursive approach with the options U,D,R and L. The problem with this approach is the memory footprint to calculate all possibilities(combinations)!!! This approach works fine in the sample input if you only work with R,D once you add more combinations the time take to solve is huge.

My second approach was a prune search, which I have deleted, at this stage, decided to keep track of my calculations. Once I found a path, I stored the result and keep executing the backtracking, now, if my total cost is bigger than the previous found I would abort. This approach was faster, but not enough, his Big O was combinatorial.

After that I realised that dynamic programming could be a solution, but did not found a way to store previous solutions since the I needed a previous computation that was expecting the value from the calculated one.

Finally, I decided to implemented Dijsktra, I was not sure if would work since I could end up in a cycle that was excluded because I keep track of my min cost at each navigation. That implementation is n^2 :)

### Code organization
Map - class that contain the map implementation, knowing the grid, this class is capable of provideding the following information:
 - movement is inside the map
 - cost to move to that position
 - neighbours from a specific location

Robot - class that contains the robot implementaion, when you create a robot you define which algorithm the robot will use to navigate, this approach hides the complexity from the robot, also you need to give a map to the robot to navigate, the start and end position, a robo can provide the following information:
 - retrieve the optimal route, the most cheaper route to achive the destiny
 - the robot can calculate the cheapest route from any to points in the map

Naive, Optimal - these are the algorithm implementations for the robot, which is based on the Strategy Pattern to hide the complexity from the "user"

### Instalation
To run the code you only needs Python 2 or 3.
  - test
```sh
$ make test
```
 - run
```sh
$ make run
```
** A file can be provided, similar to my_grid.txt to calculate based on diferent grid
```sh
$ make run
``` 

 

