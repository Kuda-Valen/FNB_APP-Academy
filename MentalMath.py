"""
    So we need to create a mental math program, that generates numbers and lets user enter answers, wont continue if its not correct
"""
import random
import time

class Addition():
    def __init__(self, x: int, y: int, z: int, a: int, b: int):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.ans = x + y + z + a + b

    def check_ans(self, answer):
        if answer == self.ans:
            return True
        else:
            return False

class Subtraction():
    def __init__(self, x: int, y: int, z: int, a: int, b: int):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b        
        self.ans = x - y - z - a - b

    def check_ans(self, answer):
        if answer == self.ans:
            return True
        else:
            return False

class Multiplication():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ans = x * y

    def check_ans(self, answer):
        if answer == self.ans:
            return True
        else:
            return False

class Division():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_divident(self):    
        product = self.x * self.y
        return product

    def check_ans(self, answer):
        if answer == self.x:
            return True
        else:
            return False

# random_x = random.randint(1, 10)
def random_number(user_input):
    if user_input == 1:
        random_x = random.randint(1, 10)
        random_y = random.randint(1, 10)
        random_z = 0
        random_a = 0
        random_b = 0

    elif user_input == 2:
        random_x = random.randint(10, 99)
        random_y = random.randint(10, 99)
        random_z = random.randint(10, 99)
        random_a = 0
        random_b = 0

    elif user_input == 3:
        random_x = random.randint(100, 250)
        random_y = random.randint(100, 250)
        random_z = random.randint(100, 250)
        random_a = random.randint(100, 250)
        random_b = 0

    elif user_input == 4:
        random_x = random.randint(251, 1000)
        random_y = random.randint(251, 1000)
        random_z = random.randint(251, 1000)
        random_a = random.randint(251, 1000)
        random_b = random.randint(251, 1000)

    return random_x, random_y, random_z, random_a, random_b

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
                corrects = 0
                i = 0
                user_input = difficulty()
                while i < 10:
                    random_x = random_number(user_input)[0]
                    random_y = random_number(user_input)[1]
                    random_z = random_number(user_input)[2]
                    random_a = random_number(user_input)[3]
                    random_b = random_number(user_input)[4]

                    if user_input == 1:
                        print(f"\n{random_x} + {random_y}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 2:
                        print(f"\n{random_x} + {random_y} + {random_z}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 3:
                        print(f"\n{random_x} + {random_y} + {random_z} + {random_a}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 4:
                        print(f"\n{random_x} + {random_y} + {random_z} + {random_a} + {random_b}")
                        answer_input = int(input("Answer: "))

                    addition = Addition(random_x, random_y, random_z, random_a, random_b)
                    check = addition.check_ans(answer_input)
                    if check == True:
                        corrects += 1
                        print("Correct!!")
                    else:
                        print("Incorrect!!")
                    i += 1

                print(f"\nYou Got {corrects} out of 10")

            elif option == 2:
                print("\n--- Subtraction ---")
                corrects = 0
                i = 0
                user_input = difficulty()
                while i < 10:
                    random_x = random_number(user_input)[0]
                    random_y = random_number(user_input)[1]
                    random_z = random_number(user_input)[2]
                    random_a = random_number(user_input)[3]
                    random_b = random_number(user_input)[4]

                    if user_input == 1:
                        print(f"\n{random_x} - {random_y}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 2:
                        print(f"\n{random_x} - {random_y} - {random_z}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 3:
                        print(f"\n{random_x} - {random_y} - {random_z} - {random_a}")
                        answer_input = int(input("Answer: "))

                    elif user_input == 4:
                        print(f"\n{random_x} - {random_y} - {random_z} - {random_a} - {random_b}")
                        answer_input = int(input("Answer: "))

                    subtraction = Subtraction(random_x, random_y, random_z, random_a, random_b)
                    check = subtraction.check_ans(answer_input)
                    if check == True:
                        corrects += 1
                        print("Correct!!")
                    else:
                        print("Incorrect!!")
                    i += 1
                print(f"\nYou Got {corrects} out of 10.")

            elif option == 3:
                print("\n --- Multiplication ---")
                corrects = 0
                i = 0
                user_input = difficulty()
                while i < 10:
                    random_x = random_number(user_input)[0]
                    random_y = random_number(user_input)[1]

                    print(f"\n{random_x} x {random_y}")
                    answer_input = int(input("Answer: "))

                    multiplication = Multiplication(random_x, random_y)
                    check = multiplication.check_ans(answer_input)
                    if check == True:
                        corrects += 1
                        print("Correct!!")
                    else:
                        print("Incorrect!!")
                    i += 1

                print(f"\nYou Got {corrects} out of 10")

            elif option == 4:
                print("\n --- Division ---")
                user_input = difficulty()

                random_x = random_number(user_input)[0]
                random_y = random_number(user_input)[1]

                division = Division(random_x, random_y)
                divident = division.get_divident()

                print(f"{divident} / {random_y}")
                answer_input = int(input("Answer: "))

                check = division.check_ans(answer_input)
                if check == True:
                    print("Correct!!")
                else:
                    print("Incorrect!!")

            elif option == 5:
                print("\n --- Challenge ---")
                print("Quite Difficult to program for now!!")
                print("Still figuring out the Algorithm")
                user_input = difficulty()
                pass

            elif option == 6:
                print("\nExiting...")
                break

            else:
                print("[INVALID OPTION] Choose a Valid Option...")

        except ValueError as e: 
            print(f"Encountered Input Error: {e}")