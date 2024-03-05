# def greetHello(arg1, arg2):
#     print("Hello there, " + arg1)
#     print(arg2)

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter first number: "))
    opr = input("Enter which operation to perfom (add, sub, mul, div, avg): ")
    if opr == "add":
        return a+b
    elif opr == "sub":
        return a-b
    elif opr == "mul":
        return a*b
    elif opr == "div":
        return a/b
    elif opr == "avg":
        return (a+b)/2
    else:
        return "error"
print(calculator())

#
#
# greetHello("Prashant", "Thanks!")
#
# def anotherFunction(name, date):
#     st = f"Hi sir, This is {name} and I won't be able to attend the meeting on {date}"
#     print(st)
#
# anotherFunction("Prashant", "30th December")
#
