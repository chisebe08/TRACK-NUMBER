import phonenumbers
from phonenumbers import geocoder

phone_number = input("Enter Phone number start with country code: ")
number = phonenumbers.parse(phone_number)
print("Phone_number: ", phone_number)
print("Location: ", geocoder.description_for_number(number, "en"))
