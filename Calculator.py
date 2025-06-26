# Goal: Prompt the user for two numbers. Print the sum, difference, product, and quotient 

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Perform the operations 
# Addition
sum_result = number1 + number2

# Multiplication
product_result = number1 * number2

# Subtraction 
difference_result = number1 - number2

# Divison
quotient_result = number1/number2

# Remainder aka Modulus 
remainder_result =  number1 % number2

# Exponentiation
power_result = number1 ** number2

print("Sum:", sum_result) #Print the  sum
print("Difference:", difference_result) #Print the difference 
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)
print("Power:", power_result)
print("Product:", product_result)
