#Develop a python program that could search the text in a file for
#phone numbers (+919900889977) and email addresses
with open('filename.txt', 'r') as file:
      text = file.read() 
import re
phone_numbers = re.findall(r'\+91\d{10}', text)
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Phone numbers found:", phone_numbers) 
print("Email addresses found:", email_addresses)
