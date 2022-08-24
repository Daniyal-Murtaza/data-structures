# O(N^2):

lst = input("Enter positive integers ***Example. 2,4,1,3,5***: ").split(",")

def CountInversions(lst):
    
    total = 0
    n = len(lst)
    
    for a in range(n):
        for b in range(a + 1, n):
            if lst[b] < lst[a]:
                total = total + 1
                
    return(total)

print("Number of Inversions:",CountInversions(lst))