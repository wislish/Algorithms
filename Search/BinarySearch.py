
def binarySearch(sArr, key):
    begin = 0
    end = len(sArr) - 1

    ## Pay attention to the "=" condition!!!!!
    while begin <= end:
        loc = -1
        mid = begin + (end - begin)//2

        if mid > key:
            end = mid -1
        elif mid < key:
            begin = mid +1
        else:
            return mid

    return loc

if __name__ == "__main__":
    print("D")
    binarySearch([1,2,3,4,5,7],-4)
    binarySearch([1,2,3,4,5,7],-3)
