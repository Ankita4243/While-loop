# write a program to print the factor of number

num=int(input("Enter the number:"))
i=1
while num>0:
    if num%i==0:
        print(i)
    i=i+1


