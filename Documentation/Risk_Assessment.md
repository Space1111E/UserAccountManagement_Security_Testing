# Risk Assessment for User Account Management

| Risk                    | Description                                      | Likelihood | Impact   | Mitigation                                  |
|-------------------------|--------------------------------------------------|------------|----------|----------------------------------------------|
| Weak Passwords          | Users may choose simple, easy-to-guess passwords| Medium     | High     | Enforce strong password rules               |
| SQL Injection           | User inputs may be exploited to run SQL commands| Low        | Critical | Input validation & parameterized queries    |
| No HTTPS                | Data can be intercepted in transit              | Medium     | Medium   | Use SSL/TLS for all connections             |
| Unauthorized Access     | Users may access data they shouldn't            | Medium     | High     | Role-based access control & authentication  |
| Missing Backups         | Data may be lost without recovery options       | Low        | Critical | Regular automated backups + restore testing |
