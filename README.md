# Crypto Wallet

![](https://cdn.dribbble.com/users/900374/screenshots/5336936/wallet_2.gif)

<sub>Cryptocurrency Wallet by Framination on Dribble</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for these requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will to design and make a **digital ledger** for a client who is **Mr Sato**. The **digital ledger** will be about **storing transactions  regarding cryptocurrency** and is constructed using the software **Python** It will take  **until Project Week** to make and will be evaluated according to the criteria below.

Justify the tools/structure of your solution
I will be using Python for this solution because it provides easy data scraping functions and various libraries which could help in providing useful statistics to Mr Sato

I will be choosing Ethereum(ETHUSD) as my cryptocurrency for this solution

Ethereum is a technology for building apps and organizations, holding assets, transacting and communicating without being controlled by a central authority. There is no need to hand over all your personal details to use Ethereum - you keep control of your own data and what is being shared. Ethereum has its own cryptocurrency, Ether, which is used to pay for certain activities on the Ethereum network. 
(“What Is Ethereum?” Ethereum.org, [ethereum.org/en/what-is-ethereum/.](ethereum.org/en/what-is-ethereum/.))


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cryptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger is password-protected.
5. The electronic ledger shows past records of the cryptocurrency selected up to one month.
6. The electronic ledger shows useful statistics such as overall gain/loss
7. The electronic ledger allows to convert from USD to the crypto or vice versa

## Test Plan
| Description                           | Type           | Inputs                                                                                                                                                                                                                                                                      | Outputs                                                                                                                                                                            |
|---------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Login & Menu                          | Unit test      | 1. Run the Project1.py <br/>2. Input "joe" as Username & "123456" as Password                                                                                                                                                                                               | If the username and password matches what's stored in the user.csv file. It will transition user to the landing page which shows a menu of options                                 |
| View basic description of Crypto      | Unit test      | 1. User put in "1" into prompt following the menu                                                                                                                                                                                                                           | Print the basic description of the crypto that the ledger is based on                                                                                                              |
| View wallet balance                   | Unit test      | 1. User put in "2" into prompt following the menu                                                                                                                                                                                                                           | Prints the balance of the wallet from the wallet.csv and reference the current price of the crypto and prints that as well                                                         |
| Enter, Withdraw, Record a Transaction | Unit test      | 1. User put in "3" into prompt following the menu<br/> 2. User inputs a number from 1 to 3 to select the function they want(enter, withdraw or record) <br/> 3.User inputs amount of crypto changed(e.g : 1) <br/> 4. User inputs the date of transaction(e.g : 2022-07-09) | Program will enter, withdraw or record a transaction based on the selection and input of user and writes or removes data accordingly on wallet.csv                                 |
| View Past Records of the Crypto       | Unit test      | 1. User put in "4" into prompt following the menu                                                                                                                                                                                                                           | Program will query the yahoo finance platform the the data of the past month and print it in the terminal in a table format.                                                       |
| View Useful Statistics                | Unit test      | 1. User put in "5" into prompt following the menu                                                                                                                                                                                                                           | Program will query the yahoo finance platform through the plugin yfinance and print data such as 52 week highs/lows and overall gains/losses with reference to the wallet.csv file |
| Exit Function                         | Unit test      | 1. User put in "6" into prompt following the menu                                                                                                                                                                                                                           | Program quits                                                                                                                                                                      |
| Date input validation                 | Usability test | 1. User input wrong date or wrongly formatted date (not YYYY-MM-DD, e.g 220808) into prompt when entering, withdrawing or recording a transaction                                                                                                                           | Program prompts user that date input is wrong and prompts user to input again.                                                                                                     |
| Number input validation               | Usability test | 1. User input invalid characters(e.g : abc) into the prompt when asked to put in number(either int/float)                                                                                                                                                                   | Program prompts user that the input is invalid and prompts user to input again.                                                                                                    |
| Wrong password counter                | Usability test | 1. User inputs wrong username(e.g: bob)/password(e.g : dabuilder) when logging in                                                                                                                                                                                           | Program prompts user to retry logging in. When the amount of times the username/password is wrong exceeds 3, the program terminates itself.                                        |


# Criteria B: Design

## System Diagram
![](Assets/CryptoWallet_SysD2.jpeg)
*Fig.1* **System diagram of this program**

## Flow Diagrams

### Login
![](Assets/CryptoWallet_Login.jpg)

*Fig.2* **Flow diagram of the login function**

### Wallet Balance
![](Assets/CryptoWallet_WalletBalance.jpg)

*Fig.3* **Flow diagram of the wallet balance function**

### Withdrawing Transactions
![](Assets/CryptoWallet_Withdraw.jpg)

*Fig.4* **Flow diagram of the withdrawing transactions function**


## Record of Tasks
| Task No | Planned Action                  | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|---------------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram           | To have a clear idea of the hardware and software requirements for the proposed solution | 10min         | Sep 22                 | B         |
| 2       | Interview with the Client       | To discuss client's needs and define success criteria                                    | 5min          | Sep 23                 | A         |
| 3       | Code the Menu                   | To have menu items and title written on the screen                                       | 20min         | Sep 23                 | C         |
| 4       | Code authentication system      | A tested program to protect the application using a password with encryption             | 60min         | Sep 27                 | C         |
| 5       | Code Main Functions             | A function base of the program                                                           | 4hrs          | Sep 30                 | C         |
| 6       | Beautify Code and Final Touches | To finalize code and make it look nice                                                   | 2hrs          | Oct 1                  | C         |
| 7       | Form Test Plan                  | To a flexible test plan formed                                                           | 1hr           | Oct 1                  | B         |
| 8       | Draw Flow Diagrams              | To have completed the flow diagrams for the functions of the program                     | 1.5hrs        | Oct 3                  | B         |
| 9       | Record Demo Video               | To have a video demonstrating the program                                                | 15min         | Oct 4                  | B         |
 
# Criteria C: Development

## Techniques Used:
1. Functions
2. For/while loops
3. Input Validation
4. If/then/else statements
5. Encryption
6. File I/O
7. Exception Handling
8. List Comprehension


## Enter a transaction

```.py
    if option == 1:
        with open("wallet.csv", "a") as file:
            print("Enter a transaction")
            date = validate_date_input("Please enter the date of the transaction(YYYY-MM-DD): ")
            amount = validate_float_input("Please enter the amount of ETH changed: ")
            price = ChosenTicker.history(start=date, end=date)['Open'][0]
            file.write(f"\n{date},{amount},{price}")
        print(f"{colors[2]}Transaction recorded!{end_code}")
```

Above is the code that allows the user to enter transaction in to the digital ledger. Using the function validate_date_input, the user is prompted to input a date in the format YYYY-MM-DD. The function validate_float_input is used to validate the input of the amount of crypto changed. The price of the crypto at the date of the transaction is queried from the yahoo finance platform using the yfinance plugin. The data is then written to the wallet.csv file.


## Withdraw a transaction

```.py
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
```

The piece of code above allows the user to withdraw a transaction from the digital ledger. The user is prompted to input the date of the transaction they wish to withdraw. The wallet.csv file is read and the data is stored in a list. The list is then iterated through and the line with the date of the transaction is removed. The new list is then written to the wallet.csv file.



## Wallet Balance

```.py
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
    print(temp)
```

The code above allows the user to check the balance of their wallet. The wallet.csv file is read and the data is stored in a list. The list is then iterated through and the amount of crypto is added to the balance variable. The balance is then multiplied by the current price of the crypto to get the total value of the wallet in USD. The value is then printed to the screen. 


## Useful Statistics

```.py
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
```

The code above allows the user to check the current price of the crypto, the 52 week high and low, and the market cap. The user is also shown their gains and losses based on their wallet. The wallet.csv file is read and the data is stored in a list. The list is then iterated through and the amount of crypto is added to the balance variable. The balance is then multiplied by the current price of the crypto to get the total value of the wallet in USD. The value is then printed to the screen. 




## Video of the Program
[Video of the Program](https://drive.google.com/file/d/1dxL-tJmYLFgCwaq3jQzNEetSdhP3Wjtu/view?usp=sharing)
