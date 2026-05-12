# User Management API Testing Framework

## Project Overview
This project demonstrates API development and API testing for a User Management System built using Flask, MongoDB, and REST APIs. The project includes CRUD operations along with functional testing, validation testing, negative testing, and bug reporting using Postman.

---

# Technologies Used

- Python
- Flask
- MongoDB
- REST APIs
- Postman
- JSON
- Git & GitHub

---

# Features Implemented

## Backend Features
- Add User
- Get Users
- Update User
- Delete User

## Testing Features
- Functional API Testing
- CRUD API Validation
- Response Validation
- Negative Testing
- Validation Testing
- Bug Identification
- Response Time Validation

---

# API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /users | Retrieve all users |
| POST | /users | Add new user |
| PUT | /users/<id> | Update existing user |
| DELETE | /users/<id> | Delete user |

---

# Testing Performed

## Functional Testing
- Add valid user
- Retrieve users
- Update user
- Delete user

## Negative Testing
- Add user without name
- Add user without email
- Invalid email testing
- Invalid ObjectId testing
- Update user with missing fields

## Validation Testing
- Response status validation
- Response message validation
- Response time validation

---

# Postman Collection

The Postman testing collection is available in:

```text
postman_collection/User Mgmt API Testing.postman_collection.json
```

---

# Test Cases

API test cases are available in:

```text
test_cases/API_TestCases.xlsx
```

---

# Bug Reports

Bug reports are available in:

```text
bug_reports/Bug_Report.xlsx
```

---

# Screenshots

## Add User Success
![Add User](screenshots/add_user_success.png)

---

## Update User Success
![Update User](screenshots/update_user_success.png)

---

## Delete User Success
![Delete User](screenshots/delete_user_success.png)

---

## Delete User Bug
![Delete User Bug](screenshots/delete_user_bug.png)

---

## Add User Bug
![Add User Bug](screenshots/add_user_bug.png)

---

# Skills Demonstrated

- REST API Development
- API Testing
- Functional Testing
- Validation Testing
- Negative Testing
- CRUD Operations
- Postman Automation
- Bug Reporting
- Backend Validation
- Flask Development
- MongoDB Integration

---

# Project Structure

```text
user-management-api-testing/
│
├── backend/
├── postman_collection/
├── test_cases/
├── bug_reports/
├── screenshots/
└── README.md
```

---

# Future Improvements

- Add email format validation
- Add duplicate email validation
- Add exception handling
- Add JWT authentication
- Add automated testing pipeline
- Add frontend validation

---

# Author

Adithya S
