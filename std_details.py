Name=str(input("Enter name:"))
USN=int(input("Enter USN:"))
MS1=float(input("Enter marks of S1:"))
MS2=float(input("Enter marks of S2:"))
MS3=float(input("Enter marks of S3:"))

total_marks=MS1+MS2+MS3
percent=((total_marks)/300)*100

print("***STUDENT DETAILS***")
print("NAME:",Name)
print("USN:",USN)
print("TOTAL_MARKS:",total_marks)
print("PERCENTAGE:",percent)
