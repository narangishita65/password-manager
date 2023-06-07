# -------Password Manager:----------

# BasePasswordManager class

class BasePasswordManager:

    def __init__(self):
        # passwords list
        passwords_list = ['$@ramdom', '!#@123456', 'Ishita@0612']
        self.passwords_list = passwords_list

        # current password is last element in a list
        # self.current_password=self.passwords_list[-1]

    # old_passwords holds all previous passwords
    def old_passwords(self):
        self.old_passwords = self.passwords_list

    # get_password returns the current password of the user
    def get_password(self):
        self.current_password = self.passwords_list[-1]
        print('Current Password is:', self.current_password, '\n')

    # is_correct method takes a user input and compares with current password
    def is_correct(self, verify_password):
        if self.current_password == verify_password:
            print('Password is validated Successfully \n ')
        else:
            print('Please Enter a valid Password \n ')

        # PasswordManager class inheriting the properties of BasePasswordManager class


class PasswordManager(BasePasswordManager):

    # set_password method sets a new_password in passwords_list if passed all required cases
    def set_password(self, New_password):

        if len(New_password) < 6:
            print("New Password must have 6 characters or More")
            print("Password Change : UNSUCCESSFUL !")
            print("\n")

        elif New_password == self.current_password:
            print("Password Change: No Changes Detected")

        else:
            self.passwords_list.append(New_password)
            print("Password Change : SUCCESSFUL")
            print()

    # get_level method returns the security level of the given password and current password aswell
    def get_level(self, password):
        self.security_level = 0
        alphabet = False
        number = False
        special = False
        # checking for alphabets in password by using isalpha method
        for i in password:
            if i.isalpha():
                alphabet = True
        # checking for digits in password by using isdigit method
        for j in password:
            if j.isdigit():
                number = True
        # checking for special characters in password by taking ASCII values
        for k in password:
            if ord(k) in range(33, 47 + 1) or ord(k) in range(58, 64 + 1) or ord(k) in range(91, 96 + 1) or ord(
                    k) in range(123, 126 + 1):
                special = True

        # checking for number in a password
        if number == True and alphabet == False:
            self.security_level = 0
            print('Security level is', self.security_level)
            print('Password consists of Digits only \n')

        # checking for alphabets in password
        elif number == False and alphabet == True:
            self.security_level = 0
            print('Security level is', self.security_level)
            print('Password consists of Alphabets only \n')

        # checking for both numbers and alphabets in password
        elif alphabet == True and number == True and special == False:
            self.security_level = 1
            print('Security Level is', self.security_level)
            print('Password is alphanumeric \n')
        # checking for numbers,alphabets and special characters in password

        elif alphabet == True and number == True and special == True:
            self.security_level = 2
            print('Security level is', self.security_level)
            print('Password is alphanumeric with special characters \n')


if __name__ == '__main__':

    # object of PasswordManager
    base = PasswordManager()

    while (True):
        # Entry dialogue
        print("\nWelcome to Cisco Password Manager \n Please Enter Your choice\n")
        print("1. To check your current Password")
        print("2. To validate your Password")
        print("3. To set a new Password")
        print("4. To know security level of your current Password")
        print('5. To know security level of Entered Password')
        print("6. To Quit !\n")
        # taking user choice
        user_choice = input("Enter your choice :")

        if user_choice not in ['1', '2', '3', '4', '5', '6']:
            print('Enter a valid option')
            continue
        user_choice = int(user_choice)

        if user_choice == 1:
            base.get_password()

        elif user_choice == 2:
            password = input('Enter your password for Verification:')
            base.is_correct(password)

        elif user_choice == 3:
            New_password = input("Enter New Password: ")
            base.set_password(New_password)

        elif user_choice == 4:
            cp = base.current_password
            base.get_level(cp)

        elif user_choice == 5:
            Entered_password = input('Enter your Password:')
            base.get_level(Entered_password)

        elif user_choice == 6:
            print('Press Q for Quit and C for Continue')
            user_choice2 = input()
            if user_choice2 == 'Q':
                break
            if user_choice2 == 'q':
                break
            if user_choice2 == 'C':
                continue
            elif user_choice2 == 'c':
                continue

        else:
            print('Not a valid Option')
