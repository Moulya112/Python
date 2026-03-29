str=input()
c=True
for i in str:
    if i  not in 'AEIOUaeiou':
      c=False
      print('constant found',i)
if c:    
   print('constant is not found')
