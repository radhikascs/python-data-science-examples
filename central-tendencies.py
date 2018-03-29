from collections import Counter

num_friends = [100,49,41,40,25]

#Calculating mean value
def mean(x):
    return sum(x)/ len(x)

print(mean(num_friends))

#Calculating median value

def median(v):
    n=len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint-1
        high = midpoint
        return(sorted_v[lo]+sorted_v[high])/2

print(median(num_friends))

#Calculating the quantile
def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]


print(quantile(num_friends,0.10))