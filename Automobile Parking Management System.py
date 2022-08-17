import random
import time
from datetime import datetime

# Saleha's part(FA20-BCS-083)
def start():
    print("\n"+"\t"*8+"===============================================\n"+
          "\t"*8+"Welcome to Automobile Parking Management System"+
          "\n"+"\t"*8+"===============================================")
    print("\t"*10+"Group no. 15\n"+
          "\t"*8+"===============================================\n"+
          "\t"*8+"\t\tCreated by:\n"+
          "\t"*8+"\t\tFA20-BCS-058\n"+
          "\t"*8+"\t\tFA20-BCS-083\n"+
          "\t"*8+"\t\tFA20-BCS-095\n"+
          "\t"*8+"\t\tFA20-BCS-104\n"+
          "\t"*8+"===============================================\n")
    print("\n\n********************************************************************************************\n"+
          "1. Your token ID will be used to exit your car.\n"+
          "2. Parking limit will be for one day only.\n"+
          "3. Parking bill wil be paid online.\n"+
          "4. If parking limit of one day exceeds, then your car will be moved to additional section.\n"+
          "5. If your car is moved to additional section, contact at number provided on complain tab.\n"+
          "6. In case you lose your token ID, contact at numbers provided on complaint tab.\n"+
          "********************************************************************************************")
    print("1. Press \"1\" to park your car.\n"+
          "2. Press \"2\" to exit your car.\n"+
          "3. Press \"3\" to register your complaint.\n"+
          "4. Press \"4\" for feedback.\n"+
          "5. Press \"5\" to view database.")


# Muneeb's part(FA20-BCS-104)
def park():
    rnd = random.randint(0, 5000)
    print("Enter your car number")
    car_number = input(": ")
    print("Enter your model number")
    car_model = input(": ")
    print("\nOn which floor you want to park your car?\n" +
          "Press \"0\" for Ground floor\n" +
          "Press \"1\" for 1st floor")
    floor = input(": ")
    chk = checkslot(floor)
    if (chk):
    #   Saleha's part`````````````````
        while True:
            print("\nYour parking bill is RS. 80\n"+
                  "which payment method you want to use?\n"+
                  "1. Easypaisa\n"+
                  "2. Jazzcash")
            q = input(": ")
            if q == '1':
                print("\nPay your bill at these numbers\n"+
                      "1. 03140000100\n"+
                      "2. 03020000200")
                break
            elif q == '2':
                print("\nPay your bill at these number\n"+
                      "1. 03140000100\n"+
                      "2. 03020000200")
                break
            else:
                print("Invalid input!")
        print("Have you paid your bill?(y/n)")
        g = input(": ").lower()
        if g == 'y':
    #    Saleha's part``````````````
            with open("car.txt", "r") as file:
                all = file.readlines()
                l = False
                for i, line in enumerate(all):
                    if i < 2:
                        if int(floor) == 0:
                            g = False
                            for j in range(0, 21):
                                a = all[j].split(" ")
                                if int(a[1]) == 0:
                                    t1 = datetime.now()
                                    all[j] = "Slot#" + str(j + 1) + ":" + " 1 " + "" + str(car_number) + "_" + str(car_model) + " A" + str(rnd) + " " + str(t1) + "\n"
                                    slot = "Slot#" + str(j + 1)
                                    file = open("car.txt", "w")
                                    file.writelines(all)
                                    file.close()
                                    l = True
                                    g = True
                                    break
                                else:
                                    print("", end="")
                            if (g):
                                print("", end="")
                                break
                            else:
                                print("Ground floor parking full")
                        elif int(floor) == 1:
                            for k in range(20, 41):
                                f = False
                                a = all[k].split(" ")
                                if int(a[1]) == 0:
                                    t2 = datetime.now()
                                    all[k] = "Slot#" + str(k + 1) + ":" + " 1 " + "" + str(car_number) + "_" + str(car_model) + " A" + str(rnd) + " " + str(t2) + "\n"
                                    slot = "Slot#" + str(k + 1)
                                    file = open("car.txt", "w")
                                    file.writelines(all)
                                    file.close()
                                    l = True
                                    f = True
                                    break
                                else:
                                    print("", end="")
                            if (f):
                                print("", end="")
                                break
                            else:
                                print("First floor parking full.")
                                break
                        else:
                            print("Wrong Input")
                            break
                    else:
                        break
                if (l):
            #    Saleha's part
                    print("Your payment is being processed, Kindly wait for a moment.")
                    time.sleep(2)
                    print("Checking account details.")
                    time.sleep(3)
                    print("Verifying bill.")
                    time.sleep(2)
                    print("Payment accepted.")
                    time.sleep(2)
                    print("Your bill has been paid.\n")
            #    Saleha's part
                    print("Park your car at:", "\n" + "\"" + slot + "\"" + "\n")
                    print("Your token number is", "\n" + "\"" + "A" + str(rnd) + "\"" + "\n")
                    print("``````````````````````````````\n" +
                          "Thanks for using our services\n" +
                          "```````````````````````````````")
                else:
                    print("No Parking Available on any Floor")
                with open("database.txt", "a") as a:
                    a.write(f"{slot} : {car_number}_{car_model} at {time.asctime(time.localtime(time.time()))}\n")
                    a.close()
        elif g == 'n':
            print("You can't park your car without paying your bill.")
        else:
            print("invalid input!")
    else:
        if floor == '0':
            print("Ground floor parking full.")
        elif floor == '1':
            print("First floor parking full.")
        else:
            print("", end="")


