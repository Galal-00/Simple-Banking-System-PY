import pwinput
import mysql.connector

#Create MySQL users_db object
users_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "bank_users_credentials"
)
cursor = users_db.cursor(buffered=True)

# Create users_credentials table if it doesn't exist
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS users_credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    users_name VARCHAR(255),
    users_age INT,
    users_gender VARCHAR(255),
    users_id INT,
    users_pass VARCHAR(255),
    users_security_question VARCHAR(255),
    users_security_question_ans VARCHAR(255),
    users_account_balance DECIMAL(10, 2)
);
"""

cursor.execute(CREATE_TABLE_QUERY)
users_db.commit()

#Getting db data
def get_db_data():
    users_db_select_query = "SELECT * FROM users_credentials"
    cursor.execute(users_db_select_query)
    user_names = []
    user_ages = []
    user_genders = []
    user_ids = []
    user_passwords = []
    user_security_qs = []
    user_security_q_anses = []
    user_account_balances = []
    credentials = {
        "name": user_names,
        "age": user_ages,
        "gender": user_genders,
        "id": user_ids,
        "pass": user_passwords,
        "securityQ": user_security_qs,
        "securityQAns": user_security_q_anses,
        "accountBalance": user_account_balances
    }
    # Get all records
    records = cursor.fetchall()
    for row in records:
        user_names.append(row[1])
        user_ages.append(row[2])
        user_genders.append(row[3])
        user_ids.append(row[4])
        user_passwords.append(row[5])
        user_security_qs.append(row[6])
        user_security_q_anses.append(row[7])
        user_account_balances.append(row[8])
    return credentials

#Password forget check method
def pass_forget_check(user, check):
    db_select_row_query = """SELECT * FROM users_credentials WHERE users_id = %s"""
    #order: unique id 0, name 1, age 2, gender 3, id 4, password 5, secQ 6, secQAns 7, balance 8
    cursor.execute(db_select_row_query, (int(user),))
    users_db.commit()
    records = cursor.fetchall()
    records = list(records[0])
    try:
        choice1 = input("Forgot password? [y/n] or sign up [0]: ")
        if choice1 in ['y', 'Y']:
            try:
                choice2 = input("""Choose your security question:
                1: father name
                2: mother name
                3: pet name
                Choice: """)
                if choice2 == records[6]: #choice2 == secQ
                    if choice2 == "1":
                        ans = input("What is your father's name? ")
                        if ans == records[7]: #ans == secQAns
                            #change pass
                            records[5] = pwinput.pwinput(prompt="Correct! Enter a new password: ")
                            index = records[0]
                            db_pass_update_query ="""UPDATE users_credentials
                                                    SET users_pass = %s
                                                    WHERE id = %s"""
                            form2 = (records[5], index) #pass, unique id
                            cursor.execute(db_pass_update_query, form2)
                            users_db.commit()
                            user = Bank(records[1], records[2], records[3], records[4], 
                            records[5], records[6], records[7], records[8])
                            main_menu(user)
                        else:
                            print("Wrong answer")
                            pass_forget_check(user, check)
                    elif choice2 == "2":
                        ans = input("What is your mother's name? ")
                        if ans == records[7]: #ans == secQAns
                            #change pass
                            records[5] = pwinput.pwinput(prompt="Correct! Enter a new password: ")
                            index = records[0]
                            db_pass_update_query ="""UPDATE users_credentials
                                                    SET users_pass = %s
                                                    WHERE id = %s"""
                            form2 = (records[5], index) #pass, unique id
                            cursor.execute(db_pass_update_query, form2)
                            users_db.commit()
                            user = Bank(records[1], records[2], records[3], 
                            records[4], records[5], records[6], records[7], records[8])
                            main_menu(user)
                        else:
                            print("Wrong answer")
                            pass_forget_check(user, check)
                    elif choice2 == "3": #ans == secQAns
                        ans = input("What is your pet's name? ")
                        if ans == records[7]: #ans == secQAns
                            #change pass
                            records[5] = pwinput.pwinput(prompt="Correct! Enter a new password: ")
                            index = records[0]
                            db_pass_update_query ="""UPDATE users_credentials
                                                    SET users_pass = %s
                                                    WHERE id = %s"""
                            form2 = (records[5], index) #pass, unique id
                            cursor.execute(db_pass_update_query, form2)
                            users_db.commit()
                            user = Bank(records[1], records[2], records[3],
                            records[4], records[5], records[6], records[7], records[8])
                            main_menu(user)
                        else:
                            print("Wrong answer")
                            pass_forget_check(user, check)
                    else:
                        raise ChoiceNotExist
                elif choice2 != records[6]: #choice2 == secQ
                    print("Wrong secuity qusetion")
                    pass_forget_check(user, check)
                else:
                    raise ChoiceNotExist
            except ChoiceNotExist:
                print("Please choose only from the given choices")
                pass_forget_check(user, check)
        elif choice1 in ['n', 'N'] and check == 1:
            user = Bank(records[1], records[2], records[3],
            records[4], records[5], records[6], records[7], records[8])
            main_menu(user)
        elif choice1 in ['n', 'N'] and check == 0:
            sign_in()
        elif choice1 == "0":
            sign_up()
        else:
            raise ChoiceNotExist
    except ChoiceNotExist:
        print("Please choose only from the given choices")
        pass_forget_check(user, check)

#Define user class and methods
class User:
    def __init__(self, name, age, gender, id, password, security_q, security_q_ans):
        self._name = name
        self._age = age
        self._gender = gender
        self._id = id
        self._password = password
        self._security_q = security_q
        self._security_q_ans = security_q_ans

    #Setter and Getter of _name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def del_name(self):
        del self._name
    name = property(get_name, set_name, del_name, "")

    #Setter and Getter of _age
    def get_age(self):
        return self._age
    def set_age(self, value):
        self._age = value
    def del_age(self):
        del self._age
    age = property(get_age, set_age, del_age, "")

    #Setter and Getter of _gender
    def get_gender(self):
        return self._gender
    def set_gender(self, value):
        self._gender = value
    def del_gender(self):
        del self._gender
    gender = property(get_gender, set_gender, del_gender, "")
    
    #Setter and Getter of _id
    def get_id(self):
        return self._id
    def set_id(self, value):
        self._id = value
    def del_id(self):
        del self._id
    id = property(get_id, set_id, del_id, "")

    #Setter and Getter of _password
    def get_password(self):
        return self._password
    def set_password(self, value):
        self._password = value
    def del_password(self):
        del self._password
    password = property(get_password, set_password, del_password, "")

    #Setter and Getter of _securityQ
    def get_security_q(self):
        return self._security_q
    def set_security_q(self, value):
        self._security_q = value
    def del_security_q(self):
        del self._security_q
    securityQ = property(get_security_q, set_security_q, del_security_q, "")

    #Setter and Getter of _securityQAns
    def get_security_q_ans(self):
        return self._security_q_ans
    def set_security_q_ans(self, value):
        self._security_q_ans = value
    def del_security_q_ans(self):
        del self._security_q_ans
    securityQAns = property(get_security_q_ans, set_security_q_ans, del_security_q_ans, "")

    #Get user details
    def get_user_details(self, user):
        pass_check = pwinput.pwinput(prompt="Please enter password: ")
        if pass_check == self._password:
            print(f"\nName: {self._name}, Age: {self._age}, Gender: {self._gender}, ID: {self._id}\n")
            main_menu(user)
        else:
            print("Wrong password")
            pass_forget_check(user, 1)

#Define bank class and methods
class Bank(User):
    def __init__(self, name, age, gender, id, password, securityQ, securityQAns, accountBalance):
        super().__init__(name, age, gender, id,  password, securityQ, securityQAns)
        self._accountBalance = accountBalance
        credentials = get_db_data()
        if self._id not in credentials.get("id"):
            self.store_user_account()

    #Setter and Getter of _accountBalance
    def get_account_balance(self):
        return self._accountBalance
    def set_account_balance(self, value):
        self._accountBalance = value
    def del_account_balance(self):
        del self._accountBalance
    accountBalance = property(get_account_balance, set_account_balance, del_account_balance, "")
    
    # Account creation for user
    def store_user_account(self):
        users_db_insert_query = """INSERT INTO users_credentials(users_name, users_age, users_gender, users_id, users_pass, users_security_question, users_security_question_ans, users_account_balance)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        form = (self._name, self._age, self._gender, self._id, self._password, self._security_q, self._security_q_ans, self._accountBalance)
        cursor.execute(users_db_insert_query, form)
        users_db.commit()

    #Deposit money method
    def deposit_money(self, user):
        pass_check = pwinput.pwinput(prompt="Please enter password: ")
        if pass_check == self._password:
            try:
                money = float(input("Enter deposit amount: "))          
                self._accountBalance += money
                credentials = get_db_data()
                index = int(credentials.get("id").index(int(self._id))) + 1
                print(index)
                db_balance_update_query = """UPDATE users_credentials
                                        SET users_account_balance = %s
                                        WHERE id = %s"""
                form = (self._accountBalance, index)
                cursor.execute(db_balance_update_query, form)
                users_db.commit()
                credentials = get_db_data()
                print(credentials)
                print(f"\nBalance: {str(self._accountBalance)}\n")
            except ValueError as error_name:
                print("Enter a numerical value!!!")
                print(error_name)
            main_menu(user)
        else:
            print("Wrong password")
            pass_forget_check(user, 1)
    
    #Withdraw money method
    def withdraw_money(self, user):
        pass_check = pwinput.pwinput(prompt="Please enter password: ")
        if pass_check == self._password:
            try:
                money = float(input("Enter withdraw amount: "))
                self._accountBalance -= money
                credentials = get_db_data()
                index = int(credentials.get("id").index(int(self._id))) + 1
                db_balance_update_query = """UPDATE users_credentials
                                        SET users_account_balance = %s
                                        WHERE id = %s"""
                form = (self._accountBalance, index)
                cursor.execute(db_balance_update_query, form)
                users_db.commit()
                credentials = get_db_data()
                print(f"\nBalance: {str(self._accountBalance)}\n")
            except ValueError:
                print("Enter a numerical value!!!")
            main_menu(user)
        else:
            print("Wrong password")
            pass_forget_check(user, 1)

    #View balance money method
    def view_balance(self, user):
        pass_check = pwinput.pwinput(prompt="Please enter password: ")
        if pass_check == self._password:
            print(f"\nBalance: {str(self._accountBalance)}\n")
            main_menu(user)
        else:
            print("Wrong password")
            pass_forget_check(user, 1)

