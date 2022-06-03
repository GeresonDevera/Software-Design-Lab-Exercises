def multiply(x,y):
    if  y == 0 :
        return 0
    elif y < 0:
        return -(x - multiply(x,y+1))
    else:
        return x + multiply(x,y-1)

if __name__ == '__main__':
    print("3 + 2 = " ,multiply(3,2))
    print("3 + (-2) = ",multiply(3,-2))
    print("(-3) + 2 = ",multiply(-3,2))
    print("(-3) + (-2)= ",multiply(-3,-2))