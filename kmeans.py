#!/usr/bin/python3
import math
import sys

def kmeans(n, d, k, init_clusters, data):
    
    data_cluster = list()
    ms           = list()

    ms.append(init_clusters)

    # processing data
    
    while True:

        # discover clusters
        for x in range(0, n):
            min_dist       = sys.maxsize
            cluster_assign = 0
            for m in range(0, k):
                dist = distance(data[x], ms[len(ms)-1][m])
                if dist < min_dist:
                    min_dist       = dist
                    cluster_assign = m
            data_cluster.insert(x, cluster_assign)
    

        # save centroids for analysis
        
        new_m = list()
        
        for i in range(0, k):
            data_cluster_temp = list()
            for j in range(0, n):
                if(data_cluster[j] == i):
                    data_cluster_temp.append(data[j])
            new_m.append(calculate_centroid(data_cluster_temp))
        ms.append(new_m)
        
        
        # check if the algorithm may stop
        if(compare(new_m, ms[len(ms)-1])):
            break
                
        print("continuing...")

    print (ms[len(ms)-1])




def distance(a, b):
    
    d = len(a)
    result = 0
    
    for i in range(0, d):
        result += math.sqrt(abs(math.pow(a[i],2) - math.pow(b[i], 2)))
    return result


def calculate_centroid(data):

    result = list()

    n = len(data)
    d = len(data[0])
    
    for i in range(0, d):
        result.insert(i, 0)

    for i in range(0, n):
        for j in range(0, d):
            result[j] += data[i][j]

    for i in range(0, d):
        result[i] /= n

    return result


def compare(list1, list2):

    len1 = len(list1)
    len2 = len(list2)

    if (len1 != len2):
        return False

    for i in range (0, len1):
        if(len1 != len2):
            return False

    return True
