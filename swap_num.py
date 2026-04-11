# Swap Numbers using different methods

a = 5
b = 10

print("Original values:")
print("a =", a, "b =", b)

# Method 1: Using Third Variable

x, y = a, b

temp = x
x = y
y = temp

print("\nMethod 1 (Using temp):")
print("a =", x, "b =", y)

# Method 2: Without Third Variable (Python way)

x, y = a, b

x, y = y, x

print("\nMethod 2 (Python swap):")
print("a =", x, "b =", y)

# Method 3: Using Arithmetic

x, y = a, b

x = x + y
y = x - y
x = x - y

print("\nMethod 3 (Arithmetic):")
print("a =", x, "b =", y)