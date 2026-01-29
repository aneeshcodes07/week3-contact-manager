# Contact Management System
# Week 3 Internship Project – Functions & Dictionaries

import json
import re
from datetime import datetime
import csv
import os

DATA_FILE = "contacts_data.json"

# ---------------- GLOBAL DICTIONARY ----------------
contacts = {}

# ---------------- VALIDATION FUNCTIONS ----------------
def validate_phone(phone):
    """Validate phone number and return cleaned digits"""
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ---------------- FILE OPERATIONS ----------------
def load_from_file():
    global contacts
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                contacts = json.load(f)
            print("✅ Contacts loaded successfully.")
        except:
            print("❌ Error loading contacts file.")
    else:
        print("ℹ️ No existing contacts file found. Starting fresh.")

def save_to_file():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(contacts, f, indent=4)
        print("✅ Contacts saved successfully.")
    except:
        print("❌ Error saving contacts.")

# ---------------- CRUD FUNCTIONS ----------------
def add_contact():
    print("\n--- ADD NEW CONTACT ---")

    while True:
        name = input("Enter contact name: ").strip().title()
        if not name:
            print("Name cannot be empty!")
        elif name in contacts:
            print("Contact already exists!")
            return
        else:
            break

    while True:
        phone = input("Enter phone number: ").strip()
        valid, cleaned_phone = validate_phone(phone)
        if valid:
            break
        print("Invalid phone number! Enter 10–15 digits.")

    while True:
        email = input("Enter email (optional): ").strip()
        if not email or validate_email(email):
            break
        print("Invalid email format!")

    group = input("Enter group (Friends/Work/Family/Other): ").strip().title()
    if not group:
        group = "Other"

    contacts[name] = {
        "phone": cleaned_phone,
        "email": email if email else None,
        "group": group,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added successfully!")
    save_to_file()

def search_contact():
    print("\n--- SEARCH CONTACT ---")
    term = input("Enter name to search: ").strip().lower()
    found = False

    for name, info in contacts.items():
        if term in name.lower():
            print("-" * 40)
            print(f"Name : {name}")
            print(f"Phone: {info['phone']}")
            if info["email"]:
                print(f"Email: {info['email']}")
            print(f"Group: {info['group']}")
            found = True

    if not found:
        print("❌ No matching contacts found.")

def update_contact():
    print("\n--- UPDATE CONTACT ---")
    name = input("Enter contact name to update: ").strip().title()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    phone = input("Enter new phone (press Enter to skip): ").strip()
    if phone:
        valid, cleaned_phone = validate_phone(phone)
        if valid:
            contacts[name]["phone"] = cleaned_phone
        else:
            print("Invalid phone number!")

    email = input("Enter new email (press Enter to skip): ").strip()
    if email:
        if validate_email(email):
            contacts[name]["email"] = email
        else:
            print("Invalid email format!")

    group = input("Enter new group (press Enter to skip): ").strip().title()
    if group:
        contacts[name]["group"] = group

    contacts[name]["updated_at"] = datetime.now().isoformat()
    print("✅ Contact updated successfully!")
    save_to_file()

def delete_contact():
    print("\n--- DELETE CONTACT ---")
    name = input("Enter contact name to delete: ").strip().title()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
    if confirm == 'y':
        del contacts[name]
        print("✅ Contact deleted successfully.")
        save_to_file()
    else:
        print("Deletion cancelled.")

def display_all_contacts():
    print("\n--- ALL CONTACTS ---")
    if not contacts:
        print("No contacts available.")
        return

    for name, info in contacts.items():
        print("=" * 40)
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        if info["email"]:
            print(f"Email: {info['email']}")
        print(f"Group: {info['group']}")

# ---------------- EXTRA FEATURES ----------------
def export_to_csv():
    if not contacts:
        print("No contacts to export.")
        return

    with open("contacts_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Group"])
        for name, info in contacts.items():
            writer.writerow([name, info["phone"], info["email"], info["group"]])

    print("✅ Contacts exported to contacts_export.csv")

def statistics():
    print("\n--- CONTACT STATISTICS ---")
    print(f"Total Contacts: {len(contacts)}")

    groups = {}
    for info in contacts.values():
        group = info["group"]
        groups[group] = groups.get(group, 0) + 1

    for g, count in groups.items():
        print(f"{g}: {count}")

# ---------------- MENU ----------------
def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("      CONTACT MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            statistics()
        elif choice == "8":
            print("👋 Thank you for using Contact Management System!")
            break
        else:
            print("❌ Invalid choice!")

# ---------------- PROGRAM START ----------------
if __name__ == "__main__":
    load_from_file()
    main_menu()
