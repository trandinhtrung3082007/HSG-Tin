def tímonhonhatkocotrongday(lst):

    if (lst[0] != 0):
        return 0

    if (lst[-1] == len(lst) - 1):
        return len(lst)
     
    first = lst[0]
     
    return findFirstMissing(lst, 0,
            len(lst) - 1, first)
 
def findFirstMissing(lst, start, end, first):
     
    if (start < end):
        mid = int((start + end) / 2)
         
        if (lst[mid] != mid + first):
            return findFirstMissing(lst, start,
                                    mid, first)
        else:
            return findFirstMissing(lst, mid + 1, 
                                    end, first)
     
    return start + first
 

lst = [0, 1, 2, 3, 4, 5, 6, 7, 10]


a = len(lst)

print(tímonhonhatkocotrongday(lst))
    