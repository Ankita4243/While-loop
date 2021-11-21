# 17. Write a program to check whether a number is Armstrong or not.
#  (Armstrong number is a number that is equal to the sum of cubes of its digits,
#   for example : 153 = 1^3 + 5^3 + 3^3.)
  
  
num=int(input("Enter the number:"))
i=num
sum=0
while i>0:
    digit=i%10
    sum+=digit**3
    i=i//10
if num==sum:
    print(sum,"it's armstrong number")
else:
    print(sum,"it's not armstrong number")

4