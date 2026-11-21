from PySide6 import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout

while True:
    count = 3
    has_ticket = False
    has_backed = False
    while count > 0:
        if has_ticket:
            f = "Ticket: Yes"
        else:
            f = "Ticket: No"
        if has_backed:
            g = "Backpack: Yes"
        else:
            g = "Backpack: No"
        print(f"Turns left: {count}\n{f}\n{g}")
        print("1. Buy a ticket")
        print("2. Go to the platform")
        print("3. Pick up your backpack")
        choise  = input("What will you do ?")
        if choise != '1' and choise != '2' and choise != '3':
            print("Please enter either 1 ,2 or 3")
        else:
            count = count - 1
            if choise == "1":
                print("You went to the ticket office")
                has_ticket = True
            elif choise == "2":
                if has_ticket and has_backed:
                    print("You boarded the train!")
                    break
                else:
                    print("You need your ticket and backpack to board.")
                print("You went to the platform")
            elif choise == "3":
                has_backed = True
                print("You picked up your backpack.")

    else:
        print("The train has left")

    l = input("Play again? (y/n)")
    if l == 'y':
        continue
    else:
        break

