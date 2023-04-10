str1=input("Enter a string")
fl1=float(input("Enter a float number"))
num1=int(input("Enter an integer"))

print(str1,fl1,num1)
print(str1,fl1,num1,sep=":")

print(str1,fl1,num1,end=" ")
print(str1,fl1,num1)

print("fl1=%0.2f" %fl1)
print("num1=%8d" %num1)
print("num1=%-8d" %num1)

"""
Output:
Enter a string XYZ
Enter a float number 19.473
Enter an integer 190
Raghav 19.473 190
Raghav:19.473:190  #seperator between variables changed to ‘:’
Raghav 19.473 190 Raghav 19.473 190  #seperator between two print statement changed to " "
fl1=19.47 #as the format is 0.2 value is rounded of two decimal digits
num1=        190 #right aligned within the reserved 8 spaces 
num1=190         #left aligned within the reserved 8 spaces as there is – symbol
"""