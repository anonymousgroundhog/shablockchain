from tkinter import *
import tkinter as tk # Python 3 import
# import Tkinter as tk # Python 2 import
from random import *
import hashlib
import uuid
import datetime
import time
import csv
from itertools import repeat
import sha3
from pylab import *
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import os
#GLOBAL VARIABLES
global tempcounter
tempcounter = []

global RunningTimes
RunningTimes = []

global RunningAlg
RunningAlg = []
global LoopIter
LoopIter = []

global salt
global counterGraphTimes
global updatedCounterGraphTimes
global counterGraphTimes
#global temp

#global TotalHours
#global TotalMinutes
#global TotalSeconds

def SentenceLength():
   sentencesize = len(my_entry.get())
   print("Sentence Length is: " + str(sentencesize))
   my_lablesetnencesize = tk.Label(root, text = "Current Sentence Size is: " + str(sentencesize))
   my_lablesetnencesize.grid(row = 17, column = 1)
def refreshVariables():
        del tempcounter[:]
        del RunningTimes[:]
        del LoopIter[:]
        del temp[:]
        counterGraphTimes = 0
        
def validateIsInteger(value):
        try:
            if value:
                v = int(value)
            return value
        except ValueError:
            return None

def RunningTimeToCSV():
        file_name = str(my_entry7.get() + "Time")
        print("Total running time of current attempts being saved to " + str(file_name))
        counter = 0
        sentencesize = len(my_entry.get())        
        if (file_name != "Time" and os.path.isfile(file_name)):
                download_dir = file_name +".csv"#where you want the file to be downloaded to
                csv = open(download_dir, "a") 
                #columnTitleRow = "Attempt Number, Running Time, Normalized Time, Algorithm, Sentence Size\n"
                #csv.write(columnTitleRow)
        else:
                download_dir = file_name +".csv"#where you want the file to be downloaded to
                csv = open(download_dir, "a") 
                columnTitleRow = "Attempt Number, Running Time, Normalized Time, Algorithm, Sentence Size\n"
                csv.write(columnTitleRow)
                
                for x in RunningTimes:
                        counter = counter + 1
                        
                        row = str(counter) + "," + str(x) + "," + str(x[:-8]) + "," + str(RunningAlg[counter-1]) + "," + str(sentencesize) + "\n"
                        csv.write(row)
                    
def AttemptsToCSV():
        file_name = str(my_entry7.get() + "Attempts")
        print("RUNNING AttemptsToCSV" + str(temp) + " being saved to " + str(file_name))
        counter = 0
                
        if (file_name != "Attempts"):
                download_dir = file_name +".csv"#where you want the file to be downloaded to
                csv = open(download_dir, "a") 
                columnTitleRow = "Attempt Number, Attempts\n"
                csv.write(columnTitleRow)
                for x in temp:
                        counter = counter + 1
                        row = str(counter) + "," + str(x) + "\n"
                        csv.write(row)
        
        
def graphTimes():
        
        counterGraphTimes = 0
        updatedCounterGraphTimes = []
        Counter = []
        #CLEAR ALL DATA IF LOOP NUMBER CHANGES
        
        LoopIter.append(my_entry6.get())
        LoopLastVal = len(LoopIter)-1
       
        for x in RunningTimes:
                counterGraphTimes=counterGraphTimes + 1
                Counter.append(counterGraphTimes)
                #print("TIME for attempt " + str(counterGraphTimes) + " graphTimes Func is: " + str(x))
                updatedCounterGraphTimes.append(x)
       
        plt.xticks(np.arange(1, len(updatedCounterGraphTimes)+1, 1.0))
        
        if (len(updatedCounterGraphTimes) == 1):
            plot(Counter, updatedCounterGraphTimes, "ro")
        else:
            plot(Counter, updatedCounterGraphTimes)

        if (LoopIter[LoopLastVal] != LoopIter[LoopLastVal-1]):
                        #ax = plt.gca
                ax = plt.axes()
                plt.clf()
                        #plot(Counter, updatedCounterGraphTimes)
                plot(1,updatedCounterGraphTimes[len(LoopIter)-1], "ro")
                xint = range(0,1)
                matplotlib.pyplot.xticks(xint)
                Counter[:] = []
                RunningTimes[:] = []
        elif (LoopIter[LoopLastVal] == LoopIter[LoopLastVal-1]):
            plot(Counter, updatedCounterGraphTimes)
          
        #print("Prev Val is: " + str(LoopIter[LoopLastVal]) + "Cur Val is: " + str(LoopIter[LoopLastVal-1]))
        print("LoopIter is: " + str(LoopIter))        
        #plt.xticks((1, len(updatedCounterGraphTimes)))   
        plt.xlabel('Run Number')
        plt.ylabel('Times in (Hours:Minutes:Seconds:Microseconds')
        plt.title('Time Taken to Run')
        plt.grid(True)
        show()
        
