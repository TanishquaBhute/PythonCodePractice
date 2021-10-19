import contact_details
print("1. Add contact")
print("2. Get Info of Existing Contact")
choice = int(input("Enter your choice: "))
if choice == 1:
    contact_details.write_details()
else:
    contact_name = input("Enter contact name : ")
    details = contact_details.read_details(contact_name)
    print(f"Contact Details of {contact_name} :")
    print(f"First Name : {details[0]} \n Last Name : {details[1]} \n Email : {details[2]} \n contact No. : {details[3]}")