#Defining custom ERRORS
class ChoiceNotExist(Exception):
    #Raised when user chooses a non existing option
    pass
class PassWrong(Exception):
    #Raised when user inputs wrong password
    pass
class WrongId(Exception):
    #Raised when user inputs wrong ID
    pass

#Function for sign up form
def sign_up_form():
    check = True
    while check:
        try:
            name_main = input("Please enter your name: ")
            name_test = float(name_main)
            raise ZeroDivisionError
        except ZeroDivisionError:
            print("Enter a valid name!!!")
            continue
        except ValueError:
            pass       
        try:
            age_main = input("Please enter your age: ")
            age_test = int(age_main)
        except ValueError:
            print("Enter a valid age!!!")
            continue
        try:
            gender_main = input("Please enter your gender: ")
            gender_test = float(gender_main)
            raise ZeroDivisionError
        except ZeroDivisionError:
            print("Enter a valid gender!!!")
            continue
        except ValueError:
            pass
        try:
            id_main = input("Please enter your ID: ")
            id_test = int(id_main)
            credentials = get_db_data()
            if int(id_main) in credentials.get("id"):
                raise ValueError
        except ValueError:
            print("Enter a valid ID!!!")
            continue
        password_main = pwinput.pwinput(prompt="Please enter a password: ")
        try:
            choice = input("""Please choose a security question:
            1: father name
            2: mother name
            3: pet name
            Choice: """)
            if choice == "1":
                sec_q_main = "1"
                sec_q_ans_main = input("What is your father's name? ")
            elif choice == "2":
                sec_q_main = "2"
                sec_q_ans_main = input("What is your mother's name? ")
            elif choice == "3":
                sec_q_main = "3"
                sec_q_ans_main = input("What is your pet's name? ")
            else:
                raise ChoiceNotExist
        except ChoiceNotExist:
            print("Please choose only from the given choices: ")
            continue
        check = False
    print("Account created successfully!\n")
    return name_main, age_main, gender_main, id_main, password_main, sec_q_main, sec_q_ans_main

