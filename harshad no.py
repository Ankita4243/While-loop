sum=0
num=int(input("Enter the no.:"))
a=num
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
if num%sum==0:
    print(num,"it's is harshad no.")
else:
    print(num,"it's not harshad no.")
    





    # 156=1+5+6=12
    # 156%12==0
    