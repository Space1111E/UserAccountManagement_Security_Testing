# Test Plan for User Account Management App

## Test Objectives
- Validate user registration and login
- Ensure password change works securely
- Prevent SQL injection
- Verify access control and error handling

## Test Cases

| ID   | Description                  | Steps                                             | Expected Result                     |
|------|------------------------------|---------------------------------------------------|-------------------------------------|
| TC01 | Register new user            | Fill form and click register                      | Success message shown               |
| TC02 | Login with correct password  | Enter valid email and password                    | Redirect to user dashboard          |
| TC03 | Login with wrong password    | Enter wrong password                              | Error message shown                 |
| TC04 | Change password              | Log in → Go to settings → Change password         | Password updated confirmation       |
| TC05 | Attempt SQL Injection        | Input `' OR 1=1 --` in login field                | Login fails; input is rejected      |
