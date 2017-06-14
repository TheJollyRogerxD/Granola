from time import sleep
import webbrowser
import urllib.request
import requests
from random import randint
from time import sleep

def intro():
    print("1. Download Accounts")
    print("2. Github Page")
    print("4. Josh'o Matic")
    print("3. About")
intro()
answer = input("What would you like to do?")
if answer == "1":
    print("Starting download")
    urllib.request.urlretrieve("http://www82.zippyshare.com/v/W4FqqBGt/file.html", "Netflix.txt")
    print("Completed")

elif answer == "2":
    webbrowser.open("https://github.com/TheJollyRogerxD")
elif answer == "3":
    print("Coded by The Jolly Roger")
    print("For Educational purposes only")
elif answer == "4":
    print("Starting Josh'O Matic")
    url = 'http://www.matthewlush.com/VotingSystem/submitVote.php'
    vote = 0

    while True:
        vote += 1
        fakeip = str(randint(90, 180)) + "." + str(randint(90, 180)) + "." + str(randint(90, 180)) + "." + str(
            randint(90, 180))
        postVars = {"postperson": 7, "postip": fakeip}

        kek = requests.post(url, params=postVars)
        if kek.text == "Thank you for voting!":
            print("Josh is " + str(vote) + " " + "votes closer to meeting his lover")
        sleepTime = randint(5, 15)
        print("Waiting for " + str(sleepTime) + " " + "seconds")
        sleep(sleepTime)

else:
    print("Unknown error. you can find help on my github page.")
    sleep(3)
    webbrowser.open("https://github.com/TheJollyRogerxD")
