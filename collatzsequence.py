def collatz(n):
    if n%2==0:
        return n//2
    else:
        return n*3+1
num=int(input('Enter the number:'))
while num!=1:
    num=collatz(num)
    print(num)
