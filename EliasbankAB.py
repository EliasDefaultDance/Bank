#inloggning
bankId = 200102186798 #Inloggnings 'namn'
userBankId = int(input("bankID: ")) #Användare sätter värde för 'userBankId' - intiger

if userBankId != bankId: #Om användaren matchat det korrekta inloggninsnamnet så gå vidare
    exit() #Om använderen inte matchat det korrekta inloggninsnamnet, avsluta

menu = 0
file = open("Saldo.txt", "r")
saldo = float(file.readline()) #Float - Data typ för decimal tal
file.close()

while menu == 0:

    menu = int(input("Menu: 1.deposit 2.withdraw 3.logout"))
    if menu == 1:
        open("saldo.txt", "w")
        deposit = float(input("Deposit, how much? "))
        saldo = saldo + deposit
        file.write(str(saldo))
        file.close()
        print(saldo)
        menu = 0

    elif menu == 2:
        open("saldo.txt", "w")
        withdraw = float(input("Withdraw, how much? "))
        saldo = saldo - withdraw
        file.close()
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