#      SIMPLE CALCULATOR
num1=int(input('Enter the value for num1:'))
num2=int(input('Enter the value for num2:'))

print('1. Add')
print('2. Sub')
print('3. Multi')
print('4. Div')

choice=int(input('Enter the op num(1-4): '))
if choice==1:
           print("Result=", num1+num2)
elif choice==2:
           print("Result=", num1-num2)

elif choice==3:
           print("Result=", num1*num2)

elif choice==4:
           print("Result=", num1/num2)
else:
           print("INVALLID OP NUM")
