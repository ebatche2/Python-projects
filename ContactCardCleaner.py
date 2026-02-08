# Program: ContactCardCleaner.py
# Author: Elijah Batchelor
# Date: 2/6/2026
# Program description: This program receives input from user of their name email and
#                      phone number and formats their info into a contact card

# Receive user input
print("Enter full name: ", end="")
full_Name = input()

print("Enter email: ", end="")
email_Address = input()

print("Enter phone: ", end="")
phone_Num = input()

# Clean name
full_Name = " ".join(full_Name.split()) # join gets rid of extra space and split keeps everything spaced out

# Clean email
email_Address = " ".join(email_Address.split()) # join gets rid of extra space and split keeps everything spaced out

# Clean phone
phone_Num = phone_Num.replace("(", "") # used the replace method to get rid of (
phone_Num = phone_Num.replace(")", "") # used the replace method to get rid of )
phone_Num = phone_Num.replace("-", "") # used the replace method to get rid of -
phone_Num = "".join(phone_Num.split()) # join gets rid of extra space and split keeps everything spaced out

# Extract information

# Extract the initials
parts = full_Name.split() # splits full_name at the space

first_initial = parts[0][0] # gets the first initial at index 0 for the first name
last_initial = parts[-1][0] # gets second initial at index 0 for the last name

# Clean email address
domain = "@" + email_Address.split("@")[1] # receives info of email after "@"

# Clean phone number
area_code = phone_Num[0:3] # getting the first three digits
middle_three_digs = phone_Num[3:6] # getting the middle three digits
last_four_digs = phone_Num[6:] # getting the last four digits

initials = (first_initial, last_initial) # tuple created for the initials

contact_card = { # dictionary created for contact card
    "name": full_Name,
    "email": email_Address,
    "phone": phone_Num,
    "domain": domain,
    "area_code": area_code,
    "initials": initials
}

# Print output
print("---Clean Contact Card---")
print("Name: " + full_Name.title())
print("Initials: " + first_initial.upper() + "." + last_initial.upper())
print("Email: " + email_Address.lower())
print("Email domain: " + domain)
print("Phone: (" + area_code + ") " + middle_three_digs + "-" + last_four_digs)
print("Area code: " + area_code)
print()
print("Contact saved. Thanks!")