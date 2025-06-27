# 🔹 Step 1: Take full name input from user
full_name = input("Enter your full name (first and last): ")

# 🔹 Step 2: Find the space between first and last name
space_index = full_name.find(" ")

# 🔹 Step 3: Slice first name and last name
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

# 🔹 Step 4: Print sliced names
print("First Name:", first_name)
print("Last Name:", last_name)

# 🔹 Step 5: Take two numeric inputs from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 🔹 Step 6: Perform arithmetic operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# 🔹 Step 7: Display results using formatted print
print(f"\nResults for numbers {num1} and {num2}:")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

