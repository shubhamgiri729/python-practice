#Check if a number is prime

num=7

if num<=1:
    print("Not Prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")