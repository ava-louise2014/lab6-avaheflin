

#this is the menu options the user can choose from

def menu_display():

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


#this defines the process of encoding the password that the user inputs
def encode_password(password):
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password must be an 8-digit string containing only integers.")
    encoded_password = ""
    for digit in password:
        original_digit = int(digit)
        encoded_digit = (original_digit+3)%10
        encoded_password += str(encoded_digit)
    return encoded_password

if __name__ == '__main__':
    user_input = 0
    menu_display()
#these are the conditions of if the user inputs a certain number for the menu, and it tells the program what to do if that menu option is selected
    while True:
        menu_display()
        user_input = input("Please enter an option: ")
        #encoded option
        if user_input == '1':
            password_to_encode = input("Please enter your password to encode: ")
            password = "12345678" #Replace with your 8 digit password
            enocded_password = encode_password(password)
            print("Your password has been encoded and stored!", enocded_password)

        #exit option
        if user_input == '3':
            break
