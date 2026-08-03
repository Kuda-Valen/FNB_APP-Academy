"""
Create a mini data directory using a List and a Dictionary combined.

1. Create a dictionary called contacts where the Keys are friend names and the Values are 
   their phone numbers (keep phone numbers as strings so the leading 0 doesn’t drop off, 
   e.g., “0821112222”). Fill it with 3 people.

2. Ask the user to input the name of the friend they want to look up.

3. Use a conditional check to see if the name matches a key. If it exists, pull out and print their number: “Found! [Name]’s number is [Number]”.

4. Otherwise, print “Contact not found.”
"""
contacts = []

class Contact:
   def __init__(self, name: str, phone: str):
      self.name = name
      self.phone = phone

      contact = {
         "name": name,
         "phone": phone
      }

def add_contact(new_contact):
   contacts.append(new_contact)
   print(f"{new_contact.name} has been added successfully!!")

"""new_contact = Contact("Kuda", "0616168539")
add_contact(new_contact)"""

def search_contact(name):
   i = 0
   n = len(contacts)

   while i < n:
      contact = contacts[i]
      if name == contact.name:
         return i
      i += 1

def view_all():
   i = 0
   n = len(contacts)

   while i < n:
      contact = contacts[i]
      print(f"{contact.name} -> {contact.phone}")
      i += 1

def delete_contact(name):
   contact_indx = search_contact(name)
   del contacts[contact_indx]
   print(f"{name} has been deleted successfully!!")

if __name__ == "__main__":

   while True:
      print("\n== Contacts Phone Book ==\n")
      print("1. Add Contact")
      print("2. Search Contact")
      print("3. Delete Contact")
      print("4. View all Contacts")
      print("5. Exit!!")

      try:
         option = int(input("\nChoose an Option: "))

         if option == 1:
            name = input("\nEnter Name: ").strip().lower()
            phone = input("Enter Phone: ").strip()

            new_contact = Contact(name, phone)
            add_contact(new_contact)

         elif option == 2:
            if not contacts:
               print("There are no Contacts Available..")
            else:
               name = input("Enter Name: ").lower().strip()
               contact_index = search_contact(name)
               if contact_index:
                  contact = contacts[contact_index]
                  print(f"{contact.name} -> {contact.phone}")

               else:
                  print("Contact Not found!!")

         elif option == 3:
            if not contacts:
               print("There are no contacts to delete!!")
               
            else:
               name = input("Enter Name: ")
               delete_contact(name)

         elif option == 4:
            if not contacts:
               print("No Contacts. Add new Contacts First..")

            else:
               view_all()

         elif option == 5:
            print("\nExiting...")
            break

         else:
            print("Invalid Option!!..Choose a Valid option!!")

      except ValueError as e:
         print(f"Encountered Input Error: {e}")
   
   
