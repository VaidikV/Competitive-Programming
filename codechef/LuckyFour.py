t = int(input())

for i in range(t):
    
    fours = 0
    n = str(input())
    
    for s in n:
        
        if int(s) == 4:
            fours += 1
            
    print(fours)
