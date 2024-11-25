import subprocess
import focustui
import time

def focus():

    print("\nZen >> Hello user, welcome to your daily Zen practice!")
    print('Zen >> We are going to another meditation session :)')

    answer = int(input("Zen >> Enter '1' to proceed: "))

    if answer == 1:
        print("\nZen >> Initializing meditation clock in 3s")
        time.sleep(3)
        subprocess.run(["focustui"])
    else:
        time.sleep(1)
        print('\nZen >> I am deeply sorry to see you go traveller,')
        print('Zen >> Farewell young adventurer')