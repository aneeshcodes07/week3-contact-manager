# week3-contact-manager
# 📇 Contact Management System
## Week 3 Internship Project – Functions & Dictionaries

---

## 📌 Project Description
The Contact Management System is a Python-based application designed to manage personal and professional contacts efficiently.  
It uses **functions and dictionaries** to perform CRUD operations such as adding, searching, updating, and deleting contacts.  
The project also supports **data persistence using JSON files** and provides a **menu-driven interface** for ease of use.

---

## 🎯 Objectives
- Understand and implement Python functions
- Use dictionaries for structured data storage
- Apply string methods for data cleaning
- Perform input validation
- Implement file operations using JSON
- Build a real-world menu-driven application

---

## ✨ Features
- Add new contacts with validation
- Search contacts using partial name matching
- Update existing contact details
- Delete contacts with confirmation
- View all contacts in formatted output
- Save and load contacts automatically (JSON)
- Export contacts to CSV format
- View contact statistics by group
- User-friendly menu system
- Error handling for invalid inputs

---

## 🛠 Technologies Used
- Python 3
- Dictionaries & Functions
- JSON module
- Regular Expressions (re)
- CSV module
- DateTime module

---

## 📂 Project Structure
week3-contact-manager/
│── contacts_manager.py
│── contacts_data.json
│── contacts_export.csv
│── README.md
│── test_contacts.py
│── requirements.txt


---

## ▶️ How to Run the Project

```bash
# Navigate to project folder
cd week3-contact-manager

# Run the application
python contacts_manager.py

```
Data Structures Used

contacts = {
    "John Doe": {
        "phone": "9876543210",
        "email": "john@gmail.com",
        "group": "Friends",
        "created_at": "2026-01-20",
        "updated_at": "2026-01-20"
    }
}

Sample Menu

1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit


Sample Output

--- ADD NEW CONTACT ---
Enter contact name: John Doe
Enter phone number: +91 98765 43210
Enter email: john@gmail.com
Enter group: Friends
✅ Contact 'John Doe' added successfully!

--- ADD NEW CONTACT ---
Enter contact name: John Doe

Enter phone number: +91 98765 43210

Enter email: john@gmail.com

Enter group: Friends

✅ Contact 'John Doe' added successfully!
