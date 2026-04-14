# Remove spaces from string Using replace()

text1 = "he llo"
result = text1.replace(" ", "")
print("Result:", result)

# Remove spaces from string Using Loop

text2 = "he llo"
result = ""
for char in text2:
    if char != " ":
        result += char
print("Result:", result)

## Remove spaces from string Using join()

text3 = "he llo"
result = "".join(text3.split())
print("Result:", result)