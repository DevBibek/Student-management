#🎓 Student Management System with Authentication

This is a robust and secure Django CRUD Application designed to manage student records. It features a full User Authentication system to ensure data security and privacy.
#🚀 Key Features

🔒 Security & Access Control (Auth)
User Registration: New users can create an account to access the system.
Secure Login: Data is protected; unauthorized users cannot view, add, or modify student records without logging in.
Session Management: Dynamic Navigation Bar that shows 'Logout' when logged in and 'Login/Register' when logged out.
Protected Routes: Using Django's @login_required to prevent direct URL access to the dashboard by unauthenticated users.

#📝 Student Management (CRUD)

Create: Easily add new student records to the database.
Read: A clean, organized table view to list all registered students.
Update: Modify existing student information with a few clicks.
Delete: Remove outdated or incorrect records securely.

#🛠 Tech Stack

Backend: Python 3.12, Django 5.x
Frontend: HTML5, CSS3, Bootstrap 5 (Responsive Design)
Database: SQLite3 (Default Django DB)
Authentication: Django Built-in Auth System
