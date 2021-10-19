def write_details():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    email = input("Enter your email id : ")
    contact = input("Enter your contact : ")
    with open("contact_details.txt", 'a') as file:
        file.write(f"{first_name},{last_name},{email},{contact}\n")


def read_details(contact_name):
    contact_details = {}
    with open("contact_details.txt", 'r') as file:
        data = file.readlines()
    for contact in data:  # ['abc,xyz,email,123\n','abc,xyz,email,123\n']
        temp = contact.split(',')
        contact_details[temp[0]] = contact
    details = contact_details[contact_name].split(',')
   # print(f"Contact Details of {contact_name} :")
    #print(f"First Name : {details[0]} \n Last Name : {details[1]} \n Email : {details[2]} \n contact No. : {details[3]}")
# print(contact_details)
    return details



