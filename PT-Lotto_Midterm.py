from datetime import date
import random
import time
import sys

lottoMoney = 1000
megaLottoMoney = 1000
superLottoMoney = 1000
luckyNumbers = 800

def potMoney():
    global lottoMoney
    global megaLottoMoney
    global superLottoMoney
    global luckyNumbers
    
def lotto():
    lotto_user = []
    
    potMoney()
    global lottoMoney
    
    print("**************************")
    print("Welcome to 6/42 Lotto")
    
    print("Lotto Prize Money: ", lottoMoney)
    print("----------------------------")
    print("--- Enter your numbers ---")

    user_counts = 0
    int(user_counts)

    while True:

        check = True
        bool(check)

        if user_counts != 6 or len(lotto_user) != 6:
            
            user_input = int(input("Enter number: "))
            user_counts = user_counts + 1
            lotto_user.append(user_input)
            
            print(lotto_user)
            
        if user_input > 42 or lotto_user != list(dict.fromkeys(lotto_user)) or user_input < 0:

            print("Please enter number below 42 only and do not type same number.")
            lotto_user.pop()
            user_counts = user_counts - 1
            #print(user_counts)
            print(lotto_user)
            
        elif user_counts == 6 and len(lotto_user) == 6:
            time.sleep(1)
            print("Numbers Cleared")
            time.sleep(1)
            print("Here are your entered number: ",lotto_user)
            break

    lotto_ai = []

    count = 0
    int(count)
    checker = False
    bool (checker)
    time.sleep(2)
    print("..Winning balls are shuffling...")
    time.sleep(4)
    print("Here are the winning the numbers!!")
    for i in range (0,6):
        number = random.randint(1,42)

        
        while number in lotto_ai:
            number = random.randint(1,42)
      
        lotto_ai.append(number)

    time.sleep(1)
    #lotto_ai.sort()
    print(lotto_ai)

    if set(lotto_ai) == set(lotto_user):
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("Wow!!! you won!")
        time.sleep(1)
        print("Congratulations!")
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
    else:
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("awww ... better luck next time dude! ")
        
        lottoMoney = lottoMoney + 500
        print("Current Lotto Prize Money: ", lottoMoney)
        
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
            
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
def megalotto():

    lotto_user = []

    potMoney()
    global megaLottoMoney
    
    print("**************************")
    print("Welcome to 6/45 Lotto")
    print("Mega Lotto Prize: " , megaLottoMoney)
    print("----------------------------")
    print("--- Enter your numbers ---")

    user_counts = 0
    int(user_counts)

    while True:

        check = True
        bool(check)

        if user_counts != 6 or len(lotto_user) != 6:
            
            user_input = int(input("Enter number: "))
            user_counts = user_counts + 1
            lotto_user.append(user_input)
            
            print(lotto_user)
            
        if user_input > 45 or lotto_user != list(dict.fromkeys(lotto_user)) or user_input < 0:

            print("Please enter number below 45 only and do not type same number.")
            lotto_user.pop()
            user_counts = user_counts - 1
            #print(user_counts)
            print(lotto_user)
            
        elif user_counts == 6 and len(lotto_user) == 6:
            time.sleep(1)
            print("Numbers Cleared")
            time.sleep(1)
            print("Here are your entered number: ",lotto_user)
            break
        
    lotto_ai = []

    count = 0
    int(count)
    checker = False
    bool (checker)

    time.sleep(2)
    print("..Winning balls are shuffling...")
    time.sleep(4)
    print("Here are the winning the numbers!!")
    for i in range (0,6):
        number = random.randint(1,45)
      
        while number in lotto_ai:
            number = random.randint(1,45)
      
        lotto_ai.append(number)
        
    if set(lotto_ai) == set(lotto_user):
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("Wow!!! you won!")
        time.sleep(1)
        print("Congratulations!")
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
    else:
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("awww ... better luck next time dude! ")
        megaLottoMoney = megaLottoMoney + 500
        print("Current Mega Lotto Prize: ", megaLottoMoney)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()


    
def superlotto():
    lotto_user = []

    potMoney()
    global superLottoMoney
    
    print("**************************")
    print("Welcome to 6/49 Lotto")
    print("Super Lotto Prize: " , superLottoMoney)
    print("----------------------------")
    print("--- Enter your numbers ---")

    user_counts = 0
    int(user_counts)

    while True:

        check = True
        bool(check)

        if user_counts != 6 or len(lotto_user) != 6:
            
            user_input = int(input("Enter number: "))
            user_counts = user_counts + 1
            lotto_user.append(user_input)
            
            print(lotto_user)
            
        if user_input > 49 or lotto_user != list(dict.fromkeys(lotto_user)) or user_input < 0:

            print("Please enter number below 49 only and do not type same number.")
            lotto_user.pop()
            user_counts = user_counts - 1
            #print(user_counts)
            print(lotto_user)
            
        elif user_counts == 6 and len(lotto_user) == 6:
            time.sleep(1)
            print("Numbers Cleared")
            time.sleep(1)
            print("Here are your entered number: ",lotto_user)
            break
        
    lotto_ai = []

    count = 0
    int(count)
    checker = False
    bool (checker)

    time.sleep(2)
    print("..Winning balls are shuffling...")
    time.sleep(4)
    print("Here are the winning the numbers!!")
    for i in range (0,6):
        number = random.randint(1,49)
      
        while number in lotto_ai:
            number = random.randint(1,49)
      
        lotto_ai.append(number)
        
    if set(lotto_ai) == set(lotto_user):
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("Wow!!! you won!")
        time.sleep(1)
        print("Congratulations!")
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
    else:
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("awww ... better luck next time dude! ")
        superLottoMoney = superLottoMoney + 500
        print("Current Super Lotto: ", superLottoMoney)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()

