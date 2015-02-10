__author__ = 'quicksand77'
import datetime
import time
import random
class RandTemp:
    def __init__(self):
        self.month1 = int(datetime.datetime.now().strftime(("%m")))
        self.day1 = int(datetime.datetime.now().strftime(("%d")))
        self.hour1 = int(datetime.datetime.now().strftime(("%H")))
        self.minute1 = int(datetime.datetime.now().strftime(("%M")))
        self.count = 1
        self.limit = 100
        self.server = "balrog"
        self.config()
    def loop(self):
        while self.count <= self.limit:
            print(self.server+","+str(self.month1)+"/"+str(self.day1)+","+str(self.hour1)+":"+str(self.minute1)+","+str(random.randint(60,100)))
            self.minute1 += 1
            if self.minute1 == 61:
                self.minute1 -= 61
                self.hour1 += 1
            if self.hour1 == 25:
                self.hour1 -= 25
                self.day1 += 1
            ### will need extra work to configure day limit for month
            # if self.day1 == 30:
            #     self.day1 -= 29
            #     self.month1 += 1
            # if self.month1 == 13:
            #     self.month -= 12
            ###
            self.count += 1
        choice = input('"q" to exit, "rr" to startover')
        if choice == "rerun":
            self.config()
    def config(self):
        print("Server: "+self.server)
        print("Loop count: "+str(self.limit))
        input1 = input('"o" for options, "r" to start loop, "q" to exit.\n')
        if input1 == "o":
            self.options()
        elif input1 == "r":
            self.loop()
        elif input1 == "q":
            print()
        else:
            print("invalid command")
            self.config()
    def options(self):
        print('To change server name, enter a string.')
        option = input('To change number of entries, enter a positive integer.\n"q" to go back\n')
        try:
            option = int(option)
        except:
            str(option)
        if option == "q":
            self.config()
        elif type(option) == int:
            self.limit = option
            self.config()
        else:
            self.server = option
            self.config()
    def write(self):
        asdf="111"
RandTemp()