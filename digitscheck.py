#      CHECKING DIGITS OF NUM
NUM=int(input('Enter the NUM:'))
if NUM>=10 and NUM<=99:
    print('TWO DIGIT NUM')
elif NUM>=100 and NUM<=999:
    print('THREE DIGIT NUM')
else:
    print('Neither TWO DIGIT NUM nor THREE DIGIT NUM')

