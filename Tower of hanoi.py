#Program to move n disks in tower if hanoi
def hanoi(n,a,b,c):
    if n==1:
        print("Move disk 1 from",a,"to",b)
        return
    #move n-1 disk from a to b
    hanoi(n-1,a,b,c)
    print("Move disk",n,"from",a,"to",b)
    hanoi(n-1,c,b,a)
n=4
hanoi(n,"a","c","b")