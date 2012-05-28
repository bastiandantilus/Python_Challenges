import random

jj = 0   
for nn in range(1,1000):
    x = 0
    n=1000
    for i in range(n):
        y = [0, 0, 0, 0]
        for j in range(12):
            y[random.randrange(0,4)] += 1
        if 0 in y:
            x += 1
            #print( y)
    jj += x / n
    print( 1 - x / n, 1 - jj / nn)

    #0.875

    p(R|X) * P (X) / P(R)
    
    
    
