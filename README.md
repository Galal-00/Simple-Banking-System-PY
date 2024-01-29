# Simple Banking System 🏦

This Python program is a simple banking system that uses MySQL for user data storage. Users can sign up, sign in, view account details, check account balance, deposit money, and withdraw money. The program utilizes object-oriented programming concepts and MySQL Connector for Python to interact with the database.

## Features 🚀

- **User Registration:** Users can sign up by providing their name, age, gender, ID, password, and security questions.

- **Secure Password Handling:** The program incorporates secure password input using the `pwinput` library to enhance overall security.

- **Password Recovery:** Users can recover their password by answering security questions.

- **Banking Operations:** Signed-in users can perform various banking operations such as viewing account details, checking balance, depositing money, and withdrawing money.

- **Custom Exceptions:** The program defines custom exceptions (`ChoiceNotExist`, `PassWrong`, `WrongId`) to handle specific error scenarios and guide users appropriately.

## Getting Started 🛠️

1. **Database Setup:**
   - Create a MySQL database named `bank_users_credentials`.
   - Update the connection details in the program (`host`, `user`, `password`, `database`) to match your MySQL server configuration.

2. **Library Installation:**
   - Install the required libraries using the following command:
     ```bash
     pip install mysql-connector-python pwinput
     ```

3. **Run the Program:**
   - Execute the program using a Python interpreter:
     ```bash
     python banking_system.py
     ```

## Dependencies 📚

- [MySQL Connector for Python](https://pypi.org/project/mysql-connector-python/)
- [pwinput](https://pypi.org/project/pwinput/)
