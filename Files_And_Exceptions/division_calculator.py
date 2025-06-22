print("Enter two numbers. Enter 'q' to quite.")

while True:
    first_number = input("First Number: ")
    if first_number == "q":
        break
    second_number = input("Second Number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide a number with zero.")
    else:
        print(answer)
