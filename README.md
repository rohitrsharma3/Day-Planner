# Day-Planner

A simple desktop app nade with python and tkinter library to manage tasks. You can register new reminds/events, define their date/duration and recieve reminder e-mails for the respective tasks. 

To Create a Reminder-
You can choose among all the days of the ongoing month and can create multiple reminders, classified as : Reminders and Events, collectibly refereed to as an 'Entry'. Each entry can have a span of operation such as 'All-Day' or 'Limited'. For Limited time reminders users need to specify the start and the end time of the action (in 24H format). Entries can be made for any of th allowed dates from the same window. Once an entry is submitted, it is exported to a CSV file named, remindersData.csv, in the root folder. You can send yourself an email consisting of a list of all the entries made through the 'Send mail' button at the bottom of the window.

To send emails- 

You need to specify your Gmail username and password in the 'mail()' function wihtin backend.py, eaach of these details are to be passed as a string. You then need to run the backend.py file, it refreshes every ! minute, scans for due reminders and sends them the minute they are due. Whenver an email is sent, the script updates log.txt with the info.

Event Contdown -
The main window features a countdown to upcoming calender events (if any). The list of the calender events can be updated by appending to the calenderData.csv file.

