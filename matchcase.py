# DAY OF THE WEEK WITH MATCH CASE

day = int(input("Enter the day number (1-7) to get the day: "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Day Number!")

num = int(input("Enter a number to find its table: "))

# Table of a number with match case
# match num:
#     case num:
#         print(num, " x", 1, " =", num*1)
#         print(num, " x", 2, " =", num*2)
#         print(num, " x", 3, " =", num*3)
#         print(num, " x", 4, " =", num*4)
#         print(num, " x", 5, " =", num*5)
#         print(num, " x", 6, " =", num*6)
#         print(num, " x", 7, " =", num*7)
#         print(num, " x", 8, " =", num*8)
#         print(num, " x", 9, " =", num*9)
#         print(num, " x", 10, " =", num*10)

match num:
    case num:
        for i in range(10):
            print(num, "x", i+1, "=", num*(i+1))
        # print(num, " x", 1, " =", num*1)
        # print(num, " x", 2, " =", num*2)
        # print(num, " x", 3, " =", num*3)
        # print(num, " x", 4, " =", num*4)
        # print(num, " x", 5, " =", num*5)
        # print(num, " x", 6, " =", num*6)
        # print(num, " x", 7, " =", num*7)
        # print(num, " x", 8, " =", num*8)
        # print(num, " x", 9, " =", num*9)
        # print(num, " x", 10, " =", num*10)


