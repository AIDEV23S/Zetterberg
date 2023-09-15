def medelvarde(a):
    sum=0
    for i in range(0,len(a)):
        sum = sum +a[i]
    return sum/len(a)

def median(x, y):
    a = [*range(x,y)]
    a = (len(a))/2
    return a
    

