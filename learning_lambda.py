def add(x, y):
    sum = x + y
    return sum

add_lambda = lambda x, y: x + y

while True:
    print("\n1. Normal")
    print("2. Lambda")
    print("3. exit")

    user_input = int(input("\nChoose option: "))

    if user_input == 1:
        x = int(input("\nEnter x: "))
        y = int(input("Enter y: "))

        sum = add(x, y)
        print(f"Sum = {sum}")

    elif user_input == 2:
        x = int(input("\nEnter x: "))
        y = int(input("Enter y: "))

        sum = add_lambda(x, y)
        print(f"Sum = {sum}")

    elif user_input == 3:
        print("Exiting")
        break

    else:
        print("\nInvalid input")