# Project 1 - Crypto Wallet(Electronic Ledger)

# Success Criteria
# The electronic ledger is a text-based software (Runs in the Terminal).
# The electronic ledger display the basic description of the cryptocurrency selected.
# The electronic ledger allows to enter, withdraw and record transactions.
# The electronic ledger is password-protected.
# The electronic ledger shows past records of the cryptocurrency selected up to one month.
# The electronic ledger shows useful statistics such as overall gain/loss
# The electronic ledger allows to convert from USD to the crypto or vice versa

import maskpass
import yfinance as yf

import simple_login
## Initial Setup ##
# Importing Modules
from my_lib import validate_int_input, validate_float_input, validate_date_input

# Defining Variables
password = "1234"
crypto = "ETH-USD"
ChosenTicker = yf.Ticker(crypto)
crypto_name = "Ethereum"
crypto_description = '''Ethereum is a technology for building apps and organizations, holding assets, transacting and communicating without being controlled by a central authority.
There is no need to hand over all your personal details to use Ethereum - you keep control of your own data and what is being shared. 
Ethereum has its own cryptocurrency, Ether, which is used to pay for certain activities on the Ethereum network. 
(Source: “What Is Ethereum?” Ethereum.org, ethereum.org/en/what-is-ethereum/.)
'''
username = "John Doe"
colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m",
          "\033[0;37m", "\033[0;38m", "\033[0;39m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m",
          "\033[0;44m", "\033[0;45m", "\033[0;46m", "\033[0;47m", "\033[0;48m", "\033[0;49m", "\033[0;50m",
          "\033[0;51m", "\033[0;52m", "\033[0;53m", "\033[0;54m", "\033[0;55m", "\033[0;56m", "\033[0;57m",
          "\033[0;58m", "\033[0;59m", "\033[0;60m", "\033[0;61m", "\033[0;62m", "\033[0;63m", "\033[0;64m",
          "\033[0;65m", "\033[0;66m", "\033[0;67m", "\033[0;68m", "\033[0;69m", "\033[0;70m", "\033[0;71m",
          "\033[0;72m", "\033[0;73m", "\033[0;74m", "\033[0;75m", "\033[0;76m", "\033[0;77m", "\033[0;78m",
          "\033[0;79m", "\033[0;80m", "\033[0;81m", "\033[0;82m", "\033[0;83m", "\033[0;84m", "\033[0;85m",
          "\033[0;86m", "\033[0;87m", "\033[0;88m", "\033[0;89m", "\033[0;90m", "\033[0;91m", "\033[0;92m"]
end_code = "\033[00m"
widthcentering = 100

## End of Initial Setup ##

## Landing Page ##
print(f"{colors[2]}Welcome to the Electronic Ledger{end_code}")
pass_wrong_count = 0
username = input("Please enter your username: ")
password = maskpass.askpass("Please enter your password: ")
temp = simple_login.simple_login(username, password)
while pass_wrong_count < 3:
    while temp == False:
        pass_wrong_count += 1
        print(f"{colors[1]}Incorrect username or password. Please try again.{end_code}")
        username = input("Please enter your username: ")
        password = maskpass.askpass("Please enter your password: ")
        temp = simple_login.simple_login(username, password)
    else:
        print(f"{colors[2]}Welcome {username.capitalize()}{end_code}".center(50))
        break
else:
    print(f"{colors[1]}Too many incorrect attempts. Exiting program.{end_code}")
print(f"{colors[2]}Access Granted{end_code}".center(50))

menu = colors[6] + """
1. View Basic Description of the Cryptocurrency
2. View Wallet Balance
3. Enter, Withdraw, Record a Transaction
4. View Past Records of the Cryptocurrency
5. View Useful Statistics
6. Exit
""" + end_code


## Functions ##
def basic_description():
    print(f"{colors[1]}{crypto_name}{end_code}".center(50))
    print(crypto_description.center(75))


def wallet_balance():
    balance = 0
    with open("wallet.csv", "r") as file:
        wallet = file.readlines()
        i = 0
        for line in wallet:
            if i > 0:
                data = line.split(",")
                # print(data)
                balance += float(data[1])
            i += 1
    temp = f"You currently have {colors[1]}{balance} {crypto_name}{end_code} in your wallet, which is worth {colors[1]}{round(balance * float(ChosenTicker.info['regularMarketPrice']), 2)} USD{end_code} currently."
    temp = temp.center(widthcentering, "=")
    # print(colors[2] + "=" * widthcentering + end_code)
    print(temp)
    # print(colors[2] + "=" * widthcentering + end_code)


