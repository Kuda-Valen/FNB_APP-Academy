"""
    Build a command-line contact book that stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. 
    This is a foundational data structure pattern used in virtually every real app.

    REQUIREMENTS
    ============

    Store contacts as a list of dictonaries, each with keys: name, phone, email
    Implement an add_contact() function that appends a new dictionary to the list
    Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
    Implement a delete_contact(name) function that removes a contact by name
    Implement a view_all() function that displays all contacts in a formatted layout
    Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)

"""
contacts = []

def add_contact(name, phone, email):
    contact = {
    "name": name,
    "phone": phone,
    "email": email
    }
    contacts.append(contact)
    print(f"Contact '{name}' Added Successfully!")

def search(name):
    index = 0
    while True:
        if contacts[index]['name'] == name:
            return index
        else:
            print("Contact not Found!")
            index += 1

def delete(name):
    contact = search(name)
    option = input(f"Do you want to Delete {contacts[contact]['name']} | {contacts[contact]['phone']} (Y/N)")
    if option.upper() == 'Y':
        del contacts[contact]
        print(f"Contact '{name}' has been removed Successfully!")
    else:
        print("You chose Not to Delete..")

def view_all():
    if not contacts:
        print("There are no contacts!")

    i = 0
    length = len(contacts)

    while i < length:
        print(f"Name: {contacts[i]['name']} | Phone: {contacts[i]['phone']} | Email: {contacts[i]['email']}")
        i += 1

if __name__ == "__main__":

    while True:
        print("\n== Contact Book ==\n")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All contacts")
        print("5. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                name = input("Enter Contact Name: ").lower().strip()
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email: ").lower().strip()

                add_contact(name, phone, email)

            elif option == 2:
                if not contacts:
                        print("There are no Contacts!")
                else:
                    name = input("Enter Name: ").lower().strip()
                    contact = search(name)
                    print(f"Name: {contacts[contact]['name']} | Phone: {contacts[contact]['phone']} | Email: {contacts[contact]['email']}")

            elif option == 3:
                if not contacts:
                    print("There are no Contacts!")
                else:
                    name = input("Enter name: ").lower().strip()
                    delete(name)

            elif option == 4:
                view_all()
            
            elif option == 5:
                print("Exiting!!!!...")
                break
            else:
                print("Invalid Option! Choose a Valid option: ")
        except ValueError as e:
            print(f"An Input Error occured: {e}")

""" In the Search function, we have unfinished business for when a search is not found in our list of contacts """