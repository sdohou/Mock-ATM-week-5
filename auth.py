import random
import validation
import database
from getpass import getpass

# Datetime object- current date and time
from datetime import datetime

now = datetime.now()


# Initializing the system (Welcome Page)
def init():
    print("\n ********* Welcome to Python Bank ********* \n")
    dt_string()
    have_account = int(input("\nDo you have account with us: 1 (Yes) 2 (No) \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected an invalid option.")
        init()


# Login
# - account number & password

def login():
    print("********* Login ***********")
    global account_number_from_user

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password? \n")

        user = database.authenticated_user(account_number_from_user, password)
        print(user)
        if user:
            bank_operation(user)

        print('Invalid account number or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


# Register
# - First name, last name, email, password

def register():
    print("****** Register for an Account *******")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = getpass("Create your password: \n")

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your account has been created.")
        print("=== ===== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe.")
        print("=== ===== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


# Bank operations
def bank_operation(user):
    print("Hello %s %s " % (user[0], user[1]))

    selected_option = int(input("\nWhat would you like to do? (1) Deposit (2) Withdrawal (3) Exit Session (4) Logout  \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        exit()

    elif selected_option == 4:
        logout()

    else:
        print("Invalid option selected.")
        bank_operation(user)


def deposit_operation(user):
    current_balance = user[4]
    print("****** Make a Deposit ******")
    print('Your account balance is: \n', int(current_balance))
    deposit_amount = input('How much would you like to deposit? \n')
    current_balance = int(current_balance) + int(deposit_amount)
    user[4] = current_balance

    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    user_db_path = "data/user_record/"
    f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
    f.write(updated_user)
    f.close()

    print('Transaction complete. Your balance is now: {}'.format(current_balance))

    return exit()


def withdrawal_operation(user):
    current_balance = user[4]
    print("****** Make a Withdrawal ******")
    print('Your account balance is: \n', current_balance)
    withdrawal_amount = input('How much would you like to withdraw? \n')
    user[4] = current_balance

    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    user_db_path = "data/user_record/"
    f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
    f.write(updated_user)
    f.close()

    print('Transaction complete. Please take your cash.\n')
    current_balance = int(current_balance) - int(withdrawal_amount)
    print('Your current balance is now: {}'.format(current_balance))

    return exit()


# - Generate user account
def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def get_start_balance(user_details, balance):
    user_details[4] = balance


def get_end_balance(user_details):
    return user_details[4]


def exit():
    print('Session complete. Welcome back to the Main Menu.')


def logout():
    print('Thank you for choosing Python Bank. See you next time!')
    login()


# Datetime function
def dt_string():
    dt_string = now.strftime("==== %B %d, %Y %H:%M ====")  # type: str
    print(dt_string)


#### ACTUAL BANKING SYSTEM #####

init()