def enter_withdraw_record():
    print(f"{colors[4]}Enter, Withdraw, Record a Transaction{end_code}")
    print(colors[4] + """
        1. Enter a transaction
        2. Withdraw a transaction
        3. Record a transaction
        4. Back to main menu
        """ + end_code)
    option = validate_int_input("Please choose an option: ")
    if option == 1:
        with open("wallet.csv", "a") as file:
            print("Enter a transaction")
            date = validate_date_input("Please enter the date of the transaction(YYYY-MM-DD): ")
            amount = validate_float_input("Please enter the amount of ETH changed: ")
            price = ChosenTicker.history(start=date, end=date)['Open'][0]
            file.write(f"\n{date},{amount},{price}")
        print(f"{colors[2]}Transaction recorded!{end_code}")
    elif option == 2:
        print("Withdraw a transaction")
        print("Here are the current transactions:")
        with open("wallet.csv", "r") as file:
            wallet = file.readlines()
            i = 0
            for line in wallet:
                if i > 0:
                    data = line.split(",")
                    print(f"{data[0]}: {data[1]}")
                i += 1
        date = validate_date_input("Please enter the date of the transaction(YYYY-MM-DD): ")
        a_file = open("wallet.csv", "r")
        list_of_lines = a_file.readlines()
        a_file.close()
        new_file = open("wallet.csv", "w")
        for line in list_of_lines:
            if str(date) not in line:
                new_file.write(line)
        new_file.close()
        print(f"{colors[2]}Transaction withdrawn!{end_code}")
    elif option == 3:
        print("Record a transaction")
        date = validate_date_input("Please enter the date of the transaction(YYYY-MM-DD): ")
        amount = validate_float_input("Please enter the amount of ETH changed: ")
        price = ChosenTicker.history(start=date, end=date)['Open'][0]
        with open("wallet.csv", "a") as file:
            file.write(f"\n{date},{amount},{price}")
        print(f"{colors[2]}Transaction recorded!{end_code}")


    elif option == 4:
        pass


def past_records():
    # gets past month(based on current date) of data of the cryptocurrency from the plugin yfinannce and print it for the user
    hist = ChosenTicker.history(period="1mo")
    print(hist)


def useful_stats():
    # shows the user the current price of the cryptocurrency, the 52 week high and low, and the market cap
    # shows the user their over gains and losses of the currency based on their wallet
    print(f"{colors[1]}{crypto_name}{end_code}".center(50))
    print(f"Current Price: {colors[1]}{ChosenTicker.info['regularMarketPrice']}{end_code}")
    print(f"52 Week High: {colors[1]}{ChosenTicker.info['fiftyTwoWeekHigh']}{end_code}")
    print(f"52 Week Low: {colors[1]}{ChosenTicker.info['fiftyTwoWeekLow']}{end_code}")
    print(f"Market Cap: {colors[1]}{ChosenTicker.info['marketCap']}{end_code}")
    balance = 0
    USDbalance = 0
    with open("wallet.csv", "r") as file:
        wallet = file.readlines()
        i = 0
        for line in wallet:
            if i > 0:
                data = line.split(",")
                # print(data)
                balance += float(data[1])
                USDbalance += float(data[1]) * float(data[2])
                # print(USDbalance)
            i += 1
        balance = balance * float(ChosenTicker.info['regularMarketPrice'])
        if balance > USDbalance:
            print(f"You have made {colors[2]}{balance - USDbalance}{end_code} in gains")
        else:
            print(f"You have made {colors[1]}{balance - USDbalance}{end_code} in losses")


## Main Program ##
while True:
    print("Options".center(50))
    print(menu)
    choice = validate_int_input("Please enter your choice: ")
    if choice == 1:
        basic_description()
    elif choice == 2:
        wallet_balance()
    elif choice == 3:
        enter_withdraw_record()
    elif choice == 4:
        print(f"{colors[1]}View Past Records of the Cryptocurrency{end_code}")
        past_records()
    elif choice == 5:
        # print(f"{colors[1]}View Useful Statistics{end_code}")
        useful_stats()
    elif choice == 6:
        print(f"{colors[1]}Exiting...{end_code}")
        exit()
