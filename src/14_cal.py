"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
import re


def cal(input=1):

    if(input == 1):
        x = datetime.now().month
        print(x)
    elif(input):
        array = input.split(" ")
        print(array)
        if(len(array) == 2):
            c = calendar.TextCalendar()
            str = c.formatmonth(datetime.now().year, int(array[1]))
            print(str)
        elif(len(array) == 3):
            c = calendar.TextCalendar()
            str = c.formatmonth(int(array[2]), int(array[1]), 0, 0)
            print(str)
        elif(len(array) > 3):
            print('out of bounds')


cal('14_cal.py 1 1')
