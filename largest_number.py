#Find the largest number in the list

numbers=[6,8,9,77,4,10]

largest_number=numbers[0]

for num in numbers:
    if num>largest_number:
        largest_number=num
print("Largest number in the given list: ",largest_number)