def HashingofT(TableofHash):
    for i in range(len(TableofHash)):
        print(i, end=" ")

        for j in TableofHash[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


# Creating Hashtable as
# a nested list.
TableofHash = [[] for _ in range(10)]


# Hashing Function to return
def Hashing(key):
    return key % len(TableofHash)


# Insert Function to add
# values to the hash table
def insertofval(TableofHash, key, value):
    hash_key = Hashing(key)
    TableofHash[hash_key].append(value)


# Driver Code
insertofval(TableofHash, 11, 'Argentina')
insertofval(TableofHash, 22, 'Canada')
insertofval(TableofHash, 44, 'Australia')
insertofval(TableofHash, 45, 'Poland')
insertofval(TableofHash, 24, 'Iceland')
insertofval(TableofHash, 19, 'Norway')

HashingofT(TableofHash)