def hash_text(text, nonce):
        #global salt
        salt = uuid.uuid4().hex

        if (SHA.get() == 2):
                #print("SHA3_256 is picked")
                #RunningAlg.append("SHA3 256")
                return hashlib.sha3_256( text.encode()+nonce.encode()).hexdigest()
        elif (SHA.get() == 3):
                #print("SHA2_224 is picked")
                #RunningAlg.append("SHA2 224")
                return hashlib.sha224( text.encode()+nonce.encode()).hexdigest()
        elif (SHA.get() == 4):
                #print("SHA2_256 is picked")
                #RunningAlg.append("SHA2 256")
                return hashlib.sha256( text.encode()+nonce.encode()).hexdigest()
        elif (SHA.get() == 6):
                #RunningAlg.append("SHA 512")
                return hashlib.sha512( text.encode()+nonce.encode()).hexdigest()
        else:
                #print("SHA3_224 is picked")
                #RunningAlg.append("SHA3 224")
                return hashlib.sha3_224( text.encode()+nonce.encode()).hexdigest()      

def isfloat(value):
	try:
		float(value)
		return True
	except:
		return False
def graph(data):
    plt.close("all") #TRY CLOSING ALL OPEN GRAPHS
    dataCount = []
    count = 0
    for x in data:
        count = count + 1
        dataCount.append(count)

    #ERASE GRAPH IF RUN PREVIOUSLY
    if (len(tempcounter) <= 0):
            ax = plt.gca() #FORMAT Y AXIS
            ax.clear()
    #END       
    ax = plt.gca() #FORMAT Y AXIS
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) #FORMAT Y AXIS

    #CHANGE X RANGE TICKS DEPENDING ON ITERATIONS
    Iterations = my_entry6.get()
    IntIterations = int(Iterations)
    if (IntIterations >= 25):
       plt.xticks(np.arange(min(dataCount), max(dataCount)+10, 11.0)) #TESTING RIGHT NOW
       for x in ax.get_yticklabels( ):
               x.set_fontsize( 'small' )
    else:
       plt.xticks(np.arange(min(dataCount), max(dataCount)+1, 1.0))

    #END
    #IF NUM ZEROS IS GREATER THAN 2 EDIT THE GRAPH Y AXIS
    NumZero = my_entry4.get()
    NumZero = int(NumZero)
    MaxYVal = max(data)
    MinYVal = max(data)/3
    Interval = (MaxYVal - 10)/10
    #print("MaxYVal is: " + str(MaxYVal))
    if (NumZero >= 1 and MaxYVal >= 5000):
            #ax.set_yticks((MinYVal, MaxYVal))
            ax.set_yticks((min(data), MaxYVal))
            

    xlabel('Simulation Number')
    ylabel('Number of Attempts')
    if (SHA.get() == 2):
                title('Frequency of Attempts for SHA3 256')
    elif (SHA.get() == 3):
                title('Frequency of Attempts for SHA2 224')
                
    elif (SHA.get() == 4):
                title('Frequency of Attempts for SHA2 256')
                
    else:
                title('Frequency of Attempts for SHA3 224')
                
    grid(True)
    #PLOT ONLY IF 1 IS CHOSEN FOR LOOP
    NumIter = my_entry6.get()
    if (NumIter == "1"):
            plot(dataCount, data, "ro")
            plt.show()
    else:
           plt.plot(dataCount, data)
           plt.show()
    #END
    
def Barplot():
    #SHA = SHA.get()
    
    barplotObjects = []
    CounterBarPlot = []
    for x in range(1, 7):
        barplotObjects.append(16**x)
        CounterBarPlot.append(x)    
    
    plt.xticks(np.arange(min(CounterBarPlot), max(CounterBarPlot)+1, 1.0))    
    plt.xlabel('16 to the power of')
    plt.ylabel('Number of Attempts')
    plt.title('Frequency of Attempts')
    plt.grid(True)
    plt.plot(CounterBarPlot, barplotObjects)
    ax = plt.gca() #FORMAT Y AXIS
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))) #FORMAT Y AXIS
    plt.show() 
    
