import smtplib
import csv
import datetime
from datetime import datetime as dt
import os
from tkinter import *
flag = True

def writeToLog(now):
    with open('C:\\Users\\rohit\\Desktop\\Code\\Day-Planner\\log.txt', 'a') as log:
        log.write('email sent at '+ str(now))

def checkTime():
    global flag, backendroot
    a = None
    with open('C:\\Users\\rohit\\Desktop\\Code\\Day-Planner\\remindersData.csv','r') as file:
        #csv_reader = csv.reader(file) #these lines cause errors but are not necessary
        #next(csv_reader)
        for line in file:
            listLine = line.split(',')
            startTime = listLine[-2]
            date = listLine[0]
            print('line', line)
            now = dt.now().strftime('%d-%m-%y %H:%M')
            if startTime == "N\A":
                pass
            else:
                try: 
                    if dt.strptime(date + " " + startTime, '%Y-%m-%d %H:%M') == dt.strptime(now, '%d-%m-%y %H:%M'):
                        print('found upcoming event at', date + " "+startTime)
                        mail('', '', line)
                        writeToLog(now)
                        try:
                            next(line)
                        except:
                            flag = False
                            break
                except:
                    try:
                        next(line)
                    except:
                        print('ERROR')
                        flag = False
                        break

    backendroot.after(1000,checkTime) #repeat checking process after x milliseconds for continuous background checking                
 
def mail(From, to, body):
    gmail_usr = ""
    gmail_password = ""
  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_usr, gmail_password)
    server.sendmail(From, to ,body)
    server.close()
    print("EMAIL SENT!!!!")

#while flag == True:
if __name__ == '__main__': #run this code only if this script is ran directly not when imported
    backendroot = Tk() #define a tkinter window for using the after method
    backendroot.withdraw() #make this window invisible as it is blank
    checkTime() #run checktime function
    backendroot.mainloop() #make window 'display' but is invisible

