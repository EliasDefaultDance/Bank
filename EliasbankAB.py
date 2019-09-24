#inloggning
bankId = 200102186798
userBankId = int(input("bankID: "))

if userBankId != bankId:
    exit()
menu = 0
saldo = 0

while menu == 0:
    menu = int(input("Menu: 1.deposit 2.withdraw 3.logout"))
    if menu == 1:
        deposit = float(input("Deposit, how much? "))
        saldo = saldo + deposit
        print(saldo)
        menu = 0
    elif menu == 2:
        withdraw = float(input("Withdraw, how much? "))
        saldo = saldo - withdraw
        if saldo <= 0:
            print("OBSERVE! Negative balance!")
            menu = 0
        print(saldo)
        menu = 0
    elif menu == 3:
        print ("Logging out")
        exit()
    else:
         menu = 0