def my_function():
    NumZeroAcc = my_entry4.get()
    NumLoopAcc = my_entry6.get()
    IsIntNumZeroAcc = validateIsInteger(NumZeroAcc)
    IsIntNumLoopAcc = validateIsInteger(NumLoopAcc)
    print("NumZero is: " + str(IsIntNumZeroAcc) + " NumLoop is: " + str(IsIntNumLoopAcc) + "Sentence is: " + str(my_entry.get()))
    if (NumZeroAcc != "" and IsIntNumZeroAcc != "None" and NumLoopAcc != "" and IsIntNumLoopAcc != "None" and my_entry.get() != ""):
            current_loop = my_entry6.get()
            file_name = my_entry7.get()
            loopiter = list(range(int(current_loop)))
            if (file_name != ""):
                download_dir = file_name +".csv"#where you want the file to be downloaded to
                csv = open(download_dir, "a") 
                columnTitleRow = "Hash, Time(H:M:S:microseconds), Average Number of Attempts\n"
                csv.write(columnTitleRow)
            
            #nonceInc = randint(1,10000000000)
            nonceInc = randint(1,1000000000)
            
            
            counter = 0;
            global temp;
            temp = [];
            Time = datetime.datetime.now().time() #NEED TO TRACK TIME HERE
            Time = str(Time)
            my_labelTime = tk.Label(root, text = str('CURRENT Start Time: ' + Time))
            my_labelTime.grid(row = 9, column = 1)
            for i in loopiter:
                       
                    my_label14 = tk.Label(root, text = str('CURRENT loop: ' + current_loop))
                    my_label14.grid(row = 15, column = 1)
                    ListStringZeros = []  
                    current_Sentence = my_entry.get()
                    current_Nonce = nonceInc
                    current_Nonce = int(current_Nonce)
                    current_NumZer = my_entry4.get()

                    #do stuff with USER SENTENCE    
                    my_label2 = tk.Label(root, text = str('CURRENT SENTNECE: ' + current_Sentence))
                    my_label2.grid(row = 5, column = 1)
                    #DO STUFF WITH NONCE
                    current_Nonce = str(current_Nonce)
                    my_labelNonce = tk.Label(root, text = str('Starting Nonce Value: ' +current_Nonce))
                    my_labelNonce.grid(row = 6, column = 1)
                    #DO STUFF WITH ZEROS
                    numberzeros = int(current_NumZer)
                    for i in range(0,numberzeros):
                        ListStringZeros += "0" #CREATING STRING OF ZEROS TO MATCH
                    StringZeros = ''.join(ListStringZeros)
                    my_labelZero = tk.Label(root, text = 'Number of Zeros String: ' +StringZeros)
                    my_labelZero.grid(row = 7, column = 1)      

                    nonce = str(current_Nonce)
                    hashed_input = hash_text(current_Sentence, nonce)
                    #MATCH NUMBER OF ZEROS TO VAL
                    tempHash = hashed_input[0:numberzeros] #USE THIS TO GET NUMBER ZEROS TO MATCH
                    counter = 0;
                   

                    #WHILE LOOP THROUGH POSSIBLE HASH VALUES
                    while tempHash != StringZeros:
                        nonce = str(nonce) 	
                        hashed_input = hash_text(current_Sentence, nonce)
                        tempHash = hashed_input[0:numberzeros]
                        firstval = [int(s) for s in hashed_input[0] if s.isdigit()]
                        print ("Hash Val: ", hashed_input)
                        #print ("First Val: ", firstval)
                        counter = counter + 1
                        nonce = int(nonce)
                        nonce = nonce + nonceInc
                        
                    Accum2 = sum(temp);
                    temp.append(counter);
                    Accum = sum(i for i in temp);
                    Sum = int(Accum);
                    Average = Sum / int(current_loop);
                    counter = Average;            
                    #print(temp); #USED TO SHOW NUMBER OF ATTEMPTS INCREASES            
                    #CHANGE END TEST
                    counter = "{:,}".format(counter)
                    counter = str(counter)
                    
                    my_labelCounter = tk.Label(root, text = str("Average NUMBER OF ATTEMPTS: " + counter ))
                    
                    my_labelCounter.grid(row = 12, column = 1)
                    pow1 = math.pow(16, float(current_NumZer))
                    pow1 = "{:,}".format(pow1)
                    pow1 = pow1.strip('.0')
                    pow1 = str(pow1)
                    my_labelCounterBase = tk.Label(root, text = str("16 to the base " + str(current_NumZer) + "= " + pow1))
                    my_labelCounterBase.grid(row = 12, column = 2)
                    my_labelSum = tk.Label(root, text = str("Total Number of Attempts: " + str(sum(temp))))
                    my_labelSum.grid(row = 12, column = 3)
                    
                    #DISPLAY HASH VALUE OF MATCH CASE
                    my_lableHash = tk.Label(root, text = "HASH VALUE MATCH CASE: " + str(hashed_input))
                    my_lableHash.grid(row = 11, column = 1)          
                    #INCREMENT NONCE VALUE BY RANDOM NUMBER
                    nonceInc = nonceInc+1
            #END TIME HERE

            EndTime = datetime.datetime.now().time() #NEED TO TRACK TIME ENDING HERE
            EndTime = str(EndTime)
            my_labelTimeEnd = tk.Label(root, text = str('CURRENT End Time: ' + EndTime))
            my_labelTimeEnd.grid(row = 10, column = 1)
            
            #CLACULATE TIME AND DISPLAY AT END
                    
            #CONDITIONALS FOR GRABBING HOURS MINUTES SECOND AND MICROSECONDS
            global TotalHours
            global TotalMinutes
            global TotalSeconds
            HoursEndTime = int(EndTime[0:2])
            HoursTime = int(Time[0:2])
            if HoursEndTime > HoursTime:
               TotalHours = HoursEndTime - HoursTime
            else:
               TotalHours = HoursTime - HoursEndTime
            TotalHours = str(TotalHours)

            MinutesEndTime = int(EndTime[3:5])
            MinutesTime = int(Time[3:5])
            if MinutesEndTime > MinutesTime:
               TotalMinutes = MinutesEndTime - MinutesTime
            else:
               TotalMinutes = MinutesTime - MinutesEndTime

            TotalMinutes = str(TotalMinutes)            
            SecondsEndTime = int(EndTime[6:8])
            SecondsTime = int(Time[6:8])

            if SecondsEndTime > SecondsTime:
               TotalSeconds = SecondsEndTime - SecondsTime
            else:
               TotalSeconds = SecondsTime - SecondsEndTime
            TotalSeconds = str(TotalSeconds)

            MicrosecondEndTime = int(EndTime[9:])
            MicrosecondTime = int(Time[9:])

            if MicrosecondEndTime > MicrosecondTime:
               TotalMicroseconds = MicrosecondEndTime - MicrosecondTime
            else:
               TotalMicroseconds = MicrosecondTime - MicrosecondEndTime
            TotalMicroSeconds = str(TotalMicroseconds)

            #DISPLAY TIME TAKEN
            my_lableTime = tk.Label(root, text = "Time Taken (H:M:S:microseconds): " + TotalHours + " : " + TotalMinutes + " : " + TotalSeconds + " : " + TotalMicroSeconds)
            my_lableTime.grid(row = 13, column = 1)
            timetaken = str(TotalHours + " : " + TotalMinutes + " : " + TotalSeconds + " : " + TotalMicroSeconds) # NEED DEFINE TIMETAKEN HERE
            if (file_name != ""):
                #WRITE TO CSV FILE FINDINGS, HASH VAL, Time           
                #timetaken = str(TotalHours + " : " + TotalMinutes + " : " + TotalSeconds + " : " + TotalMicroSeconds)
                row = hashed_input + "," + timetaken + "," + counter + "\n"
                csv.write(row)
            
            RunningTimes.append(timetaken)#USED FOR GRABBING EACH RUNNING TIME ONCE SUBMIT BUTTON IS PRESSED, NOTE APPENDING IS BACKWARDS OF WHAT YOU WOULD THINK!!!!
            
            if (SHA.get() == 2):
                #print("SHA3_256 is picked")
                RunningAlg.append("SHA3 256")
                
            elif (SHA.get() == 3):
                    #print("SHA2_224 is picked")
                    RunningAlg.append("SHA2 224")
            elif (SHA.get() == 4):
                    #print("SHA2_256 is picked")
                    RunningAlg.append("SHA2 256")
                    
            elif (SHA.get() == 6):
                    RunningAlg.append("SHA 512")
                    
            else:
                    #print("SHA3_224 is picked")
                    RunningAlg.append("SHA3 224")
                  
            print("RunningTimes were:" + str(RunningTimes))#TESTING ONLY
            print("RunningAlg were:" + str(RunningAlg))#TESTING ONLY
            print("FINISHED RUNNING PROGRAM")
            my_buttonGraphTimes['state'] = 'normal'
            my_buttonAttemptsCSV['state'] = 'normal'
            my_buttonRefresh['state'] = 'normal'
            my_buttonRunTime['state'] = 'normal'
            graph(temp) #GRAPH ONCE COMPLETE LOOP
    
    
