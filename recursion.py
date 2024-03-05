def factorial(num):
    while (num>0):
        return num*factorial(num-1)
    else:
        return 1
number = int(input("Enter a number to find its factorial: "))
print(factorial(number))

def fibonacci(term):

    if(term<=1):
        return term
    else:
        return (fibonacci(term-1)+fibonacci(term-2))

nterms = int(input("Enter the number of terms you want:  "))

for i in range(nterms):
    print(fibonacci(i))