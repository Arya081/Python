name = input("Enter name: ")
phone_n0 = input("Enter phone number: ")
mail= input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{mail}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)
