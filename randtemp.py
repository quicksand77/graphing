__author__ = 'quicksand77'
#python 2.7.9
import datetime
import time
import random
import os
import platform
class RandTemp:
    def __init__(self):
        self.makePath()
        self.month1 = int(datetime.datetime.now().strftime(("%m")))
        self.day1 = int(datetime.datetime.now().strftime(("%d")))
        self.hour1 = int(datetime.datetime.now().strftime(("%H")))
        self.minute1 = int(datetime.datetime.now().strftime(("%M")))
        self.count = 1
        self.limit = 20
        self.listOfStuff = []
        self.server = "balrog"
        self.config()
    def makePath(self):
        a = platform.system()
        if a == "Linux":
            self.isWindows = False
        elif a == "Windows":
            self.isWindows = True
        if self.isWindows:
            self.path = ".\\randtemp.txt"
        elif not self.isWindows:
            self.path = "./randtemp.txt"
        else:
            self.path = ".\\randtemp.txt"
    def loop(self):
        while self.count <= self.limit:
            # stuff = self.server+","+str(self.month1)+"/"+str(self.day1)+","+str(self.hour1)+":"+str(self.minute1)+","+str(random.randint(60,100))
            self.time1 = int(time.time())
            self.stuff = str(self.time1)+","+str(random.randint(60,100))
            time.sleep(2)
            print self.stuff
            self.listOfStuff.append(self.stuff)
            self.minute1 += 1
            if self.minute1 == 61:
                self.minute1 -= 61
                self.hour1 += 1
            if self.hour1 == 25:
                self.hour1 -= 25
                self.day1 += 1
            self.count += 1
        self.count == 1
        self.afterLoopConfig()
    def afterLoopConfig(self):
        choice = raw_input('"q" to quit, "w" to write, "wq" to write then quit, "v" to view, "b" to startover')
        if choice == "b":
            self.config()
        elif choice == "w":
            self.write()
            self.afterLoopConfig()
        elif choice == "wq":
            self.write()
            print "program end"
        elif choice == "q":
            print "program end"
        elif choice == "v":
            self.whatsinfile()
            self.afterLoopConfig()
    def config(self):
        print "Server: "+self.server
        print "Loop count: "+str(self.limit)
        input1 = raw_input('"o" for options, "r" to start loop, "v" to view file, "q" to exit.\n')
        if input1 == "o":
            self.options()
        elif input1 == "v":
            self.whatsinfile()
            self.config
        elif input1 == "r":
            self.loop()
        elif input1 == "q":
            a = ""
        else:
            print "invalid command"
            self.config()
    def options(self):
        print 'To change server name, enter a string.'
        option = raw_input('To change number of entries, enter a positive integer.\n"q" to go back\n')
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
        print "writing to file %s"%self.path
        with open(self.path,'w') as f:
            for thing in self.listOfStuff:
                f.write(str(thing)+"\n")
    def whatsinfile(self):
        try:
            with open(self.path,'r') as f:
                a = f.read()
                print a
        except:
            f = open(self.path,'w')
            f.close()
        self.config()