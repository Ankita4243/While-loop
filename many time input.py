# Take an integer input in a variable named n. Take user input as many times as the value of n.
i=1
sum=0
num=int(input("number of input to be taken:"))
while i<=num:
    n=int(input("enter the number:"))
    sum=sum+n
    i=i+1
print(sum)
