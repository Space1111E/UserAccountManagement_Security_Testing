# User Account Management – Security Risk Assessment & Test Plan

Welcome to this project focused on identifying security risks and validating the core functionality of a **user account management system**. This includes:

- Registration
- Login
- Password management
- Security risk documentation
- Manual test planning
- Python test script

The project is structured for educational and professional purposes in **IT security**, **software testing**, and **solution design**.

---

## 📁 Project Structure

```
UserAccountManagement_Security_Testing/
├── Documentation/
│ ├── README.md # (Optional secondary README)
│ ├── Risk_Assessment.md # List of key threats and mitigations
│ ├── Test_Plan.md # Manual test cases
│ 
├── Code/
│ └── simple_auth_test.py # Python script to simulate login tests
└── README.md # ✅ You’re reading it!
```

---

##  Objectives

- Identify and document common security threats
- Define clear manual test cases for key scenarios
- Create a simple, testable login function in Python
- Demonstrate understanding of QA & InfoSec principles

---

## 📌 What's Inside

###  1. Risk Assessment (`Risk_Assessment.md`)
Covers potential vulnerabilities like:
- Weak passwords
- SQL injection
- Lack of HTTPS
- Unauthorized access
- Data loss due to missing backups

Each risk includes:
- Likelihood
- Impact
- Mitigation strategy

> 📄 [View full risk assessment](./Documentation/Risk_Assessment.md)

---

###  2. Manual Test Plan (`Test_Plan.md`)
Detailed test cases for validating:

- User registration
- Login success/failure
- Password changes
- Error handling
- SQL injection protection

> 📄 [View test plan](./Documentation/Test_Plan.md)

---

###  3. Python Login Test Script (`simple_auth_test.py`)
This Python script performs automated login tests.

####  Features:
- Asserts successful login
- Detects invalid credentials
- Blocks unknown users

#### ▶ How to run:
```bash
python Code/simple_auth_test.py
```
If working correctly, it will print:
All tests passed!

---


