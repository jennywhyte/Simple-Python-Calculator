print('')
print("A SIMPLE PYTHON CALCULATOR")
print('')

# Pick the numeric represention of the operation you would like to perform

print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaion")
print("4. Division")
print("5. Modulus")
print("6. Square Value")
print("7. Square Root")
print("8. Cubic Value")
print("9. Cubic Root")
print('')

operation = int(input("PICK THE OPERATION: "))

print('')
first_num = float(input("Enter First Number: "))
second_num = float(input("Enter Second Number: "))

print('')
if operation == 1:
    print("The sum of the operation is " + str(float(first_num) + float(second_num)))

elif operation == 2:
    print("The difference of the operation is " + str(float(first_num) - float(second_num)))

elif operation == 3:
    print("The product of the operation is " + str(float(first_num) * float(second_num)))

elif operation == 4:
    print("The result of the operation is " + str(float(first_num) / float(second_num)))

elif operation == 5:
    print("The remainder of the operation is " + str(float(first_num) % float(second_num)))

elif operation == 6:
    print("The square value of the first number is " + str(float(first_num)**2))
    print("The square value of the second number is " + str(float(second_num)**2))

elif operation == 7:
    print("The square root of the first operation is " + str(float(first_num)**0.5))
    print("The square root of the second operation is " + str(float(second_num)**0.5))

elif operation == 8:
    print("The cubic value of the first number is " + str(float(first_num)**3))
    print("The cubic value of the second number is " + str(float(second_num)**3))

elif operation == 9:
    print("The cubic root of the first operation is " + str(float(first_num)**0.3333333333))
    print("The cubic root of the second operation is " + str(float(second_num)**0.3333333333))

else:
    print("Invalid Entry")