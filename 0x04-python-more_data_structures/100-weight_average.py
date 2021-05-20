#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        times = 0
        for tup in my_list:
            (score, weight) = tup
            total += (score * weight)
            times += weight
        return (total / times) if times > 0 else 0
    else:
        return 0

# return(sum(a*b for a, b in my_list)/sum(b for a, b in my_list))
