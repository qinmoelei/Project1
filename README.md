
# Project 1 for Distrbuted Sysytem
`exp/data.py` contain duration and memory requirement for each funciton (Sampled from Azure Data), the total execution time in one month, the fee for switching funciton, price for running 1 ms second with 1 Gb memory, and configurable memories (from the paper).
# Baselines
Since running function sperately or switching them one by one does not require knowing the DAGs, these baselines are easily calculated. Simply run `python exp/all_merge.py` or `python exp/all_sperate.py` to calculate the time and price for runninig six functions or 10 functions.
# Best solution
Run `python exp/optimze.py` to get the best solution for running six functions or 10 functions. 

Use the `calculate_merge_distance` to calculate the balanced result (average of execution time and price) for merged functions or a single function.

After constructing the graph, use `dijkstra` and `get_shortest_path` to get the shortest path and its corresponding distance