#Count Total Number of Vowels in the String

str="Encyclopedia"
count=0
for ch in str:
    if ch in 'aeiouAEIOU':
        count+=1
print("Number of Vowels:",count)

