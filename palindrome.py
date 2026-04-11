n=int(input())
og=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)
if rev==og:
    print('palindrome')
else:
    print('Not palindrome')
