#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Searching Algorithm
#1. linear search
def linear_search(list, value):
    size = len(list)
    for i in range (size):
        if list[i] == value:
            return 'value ' + str(value) + ' is at the index ' + str(i)
    return 'value ' + str(value) + ' is not in the list'

#2. binary search // pre-condition : the list must be sorted beforehand
def binary_search(sorted_list, value):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == value:
            return 'value ' + str(value) + ' is at the index ' + str(mid)
        # hint : if value not found, adjust high or low to get a new mid for the next round
        elif sorted_list[mid] > value:
            high = mid - 1
        elif sorted_list[mid] < value:
            low = mid + 1
    
    return 'value ' + str(value) + ' is not in the list'

#3. binary search - recursive approach
def recursive_binary_search(sorted_list, value):

    if len(sorted_list) == 0:
        return 'value ' + str(value) + ' is not in the list'
    else:    
        mid = len(sorted_list) // 2
        if sorted_list[mid] == value:
            return 'value ' + str(value) + ' is in the list'
        elif sorted_list[mid] > value:
            smaller_list = sorted_list[:mid]
            return recursive_binary_search(smaller_list, value)
        elif sorted_list[mid] < value:
            larger_list = sorted_list[mid + 1:]
            return recursive_binary_search(larger_list, value)

# Sorting Algorithm 
#1. bubble sort
#   bubble up - larger items to the top or the end of collection 
#   sink down - smaller items to the bottom or the front of collection
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1, 0, -1):
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

#2. selection sort - select smallest and put it to the current front  
def selection_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n-1):
        smallest_index = i
        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[smallest_index]:
                smallest_index = j
        unsorted_list[i], unsorted_list[smallest_index] = unsorted_list[smallest_index], unsorted_list[i]
        
    return unsorted_list

#3. insertion sort - iterate from index 1 to the last index, 
#   pick up one and store into vatiable so that we can have 
#   a space for former items to move forward one space if needed
def insertion_sort(unsorted_list):
    n = len(unsorted_list)
    for front in range(1, n):
        cur_key = unsorted_list[front]
        while cur_key < unsorted_list[front - 1] and front > 0: 
            unsorted_list[front] = unsorted_list[front - 1]
            front -= 1 
        unsorted_list[front] = cur_key
    return unsorted_list