#Function to call sign up form and create a user
def sign_up():
    user_details_1 = sign_up_form()
    user = Bank(user_details_1[0], user_details_1[1], user_details_1[2],
    user_details_1[3], user_details_1[4], user_details_1[5], user_details_1[6], 0)
    main_menu(user)

#Sign in function
def sign_in():
    try:
        choice = input("Do you have an account? [y/n]: ")
        if choice in ['y', 'Y']:
            credentials = get_db_data()
            print(credentials)
            id_in = input("Enter ID: ")
            if int(id_in) in credentials.get("id"):
                try:
                    index = credentials.get("id").index(int(id_in))
                    pass_w = pwinput.pwinput(prompt="Enter password: ")
                    if pass_w == credentials.get("pass")[index]:
                        print("Sign-In successful")
                        user_details_1 = []
                        for key in credentials.keys():
                            user_details_1.append(credentials.get(key)[index])
                        user = Bank(user_details_1[0], user_details_1[1], user_details_1[2],
                        user_details_1[3], user_details_1[4], user_details_1[5],
                        user_details_1[6], user_details_1[7])
                        main_menu(user)
                    else:
                        raise PassWrong
                except PassWrong:
                    print("Wrong password!")
                    user = [0, 1, 2, id_in]
                    pass_forget_check(user[3], 0)
            else:
                raise WrongId
        elif choice in ['n', 'N']:
            print("Go sign up")
            sign_up()
        else:
            raise ChoiceNotExist
    except ChoiceNotExist:
        print("Choose ONLY from the given options")
        sign_in()
    except WrongId:
        print("Wrong ID!")
        sign_in()

