print("\nThe tower of hanoi solution: ")
def TOH(j, Another, to_another, fixed_another):

    if j == 0:
        return
    else:

        TOH(j - 1, Another, fixed_another, to_another)
        print("\nYou must move the disk", j, "from rod", Another, "to rod", to_another)
        TOH(j - 1, fixed_another, to_another, Another)

j = 4
TOH(j, '1', '2', '3')