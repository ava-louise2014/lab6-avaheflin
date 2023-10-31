

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

#nora nguyen
def decode(encoded_password):
    decoded = []
    for i in encoded_password:
        x = int(i)
        x = (x-3)%10
        decoded.append(str(x))
        decoded_password = ''.join(decoded)
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

if __name__ == '__main__':
    user_input = 0
#these are the conditions of if the user inputs a certain number for the menu, and it tells the program what to do if that menu option is selected
    while True:
        menu_display()
        user_input = input("Please enter an option: ")
        #encoded option
        if user_input == '1':
            password_to_encode = input("Please enter your password to encode: ")
            enocded_password = encode_password(password_to_encode)
            print("Your password has been encoded and stored!", enocded_password)
        if user_input == '2':
            decode(enocded_password)
        #exit option
        if user_input == '3':
            break
