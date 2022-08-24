# Part a:
import os
def readfile(filename):
    a = open(filename)
    b = a.read().split("\n")
    return b
# print(readfile("file1.txt"))

# Part B:
def WordsFromLineList(listie):
    a = str()
    for i in listie:
        for j in i.lower():
            if j not in "abcdefghijklmnopqrstuvwxyz":
                a += " "
            else:
                a += j
    return a.split()   
#print(WordsFromLineList(readfile("file1.txt")))

#Part C:
from collections import Counter
def countFrequency(listie):
	dict_1 = {}
    for i in listie:
        dict_1[i] == 0
    for i in listie:
        dict_1[i] += 1
    list_items = list(dict_1.items())
    return list_items

#print(countFrequency(WordsFromLineList(readfile("file1.txt")))) 

# Part D:

def mergesort(ls, key=lambda x: x):
    
    if len(ls) < 2:
        return ls
    
    mid = len(ls) // 2
    
    lll = arr[:mid]
    rrr = arr[mid:]
    
    mergesort(lll) 
    mergesort(rrr)
    
    i = 0
    j = 0
    k = 0
    
    while i < len(lll) and j < len(rrr):
        
        if key(lll[i]) < key(rrr[j]):
            ls[k] = lll[i]
            i = i + 1
            
        if key(lll[i]) > key(rrr[j]) or key(lll[i]) == key(rrr[j]):
            ls[k] = rrr[j]
            j  = j + 1
        k = k +  1
        
    while i < len(lll):
        ls[k] = lll[i]
        i , k = i + 1 , k + 1
        
    while j < len(rrr):
        ls[k] = rrr[j]
        j , k = j + 1 , k + 1
        
    return ls







