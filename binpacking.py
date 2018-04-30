# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:11:05 2018

@author: kmcke
"""

def binpack(articles, bin_cap):
    article_items=articles.items()
    article_items_sorted=sorted(article_items,key=lambda x:x[1],reverse=True)
    
    list_bins = []
    my_bin=[]
    my_team_number_or_name = "kcmckee"
    
    for key,weight in article_items_sorted:
            alloc_flag = False
            for my_bin in list_bins:
                alternates=my_bin[0::2]
                if sum(my_bin) + weight-sum(alternates) <= bin_cap:
                        my_bin.extend((key,weight))
                        alloc_flag=True
                        break
                        
            if alloc_flag == False:
                newBin = []
                newBin.extend((key,weight))
                list_bins.append(newBin)
                
    for i in range(len(list_bins)):         
        del list_bins[i][1::2]
    bin_contents=list_bins
       
    return my_team_number_or_name, bin_contents     