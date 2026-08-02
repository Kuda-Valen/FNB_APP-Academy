"""
    Extend the grade classifier into a full grade report generator. 
    The program must process a list of student dictionaries (each with name marks for three subjects),
    generate a grade and status for each student, and produce a full class summary report

    REQUIREMENTS

    - Store at least 5 students as a list of dictionaries: [{}, {},{}]
    - Use a for loop to iterate over all students and calculate each student's average
    - Apply the grade/status logic from Unit 5 insde the loop
    - Build a result list of dictionaries containing: name, average, grade, status
    - After the main loop, calculate clas average, highest mark, lowest mark
    - Display a formatted class report showing individual results and class statistics
    - Use a while loop to let the user search for a student by name after the report is shown
"""
students = []

def add_student(name, subject1, subject1_name, subject2, subject2_mark, subject3, subject3_mark):
    student = {
        "name": name,
        "subject": subject1,
        ## stopped here
    }

def search_student(name):
    ...

while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Exit")

    try:
        option = int(input("Choose option: "))

        if option == 1:
            name = input("Enter Student Name: ")
            subject1 = input("Enter Subject 1: ")
            subject1_mark = input("Enter Subject 1 mark: ")
            subject2 = input("Enter Subject 2: ")
            subject2_mark = input("Enter Subject 2 mark: ")
            subject3 = input("Enter subject 3: ")
            subject3_mark = input("Enter Subject 3 mark: ")
            add_student(name, subject1, subject1_mark, subject2, subject2_mark, subject3, subject3_mark)

        elif option == 2:
            search_student(name)

        else:
            print("Invalid Option. Choose a valid option")
    except ValueError as e:
        print(f"Encountered input error: {e}")