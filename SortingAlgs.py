# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:42:32 2019

@author: NATE

This script includes a collection of sorting algorithms. To use a specific 
one, and see its efficiency, uncomment the associated code at the end of the
file.
"""

from timeit import default_timer as timer
import random
import math

unsorted = random.sample(range(1,101),100)

def bubblerecur(the_list):
    temp_list = the_list[:]
    swapper(the_list,0)
    if temp_list == the_list:
        return the_list
    else:
        bubblerecur(the_list)
        return the_list

#swapper is a function for bubblerecur to work
def swapper(the_list, key):
    if len(the_list) < (key+ 2):
        return the_list
    if the_list[key] > the_list[key + 1]:
        item = the_list[key]
        the_list[key] = the_list[key + 1]
        the_list[key + 1] = item
        the_list = swapper(the_list, key + 1)
    else:
        the_list = swapper(the_list, key + 1)



def insertionsort(thelist):
    temp_list = thelist[:]
    for j in range(1,len(temp_list)):
        key = temp_list[j]
        i = j-1 
        while i>-1 and temp_list[i]>key:
            temp_list[i+1] = temp_list[i]
            i= i-1
        temp_list[i+1] = key    
    return temp_list  


def selectionsort(thelist):
    temp_list = thelist[:]
    for j in  range(0,len(temp_list)-1):
        key = temp_list[j]
        replacement = j
        for i in range(j+1, len(temp_list)):
            if key > temp_list[i]:
                replacement = i
                key = temp_list[i]
        temp_list[replacement] = temp_list[j]
        temp_list[j] = key
    return temp_list         

     
def bubblesort(thelist):
    temp_list = thelist[:]
    swaps = True
    q=1
    while swaps == True:
        swaps = False
        for i in range(0,len(temp_list)-q):
            if temp_list[i] > temp_list[i+1]:
                key = temp_list[i]
                temp_list[i] = temp_list[i+1]
                temp_list[i+1] = key
                swaps = True
        q = q+1
    return temp_list


def combsort(thelist):
    
    comb_length = len(thelist)
    temp_list = thelist[:]
    swaps = True
    q=1
    shrink_factor = 1.3
    while swaps == True:
        if comb_length > 1:
            for i in range(0,len(temp_list)-comb_length):
                if temp_list[i] > temp_list[i+comb_length]:
                    key = temp_list[i]
                    temp_list[i] = temp_list[i+comb_length]
                    temp_list[i+comb_length] = key
            comb_length = math.floor(comb_length/(shrink_factor))
            
        else:
            swaps = False
            for i in range(0,len(temp_list)-q):
                if temp_list[i] > temp_list[i+1]:
                    key = temp_list[i]
                    temp_list[i] = temp_list[i+1]
                    temp_list[i+1] = key
                    swaps = True
            q = q+1
    return temp_list



def quicksort(temp_list, low, high):
    if low < high:
        p = partition(temp_list,low,high)
        quicksort(temp_list,low,p-1)
        quicksort(temp_list,p+1,high)
    return temp_list

#Partition is a function for quicksort to work
def partition(temp_list,low,high):
    pivot = temp_list[high]
    i = low
    for j in range(low,high):
        if temp_list[j] < pivot:
            key = temp_list[i]
            temp_list[i] = temp_list[j]
            temp_list[j] = key
            i = i+1
    key = temp_list[i]
    temp_list[i] = temp_list[high]
    temp_list[high] = key
    return i


#RECURSIVE BUBBLE SORT. WARNING: DO NOT EXCEED 1000 ITEMS OR THE RECURSION
#DEPTH WILL BE EXCEEDED
# =============================================================================
# start = timer()
# bubble_sorted = bubblerecur(unsorted)       
# end = timer()
# print('Recursive bubble sort time: ' + str(end-start))
# =============================================================================


#SELECTION SORT
# =============================================================================
# start = timer()
# selection_sorted = selectionsort(unsorted)
# end = timer()
# print('selection sort time: ' + str(end - start))
# =============================================================================


#INSERTION SORT
# =============================================================================
# start = timer()
# insertion_sorted = insertionsort(unsorted)
# end = timer()
# print('insertion sort time: ' + str(end - start))
# =============================================================================


#BUBBLE SORT
# =============================================================================
# start = timer()
# bubble_sorted = bubblesort(unsorted)
# end = timer()
# print('bubble sort time: ' + str(end-start))
# =============================================================================


#COMB SORT
# =============================================================================
# start = timer()
# comb_sorted = combsort(unsorted)
# end = timer()
# print('comb sort time: ' + str(end-start))
# =============================================================================
   

#QUICK SORT
# =============================================================================
# start = timer()
# quick_sorted = quicksort(unsorted,0,len(unsorted)-1)
# end = timer()
# print('quick sort time: ' + str(end-start))
# =============================================================================