def luckythree():
    lotto_user = []

    potMoney()
    global luckyNumbers
    
    print("**************************")
    print("Welcome to Lucky Three!")
    print("Lucky 3 Prize: ", luckyNumbers)
    print("Choose numbers between 0-10")
    print("----------------------------")
    print("--- Enter your numbers ---")

    user_counts = 0
    int(user_counts)

    while True:

        check = True
        bool(check)

        if user_counts != 3 or len(lotto_user) != 3:
            
            user_input = int(input("Enter number: "))
            user_counts = user_counts + 1
            lotto_user.append(user_input)
            
            print(lotto_user)
            
        if user_input > 10 or lotto_user != list(dict.fromkeys(lotto_user)) or user_input < 0:

            print("Please enter number below 10 only and do not type same number.")
            lotto_user.pop()
            user_counts = user_counts - 1
            #print(user_counts)
            print(lotto_user)
            
        elif user_counts == 3 and len(lotto_user) == 3:
            time.sleep(1)
            print("Numbers Cleared")
            time.sleep(1)
            print("Here are your entered number: ",lotto_user)
            break
        
    lotto_ai = []

    count = 0
    int(count)
    checker = False
    bool (checker)

    time.sleep(2)
    print("..Winning balls are shuffling...")
    time.sleep(4)
    print("Here are the winning the numbers!!")
    for i in range (0,3):
        number = random.randint(1,10)
      
        while number in lotto_ai:
            number = random.randint(1,10)
      
        lotto_ai.append(number)
        
    if set(lotto_ai) == set(lotto_user):
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("Wow!!! you won!")
        time.sleep(1)
        print("Congratulations!")
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
    else:
        time.sleep(1)
        print("Your numbers: " , lotto_user)
        print("Winning numbers: ", lotto_ai)
        time.sleep(1)
        print("awww ... better luck next time dude! ")
        luckyNumbers = luckyNumbers + 300
        print("Current Lucky Numbers Prize: " , luckyNumbers)
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
def LuckyOne():
    print("**************************")
    print("Welcome to Lucky One!")
    print("Choose numbers between 1 & 1")
    print("----------------------------")
    print("--- Enter your number ---")
    onePut = int(input("Enter: "))

    if onePut == 1:
        time.sleep(1)
        print("Your number: " , onePut)
        print("Winning number: ", 1)
        time.sleep(1)
        print("Wow!!! you won!")
        time.sleep(1)
        print("Congratulations!")
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")
            sys.exit()
    else:
        time.sleep(1)
        print("Your number: " , onePut)
        print("Winning number: ", 1)
        time.sleep(1)
        print("awww ... better luck next time dude! ")
        time.sleep(1)
        choose = input("Do you want to play again? [y] Yes [n] No: ")
        if choose == "y":
            mainLotto()
        else:
            print("Okay. Thanks for playing! see you next time.")

def mainLotto():
    lotto_user = []
    first = []
    second = []
    third = []
    luckynums = []
    
    count = 0
    int(count)
    checker = False
    bool (checker)

    for i in range (0,6):
        number = random.randint(1,42)
      
        while number in first:
            number = random.randint(1,42)
      
        first.append(number)

    for j in range(0,6):
        secondnumber = random.randint(1,45)

        while secondnumber in second:
            secondnumber = random.randint(1, 45)
        second.append(secondnumber)

    for k in range(0,6):
        thirdnumber = random.randint(1,49)

        while thirdnumber in third:
            thirdnumber = random.randint(1,49)

        third.append(thirdnumber)

    for l in range(0,3):
        fourthnumber = random.randint(1,10)

        while fourthnumber in luckynums:
            fourthnumber = random.randint(1,10)

        luckynums.append(fourthnumber)

    
    today = date.today()
    d1 = today.strftime("%d %m %Y")

    time.sleep(1)
    potMoney()
    global lottoMoney
    global megaLottoMoney
    global superLottoMoney
    global luckyNumbers
    
    print("----------------------------")
    print("*** Welcome to IT-Lotto! ***")
    print("----------------------------")
    print("Yesterday's Winning numbers: \n In 6/42: ", first, " Prize: ", lottoMoney)
    print(" In 6/45: ", second, " Prize: ", megaLottoMoney)
    print(" In 6/49: ", third, " Prize: ", superLottoMoney)
    print(" Lucky numbers: ", luckynums, " Prize: ", luckyNumbers)
    print("----------------------------")
    print("Today's date: ", d1)
    print("----------------------------")
    
    time.sleep(1)
    while True:
        print("SELECT PLAYING MODE:")
        print("1 - 6/42 Lotto")
        print("2 - 6/45 Mega Lotto")
        print("3 - 6/49 Super Lotto")
        print("4 - Lucky 3 Numbers!")
        print("5 - Lucky 1")
        choose = int(input("Choose: "))
        print("----------------------------")

        if choose == 1:
            lotto()
        elif choose == 2:
            megalotto()
        elif choose == 3:
            superlotto()
        elif choose == 4:
            luckythree()
        elif choose == 5:
            LuckyOne()

mainLotto()

