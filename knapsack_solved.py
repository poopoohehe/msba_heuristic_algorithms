# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:45:41 2018

@author: kmcke
"""
    #Solves the knapsack problem by finding the most valuable
    #subsequence of `items` subject that weighs no more than maxweight`.

    #`items` is a sequence of pairs `(value, weight)`, where `value` is
    #a number and `weight` is a non-negative integer.

    #`maxweight` is a non-negative integer.

    #Return a pair whose first element is the sum of values in the most
    #valuable subsequence, and whose second element is the subsequence.
    
my_team_name_or_number="kcmckee"
things= {0:(1, 1), 1:(1, 2), 2:(1, 3), 3:(1, 4), 4:(1, 5)}
knapsack_cap=4

def knapsack(things, knapsack_cap):
    def bestvalue(i, j):
        if i == 0: return 0
        weight, value = things.values()[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)

#this section creates the result list using the best results from the preceding section
    j = knapsack_cap
    result = []
    for i in xrange(len(things), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            #result.append(items.values()[i - 1]) #appends the optimal value tuples
            #result.append(items.items()[i-1]) #appends the optimal tuple key and value
            #result.append(items[i-1]) #appends the correct tuple key
            result.append(things.items()[i-1][0])
            j -= things.values()[i - 1][0]
            
            
    result.reverse()  
    #return bestvalue(len(things), knapsack_cap),result #returns the sum of the values of the optimal tuples where the tuples are in the form, value, weight
    return my_team_name_or_number,result
print(knapsack(things,knapsack_cap))

#made with help from www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Dynamic/knapsackdyn.htm
