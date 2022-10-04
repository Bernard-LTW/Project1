'''
def simple_login(user:str, password:str):
    """
    Simple Authentication, needs file users.csv
    :param user: string
    :param password: string
    :return: True/False if user is in database
    """

    with open("users.csv", "r") as f:
        database = f.readlines()
        output = False
    for line in database:
        line_cleaned = line.strip()
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]:
            output = True
            return output
            break
    return output
'''

import hmac


def simple_login(username: str, password: str) -> bool:
    """This function receives a username and a password and returns True if the username is in the database and the password is correct, otherwise returns False"""

    with open("users.csv", "r") as file:
        database = file.readlines()
    salty = "┻━┻︵╰(‵□′)╯︵┻━┻"
    to_hash = username + password + salty
    hashed_password = hmac.new(''.encode(), to_hash.encode(), 'sha512').hexdigest()
    #print(hashed_password)
    output = False
    for line in database:
        line_cleaned = line.strip()
        #print(line_cleaned)
        user, password = line_cleaned.split(",")
        if user == username and password == hashed_password:
            output = True
            break
    return output
#===============================================================================
#test1 = simple_login(username = "alice", password = "password123")
#print(test1)
