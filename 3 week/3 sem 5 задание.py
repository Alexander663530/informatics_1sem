import numpy as np
def spiral(n, m, side, counter):
    


    if side == 'top':

        line = []

        for i in range (counter, counter + m):
                line.append(i)

        if n == 1:
            print(side, [line])
            return [line]
        
        res = spiral(n-1, m, 'right', counter + m)
        print(side, [line] + res)

        return [line] + res
        


    if side == 'right':

        col = []

        if m == 1:
            for i in range (counter, counter + n):
                col += [[i]]
            print(side, col)
            return col

        res = spiral(n, m-1, 'bottom', counter + n)
        for i in range (n):
            res[i].append(counter + i)
        print(side, res)
        return res



    if side == 'bottom':
        line = []
        for i in range (counter + m - 1, counter - 1, -1):
                line.append(i)
        if n == 1:
            print(side, [line])
            
            return [line]
        res = spiral(n-1, m, 'left', counter + m)
        print(side, res + [line])
        return res + [line]



    if side == 'left':
        col = []
        if m == 1:
            for i in range(counter + n - 1, counter - 1, -1):
                col += [[i]]
            print(side, col)
            return col
        res = spiral(n, m-1, 'top', counter + n)
        for i in range (n-1, -1, -1):
            res[n - 1 - i] = [counter + i] + res[n - 1 - i]
            #print(i, res[n - 1 ])
        print(side, res)
        return res

    
        
        
           
   
    
            
n = int(input())
m = int(input())
c = np.array(spiral(n, m, 'top', 1))
print(c)



      



                   
