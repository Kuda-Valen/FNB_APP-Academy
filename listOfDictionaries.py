""" Learning List of Dictoinaries """

# List of Dictionaries is a data structure used to manage
# tabular data, such as database rows or API responses. It consist of
# a standard python list [] where every individual element inside it is a dictionary {}


# A list storing database-like records of employees
employees = [
    {"id": 101, "name": "Alice", "role": "Engineer"},
    {"id": 102, "name": "Bob", "role": "Designer"},
    {"id": 103, "name": "Charlie", "role": "Manager"}
]

print("What happens if we print employees as a variable:")
print(employees)

print("\nWhat happens if we print employees including indexing: ")
print(employees[0])

print("\nWhat happens if we print employees including indexing as well as dictionary key:")
print(f"ID: {employees[0]['id']}, Name: {employees[0]['name']}")