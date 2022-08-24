listie = list(map(int, input("Enter list of positive integers i.e. 2 4 1 3 5: ").split()))

def m1(listie):
    
    aa = len(listie)
    a1 = [0]
    bb = a1 * aa
    a2 = aa - 1
    
    return m2(listie, bb, 0, a2)

def m2(listie, bb, cc, dd):     
    
    i = int(0)                     
    if cc < dd:
        
        summ = (cc + dd)
        avg = (summ) // 2    
        h1 = m2(listie, bb, cc, avg) 
        h2 = m2(listie, bb, avg + 1, dd)  
        h3 = m3(listie, bb, cc, avg, dd)    
        i = i + h1   
        i = i + h2
        i = i + h3
        
    return i

def m3(listie, bb, cc, avg, dd):  
      
    x , z , y = cc , cc , avg + 1  
    i = 0
    while x <= avg and y <= dd:    
                    
        if (listie[x] < listie[y]) or (listie[x] == listie[y]):
            bb[z] = listie[x]
            x , z = x + 1 , z + 1
            
            
        elif (listie[x] > listie[y]):
            bb[z] = listie[y]
            i = i + (avg-x + 1)
            y , z = y + 1 , z + 1
            
    while (x < avg) or (x == avg):
        bb[z] = listie[x]
        x , z = x + 1 , z + 1
        
    while (y < dd) or (y == dd):
        bb[z] = listie[y]
        y , z = y + 1 , z + 1
    
    oo = dd+1
    for cc in range(cc, oo):                
        listie[cc] = bb[cc]
    return i

print("No of inversions:",m1(listie))     
