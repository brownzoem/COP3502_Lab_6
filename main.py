# This is the part 2 of Lab 6 if you are working individually
# This is required to get full credit as a replacement for the partner

# Instructions:
# 1. Email me with your github email to be added as a collaborator
# 2. Clone this repo
# 3. Create a function that if your name is printed, the function asks the user a joke
# 4. Be sure to make name the function with your name so that I can give you credit
# 5. push your code back to the remote repository and ensure that it is added to the github

# Example is shown below

def zoe_brown():
    user_response = input('What did the fish say when he swam into a wall?')
    print('Dam')

#Jose Ortega encode function
def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

# Andy Hagen
def decode(encoded_pass):
    # Create an empty string assigned to a new variable to store the decoded password
    decoded_password = ""

    for i in range(0, len(encoded_pass)):
        encoded_digit = int(encoded_pass[i]) - 3
        decoded_password += str(encoded_digit)

    # Return decoded password string
    return decoded_password


def main():
    name = input("What is your name?")

    if name == 'Zoe Brown':
        zoe_brown()

    # Add your code below:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
