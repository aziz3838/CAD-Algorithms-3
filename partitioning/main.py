'''
Created on Mar 08, 2015

@author: Abdulaziz Alghamdi
'''

from partition import *
import sys, getopt
from os import listdir, path
import time

def main(): 
    start_time = time.time()    

    measurePerformance();
#     measurePerformanceOneBench();

    print("%.1f seconds" % (time.time() - start_time))



'''
This function goes through all benchmarks, and executes Simulated Annealing on each one of them. 
It keeps a record of time for each benchmark. It also shows a graph of the Cost vs. Iterations after EACH benchmark.
The code will STOP until the graph for the current bemchmark is closed.
'''
def measurePerformance():
    benchmarks = listdir("benchmarks")
    totalCost = 0;
    for bench in benchmarks:
        start_time = time.time()
        A = Partition('benchmarks/' + bench)
        localCost, plot, number_of_passes = A.partition()
        print path.splitext(path.basename(bench))[0], "\t", localCost
        totalCost += localCost
        print("%.3f seconds" % (time.time() - start_time))
        
        #graph
        plotting.plot(path.splitext(path.basename(bench))[0], plot, number_of_passes)
    
    print "Overall Average\t", totalCost/len(benchmarks) 



def measurePerformanceOneBench():
    start_time = time.time()
    A = Partition('benchmarks/paira.txt')
    localCost, plot, number_of_passes = A.partition()
    print "Cost\t", localCost
    print("%.3f seconds" % (time.time() - start_time))
    #graph
    plotting.plot("paira", plot, number_of_passes)



main()