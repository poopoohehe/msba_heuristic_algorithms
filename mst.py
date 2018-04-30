# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:25:45 2018

@author: kmcke
"""

def mst_algo(locs,dist):

    my_team_number_or_name = "kcmckee"
    mst = []

    connections = dist.keys()
    connections.sort(key=lambda x: dist[x], reverse=False) #sort connections 
    touched_edges = [] #keep track of connected edges
    edges = 0
    nodes = len(locs)

    def get_connections(x,built_set,touched_edges): #function to determine the connection set for x nodes
        
        built_set.add(x) #add item x to the built set
        temp_set=built_set.copy()#make a copy of the built set

        for tup in touched_edges:
            if x in tup:
                temp_set.add(tup[0])
                temp_set.add(tup[1])

        if temp_set.issubset(built_set):
            
            return built_set

        else: #get the connections for all the vertices connected to x
            missing_values=temp_set.difference(built_set)
            for y in missing_values:
                y_connections = get_connections(y,built_set,touched_edges)
                built_set = built_set.union(y_connections)

            return built_set

    while edges < nodes - 1:
        i = connections[0] #evaluate first item in the list since it is sorted in descending order 
        i0_connects = get_connections(i[0],set(),touched_edges)
        i1_connects = get_connections(i[1],set(),touched_edges)
        if bool(i0_connects.intersection(i1_connects)):
            connections.pop(0)

        else:
            mst.append(i)
            touched_edges.append(i)
            edges+=1
            connections.pop(0)

    return my_team_number_or_name, mst