# Muneeb's part(FA20-BCS-104)
def checkslot(floor):
    with open("car.txt", "r") as file:
        all = file.readlines()
        if int(floor) == 0:
            for j in range(0, 21):
                a = all[j].split(" ")
                if int(a[1]) == 0:
                    return True # slot is empty
            return False # not empty
        elif int(floor) == 1:
            for k in range(20, 41):
                a = all[k].split(" ")
                if int(a[1]) == 0:
                    return True
            return False
        else:
            print("", end="")


# Ismail's part(FA20-BCS-058)
def vehicle_exit():
    print("\nTake out your car from parking lot and enter your Token ID : ")
    token = input(": ")
    with open("car.txt", "r") as file:
        cnt = file.readlines()
        l = False
        for i, line in enumerate(cnt):
            hours = 0
            if i < 1:
                for j in range(0, 40):
                    a = cnt[j].split(" ")
                    if int(a[1]) == 1:
                        if str(a[3]).strip('\n') == str(token):
                #   Muneeb's part```````````````
        #   Additinal section
                            now  = datetime.now()
                            qa = a[4].split("-")
                            dt = a[5].split(":")
                            flt = float(dt[2])
                            then = datetime(int(qa[0]), int(qa[1]), int(qa[2]), int(dt[0]), int(dt[1]), int(flt))
                            duration = now - then
                            sec = duration.total_seconds()
                            hours = sec/3600
                #   Muneeb's part```````````````
                            cnt[j] = "Slot#" + str(j + 1) + ":" + " 0" + "\n"
                            file = open("car.txt", "w")
                            file.writelines(cnt)
                            file.close()
                            l = True
                            break
            else:
                break
        #   Muneeb's part```````````````
            if str(hours) > '24':
                print("\n*************************************************************************************************\n"
                      "Your car has been moved to additionl section because it was parked here for more than 24 hours.\n"+
                      "Contact on numbers provided on complaint tab.\n"+
                      "***************************************************************************************************")
            else:
        #   Muneeb's part````````````````
                if(l):
                    print("Vehicle Successfully Exited")
                else:
                    print("Wrong Token Number")


# Yumna's part(FA20-BCS-095)
def complaint():
    print("\nIn case of any complaint, contact us at our toll-free numbers:\n"+
          "1. 03140000100\n"+
          "2. 03020000200\n"+
          "Thank you for using our service.\n"+
          "Goodbye, Have a safe drive!")


# Saleha's part(FA20-BCS-083)
def feedback():
    print("Kindly enter your name:")
    name = input(": ")
    print("Please do tell us your remarks on our service to improve our quality of service:")
    a = input(": ")
    f = open("Feedback.txt", "a")
    f.write(f"Feedback given by \"{name}\" at {time.asctime(time.localtime(time.time()))}:\n")
    f.write(">>> "+a+".")
    f.write("\n")
    print(f"Thank you for your feedback {name}.")
    f.close()


# Yumna's part(FA20-BCS-095)
def data():
    while True:
        print("Do you want to view database?(y/n)")
        d = input()
        if d == 'y':
            print("Enter username")
            r = input().title()
            print("Enter password")
            l = input()
            if r == 'Admin' and l == '1234':
                print("Press \"1\" to view database.\n"+
                      "Press \"0\" to clear database.")
                d = input()
                if d == '1':
                    w = open("Database.txt", "r")
                    z = w.read()
                    print(z)
                    w.close()
                    break
                elif d == '0':
                    print("Do you want to clear database?(y/n)")
                    c = input()
                    if c == 'y':
                        w = open("Database.txt", "w")
                        w.truncate()
                        print("Database cleared")
                        w.close()
                    elif c == 'n':
                        print("", end="")
                    else:
                        print("", end="")
                    break
                else:
                    print("Invalid Input!")
                    break
            elif r != 'Admin' or l != '1234':
                print("Wrong username and password")
                break
        elif d == 'n':
            print("", end="")
            break
        else:
            print("", end="")




if __name__ == "__main__":
    while True:
        start()
        z = input(": ")
        if z == '1':
            park()
        elif z == '2':
            vehicle_exit()
        elif z == '3':
            complaint()
        elif z == '4':
            feedback()
        elif z == '5':
            data()
        else:
            print("Invalid input, Enter again.")
