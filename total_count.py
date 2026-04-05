#Count Total Number of Vowels in the String

str="Encyclopedia"
vowel_count=0
for ch in str:
    if ch in 'aeiouAEIOU':
        vowel_count+=1
print("Number of Vowels:",vowel_count)

#Count Total Number of Consonants in the String

text="Encyclopedia"
consonant_count=0
for ch in text:
    if ch not in 'aeiouAEIOU':
        consonant_count+=1
print("Number of Consonants:",consonant_count)