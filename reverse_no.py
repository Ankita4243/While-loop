# Write a program to reverse the number accepted by the user.
i=0
num=int(input("Enter the numbers:"))
while num>0:
    a=num%10
    i=i*10+a
    num=num//10
print(i)