#----------------------END FUNCTION----------------------------------------------------------------------



#START NEW CODE
root = tk.Tk("BLOCK HASHING")
root.title("Blockchain Hashing")    
#---------------------------------USER INPUT AREA---------------------------------------------------------
#SENTENCE    
my_label = tk.Label(root, text = "Sentence: ")
my_label.config(font=("Courier", 10))
my_label.grid(row = 0, column = 0)
my_entry = tk.Entry(root)
my_entry.grid(row = 0, column = 1)


#NUMBER OF ZEROS
my_label4 = tk.Label(root, text = "Number of Zeros to account for: ")
my_label4.config(font=("Courier", 10))
my_label4.grid(row = 1, column = 0)
my_entry4 = tk.Entry(root)
my_entry4.grid(row = 1, column = 1)


#NUMBER OF TIMES TO RUN LOOP
my_label6 = tk.Label(root, text = "How many times to run test: ")
my_label6.config(font=("Courier", 10))
my_label6.grid(row = 0, column = 2)
my_entry6 = tk.Entry(root)
my_entry6.grid(row = 0, column = 3)

#NAME THE CSV FILE
#NUMBER OF TIMES TO RUN LOOP
my_label7 = tk.Label(root, text = "Name of CSV File: ")
my_label7.config(font=("Courier", 10))
my_label7.grid(row = 1, column = 2)
my_entry7 = tk.Entry(root)
my_entry7.grid(row = 1, column = 3)

