str=input()
c=True
for i in str:
    if i  in 'AEIOUaeiou':
      c=False
      print('vowel found',i)
if c:    
   print('vowel is not found')
