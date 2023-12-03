from datetime import datetime
import time
import os
import msvcrt


os.system("cls")


def is_number(input):
    try: 
        return int(input)
    except:
        print("Make sure you enter a number")


def start_timer(duration): 
    starting_time = time.perf_counter()

    while True: 
        current_time = time.perf_counter()
        elapsed_time = int(current_time - starting_time)

        print(elapsed_time)
        if elapsed_time >= duration: 
            break

        time.sleep(1)
        os.system("cls")
    
    return print("TIMES OUT !!!")


'''
# Gör ett program som skriver ut dagens datum och tid
print(datetime.now())
'''


'''
# Prova olika sätt att skriva ut tid/datum
print(datetime.now().strftime("%y %b, %d"))
'''


'''
# Gör så klockan uppdateras automatiskt
while True:
    print(datetime.now().strftime("%X"))
    time.sleep(1)
    os.system("cls")

    if msvcrt.getwch():
        break
'''


'''
# Gör ett tidtagarur
starting_time = time.perf_counter()
def format_timer(elipsed_time): # dvin v while loop
    seconds = int(elipsed_time) % 60
    minutes = int(elipsed_time / 60) % 60
    hours = int(elipsed_time / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
'''


'''
# Skriv ett program som frågar användaren efter ett specifikt datum (månad, dag # och år) och sedan beräknar antalet dagar mellan det datumet och dagens datum.s
while True:
    current_time = time.perf_counter() # time.time()
    elapsed_time = current_time - starting_time

    format_timer(elapsed_time)

    time.sleep(1)
    os.system("cls")

current_date = datetime.date.today()
'''


'''
while True:
    year = is_number(input("Enter a year: "))
    month = is_number(input("Enter a month: "))
    day = is_number(input("Enter a day: "))

    try: 
        custom_date = datetime.date(year, month, day)
        print(f"Number of days between your date and today's: {(current_date - custom_date).days} days")
    except:
        print("Some of the date numbers were out of range.")
'''


'''
# Gör en larmklocka eller timer där man kan ställa in tid för nedräkning. Något ska hända när tiden är ute
# MAIN
while True: 
    duration = is_number(input("Enter the duration of the timer as a number: "))

    # the duration variable will be set to False if it is not a number.
    if not duration: 
        print("Make sure you enter a number !")
        continue

    os.system("cls")
    print("Timer started !")
    start_timer(duration)
'''  

