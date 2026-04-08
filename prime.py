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
        
# Print prime numbers from 1 to n
n = 20
for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")