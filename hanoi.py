def hanoi(n, a, b, c):
    if n == 1:
        print("move top disk from " + a + " to " + c)
        return
    hanoi(n-1, a, c , b)
    print("move top disk from " + a + " to " + c )
    hanoi (n-1,b,a,c)

hanoi(4,"a","b","c")