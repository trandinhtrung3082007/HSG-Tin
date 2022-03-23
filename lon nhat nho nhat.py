def max(a, b, c):
    max = a
    if max < b: max = b
    if max < c: max = c
    return max
    
def min(a, b, c):
    min = a
    if min > b: min = b
    if min > c: min = c
    return min
 
a = float(input())
 
b = float(input())

c = float(input())
 
def main() :
    print( max(a, b, c))

    print( min(a, b, c))

if __name__=="__main__":
    main()
