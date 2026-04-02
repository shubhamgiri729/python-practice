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
print:Inverted Right Angle Triangle

*****
****
***
**
*
'''

print("Inverted Right Angle Star Pattern")
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
    
'''
print:Inverted Left Angle Pattern

*****
 ****
  ***
   **
    *
'''
print("Inverted Left Angle star Pattern")
n=5
for i in range(n):
    print(" "*i+"*"*(n-i))
    
'''
print:Pyramid (Centered)
    *
   ***
  *****
 *******
*********
'''
print("Pyramid Pattern")
n=5
for i in  range(1,n+1):
    print(" "*(n-i)+"*"*((2*i)-1))
    
    
'''
print:Inverted Pyramid
*********
 *******
  *****
   ***
    *
'''
print("Inverted Pyramid Pattern")
n=5
for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))
