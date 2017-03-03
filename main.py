#!/usr/bin/python3

from kmeans import kmeans

if __name__ == "__main__":
    
    n = 5
    d = 1
    k = 2
    
    init_clusters = [[4], [9]]
    data = [[3], [4], [6], [9], [10]]

    kmeans(n, d, k, init_clusters, data)

