print("Welcome to FurkanBank.\n"
      "Transactions\n"
      "1.Inquire Balance\n"
      "2.Deposit\n"
      "3.Withdraw Money\n"
      "4.Exit")

balance = 1000
while True:
    action = int(input("Choose your action: "))
    if(action==1):
        print("Current Balance:",balance)
        print("---------------")
    elif(action==2):
        amount = int(input("Amount of money to be deposited: "))
        balance += amount
        print("Current Balance: {}".format(balance))
        print("---------------")
    elif(action==3):
        amount = int(input("Amount to be withdrawn: "))
        if(balance < amount):
            print("Insufficient Funds")
            print("---------------")
        else:
            balance -= amount
            print("Current Balance: {}".format(balance))
            print("---------------")
    elif(action==4):
        print("We hope you come again.\n-FurkanBank")
        break
    else:
        print("Incorrect entry. Please try again.")