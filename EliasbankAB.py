#inloggning
bankId = 200102186798 #Inloggnings 'namn'
userBankId = int(input("bankID: ")) #Användare sätter värde för 'userBankId' - intiger
import time # Används vid olika moment, Delay

if userBankId != bankId: #Om användaren matchat det korrekta inloggninsnamnet så gå vidare
    print("Fel BankId!")
    time.sleep(3)
    exit() #Om använderen inte matchat det korrekta inloggninsnamnet, avsluta
else:

    menu = 0
    file = open("Saldo.txt", "r+")
    saldo = float(file.readline()) #Float - Data typ för decimal tal
    file.close()

    while menu == 0:

        menu = int(input("Menu: 1.deposit 2.withdraw 3.saldo 4.logout")) # Alternativ beroende på ärende
        if menu == 1:
            file = open("saldo.txt", "w") # Öppnar saldofilen med write
            deposit = float(input("Deposit, how much? ")) # Användare får skriva float för hur mycket hen ska lägga in
            saldo = saldo + deposit # Uträkning
            file.write(str(saldo)) # Skriver in Uträkningsresultatet i filen
            file.close() # Stänger fil
            print(saldo) # Printar saldo
            menu = 0 # återgå till loopens början

        elif menu == 2:
            file = open("saldo.txt", "w")
            withdraw = float(input("Withdraw, how much? "))
            saldo = saldo - withdraw #uträkning
            if saldo <= 0: # Ifall 'saldo' är mindre än noll (-) printa observeringsmeddelande
                print("OBSERVE! Negative balance!")
            print(saldo)
            file.write(str(saldo))
            file.close()
            menu = 0

        elif menu == 3:
            print(saldo)
            time.sleep(1) # Vänta 1 sek tills den återgår till menu 0
            menu = 0
        elif menu == 4:
            print ("Logging out...")
            time.sleep(3)   # Väntar 5 sekunder innan utloggning.
            exit()

        else:
            menu = 0 # ifall skrivfel, återgå till loopens början