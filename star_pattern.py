'''
Print: Right Triangle

*
**
***
****
*****
'''
print("Right Angle Star Pattern")
n=5
for i in range(1,n+1):
    print("*"*i)
    
'''
print:Inverted Triangle

*****
****
***
**
*
'''

print("Inverted Star Pattern")
n=5
for i in range(1,n+1):
    print("*"*((n+1)-i))
    

'''
print:Left Triangle
    *
   **
  ***
 ****
*****
'''

print("Left Angle Star Pattern")
n=5
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i)