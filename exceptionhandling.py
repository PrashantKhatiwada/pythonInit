try:
    num1 = int(input("Enter your number: "))
    print(num1+3)
except Exception as e:
    print("An error occurred: ", e)

# example

try:
    number = int(input("Enter a number: "))
    result = 10/number
    print("The result is:", result)
# except ZeroDivisionError:
except Exception as e:
    print("error: ", e)

# except ValueError:
#     print("Invalid input. Please enter a valid number.")