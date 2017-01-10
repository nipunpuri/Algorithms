# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:46:06 2017

@author: nipun
"""

def Search(L , e):
    
    def bSearch(L , e , low , high):
        #The decrementing function is high - low
        if high == low: #Base case, when there is only one element left
            return L[low] == e #Check if this is the element we're looking for or not.
        mid = (high+low)//2 #Integer division
        
        if L[mid] == e:
            return True
        
        elif L[mid] > e:
            if low == mid: #Nothing left to search
                return False
            else:
                return bSearch(L , e , low , mid - 1)
        elif L[mid] < e: #Could have used just else here too
            return bSearch(L , e , mid+1 , high)
    #The function definition of bSearch ends        
    if len(L) == 0:
        return False
    else:
        return bSearch(L , e , 0 , len(L) - 1)