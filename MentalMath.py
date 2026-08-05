"""
    So we need to create a mental math program, that generates numbers and lets user enter answers, wont continue if its not correct
"""
import random
import time

class Addition():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ans = x + y

    def check_ans(self, z):
        if z == self.ans:
            return True
        else:
            return False

# random_x = random.randint(1, 10)
def random_number(user_input):
    if user_input == 1:
        random_x = random.randint(1, 10)
        random_y = random.randint(1, 10)

    elif user_input == 2:
        random_x = random.randint(10, 50)
        random_y = random.randint(10, 50)

    elif user_input == 3:
        random_x = random.randint(50, 100)
        random_y = random.randint(50, 100)

    elif user_input == 4:
        random_x = random.randint(100, 1000)
        random_y = random.randint(100, 1000)

    return random_x, random_y

def difficulty():
    print("1. Begginer")
    print("2. Intermediate")
    print("3. Advanced")
    print("4. Genius")

    try:
        user_input = int(input("\nChoose your Challenge: "))

    except ValueError as e:
        print(f"Encountered Input Error: {e}")

    return user_input

if __name__ == "__main__":

    while True:
        print("\n== Mental Maths Program ==\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Challenge")
        print("6. Exit")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1: 
                print("\n --- Addition ---")
                user_input = difficulty()

                random_x = random_number(user_input)[0]
                random_y = random_number(user_input)[1]

                print(f"{random_x} + {random_y}")
                answer_input = int(input("Answer: "))

                addition = Addition(random_x, random_y)
                check = addition.check_ans(answer_input)
                if check == True:
                    print("Correct!!")
                else:
                    print("Incorrect!!")



            elif option == 2:
                print("\n--- Subtraction ---")
                user_input = difficulty()

                if user_input == 1:
                    ...

                elif user_input == 2:
                    ...

                elif user_input == 3:
                    ...

                elif user_input == 4:
                    ...

                else:
                    print("[INVALID OPTION] Choose a valid option")

            elif option == 3:
                print("\n --- Multiplication ---")
                user_input = difficulty()

                if user_input == 1:
                    ...

                elif user_input == 2:
                    ...

                elif user_input == 3:
                    ...

                elif user_input == 4:
                    ...

                else:
                    print("[INVALID OPTION] Choose a Valid option: ")

            elif option == 4:
                print("\n --- Division ---")
                user_input = difficulty()

                if user_input == 1:
                    ...

                elif user_input == 2:
                    ...

                elif user_input == 3:
                    ...

                elif user_input == 4:
                    ...

                else:
                    print("[INVALID OPTION] Choose a Valid Option: ")

            elif option == 5:
                print("\n --- Challenge ---")
                user_input = difficulty()

                if user_input == 1:
                    ...

                elif user_input == 2:
                    ...

                elif user_input == 3:
                    ...

                elif user_input == 4:
                    ...

                else:
                    print("[INVALID OPTION] Choose a Valid Option: ")

            elif option == 6:
                print("\nExiting...")
                break

            else:
                print("[INVALID OPTION] Choose a Valid Option...")

        except ValueError as e: 
            print(f"Encountered Input Error: {e}")