#PICK HASH TYPE TO USE
my_labelHash = tk.Label(root, text = 'Pick Hash To Use: ')
my_labelHash.config(font=("Courier", 10))
my_labelHash.grid(row = 3, column = 1)
#SHA3 = tk.IntVar()

SHA = IntVar()
SHA.set(1)
tk.Radiobutton(root, text="SHA3 224 bit", font = 10, padx = 20, variable=SHA, value=1).grid(row=3, column = 2)
tk.Radiobutton(root, text="SHA3 256 bit", font = 10, padx = 20, variable=SHA, value=2).grid(row=3, column = 3)
tk.Radiobutton(root, text="SHA2 224 bit", font = 10, padx = 20, variable=SHA, value=3).grid(row=3, column = 4)
tk.Radiobutton(root, text="SHA2 256 bit", font = 10, padx = 20, variable=SHA, value=4).grid(row=3, column = 5)
tk.Radiobutton(root, text="SHA 512", font = 10, padx = 20, variable=SHA, value=5).grid(row=3, column = 6)

#SUBMIT BUTTON
my_button = tk.Button(root, text = "Submit", font = 20, command = my_function)
my_button.grid(row = 4, column = 2)

my_buttonGraphBarPlot = tk.Button(root, text = "Show Barplot", font = 10, command = Barplot)
my_buttonGraphBarPlot.grid(row = 4, column = 3)

my_buttonGraphTimes = tk.Button(root, text = "Show Running Time", font = 10, state=DISABLED, command = graphTimes)
my_buttonGraphTimes.grid(row = 4, column = 4)

my_buttonAttemptsCSV = tk.Button(root, text = "Save Attempts to CSV", font = 10, state=DISABLED, command = AttemptsToCSV)
my_buttonAttemptsCSV.grid(row = 4, column = 5)

my_buttonRefresh = tk.Button(root, text = "Refresh All Data", font = 10, state=DISABLED, command = refreshVariables)
my_buttonRefresh.grid(row = 4, column = 7)

my_buttonRunTime = tk.Button(root, text = "Save Running Times", font = 10, state=DISABLED, command = RunningTimeToCSV)
my_buttonRunTime.grid(row = 4, column = 6)
my_buttonSentenceLength = tk.Button(root, text = "Get Sentence Length", font = 10, command = SentenceLength)
my_buttonSentenceLength.grid(row = 4, column = 6)
root.mainloop()
#Barplot()
