def max(list):
    if(len(list) == 1):
        return list[0]
    else:
        maxValue = max(list[1:])
    if(maxValue < list[0]):
        maxValue = list[0]
    return maxValue

list = [3,5,21,20,20]
maxval = max(list)
print(maxval)