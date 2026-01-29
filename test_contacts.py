# test_contacts.py
# Simple test cases for Contact Management System

from contacts_manager import validate_phone, validate_email

print("Testing phone validation:")
print(validate_phone("9876543210"))       # Valid
print(validate_phone("+91 98765 43210"))  # Valid
print(validate_phone("123"))              # Invalid

print("\nTesting email validation:")
print(validate_email("test@example.com"))   # Valid
print(validate_email("wrong-email"))        # Invalid