#Main menu
def main_menu(user):
    try:
        credentials = get_db_data()
        print(credentials)
        choice = input("""Enter:
        1: show account details
        2: show account balance
        3: withdraw
        4: deposit
        5: sign-out
        0: exit from system
        Choice: """)
        if choice == "1":
            user.getUserDetails(user)
        elif choice == "2":
            user.viewBalance(user)
        elif choice == "3":
            user.withdrawMoney(user)
        elif choice == "4":
            user.depositMoney(user)
        elif choice =="5":
            print("Successfully signed out")
            sign_in()
        elif choice == "0":
            if users_db.is_connected():
                users_db.close()
                cursor.close()
                print("MySQL conncection is closed")
            print("Closing")
        else:
            raise ChoiceNotExist
    except ChoiceNotExist:
        print("Please choose only from the given choices: ")
        main_menu(user)

#Initialize function
def initialize_program():
    while True:
        try:
            choice = input("Enter [1] to sign in or [2] to sign up or [0] to exit: ")
            if choice == "1":
                sign_in()
            elif choice == "2":
                sign_up()
            elif choice == "0":
                if users_db.is_connected():
                    cursor.close()
                    users_db.close()
                    print("MySQL conncection is closed")
                print("Closing")
                break
            else:
                raise ChoiceNotExist
        except ChoiceNotExist:
            print("Choose ONLY from the given choices")

#Initialization
initialize_program()
