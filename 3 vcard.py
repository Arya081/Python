name = input("Enter name: ")
phone_no = input("Enter phone number: ")
mail= input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone_no}
EMAIL:{mail}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)
