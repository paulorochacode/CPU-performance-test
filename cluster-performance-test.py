import time
import threading

numberOfprints = 999999

testrunning = True

def counter():
    counter = 0    
    while testrunning == True :
        counter = int(counter) + 1
        time.sleep(1)
    print("#############################################################")
    print(str(counter) + " seconds")
    print("#############################################################")

threading.Thread(target=counter).start()

def processamentVolume():
    
    counter2 = 0
    while counter2 < numberOfprints :
        counter2 = counter2 + 1
        print(counter2)
    global testrunning
    testrunning = False

threading.Thread(target=processamentVolume).start()