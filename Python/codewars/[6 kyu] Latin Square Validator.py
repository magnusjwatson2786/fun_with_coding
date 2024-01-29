'''https://www.codewars.com/kata/646254375cee7a000ffaa404'''

def verify_latin_square(arr, m):
    for _ in arr:
        if len(_)!=len(arr):
            return  "Array not square"
    if len(arr)!=m:
        return "Array is wrong size"
    for i in arr:
        for j in i:
            if i.count(j)>1:
                return str(j)+" occurs more than once in row "+ str(arr.index(i)+1)
            if j>m or j<1:
                return str(j)+" at "+str(arr.index(i)+1)+","+str(i.index(j)+1)+" is not between 1 and "+str(m)
            
    zarr=list(zip(*arr))
    
    for i in zarr:
        for j in i:
            if i.count(j)>1:
                return str(j)+" occurs more than once in column "+ str(zarr.index(i)+1)
                
    return "Valid latin square of size "+str(m)
