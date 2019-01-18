

"""
- Two dates of an year, will always fall on same day as long as the following conditions holds true:
    1. The months of these dates lie either in range of [March, Dec] or [Jan,Feb]; 
       if month is 'Feb' date should be on or before 28th
    2. As long as the difference of two dates is a multiple of '7' 
   Eg: May 15th and Sep 18th 

- We can calculate the all the pairs of dates which have same day irrespective if the year is a leap year or not
   by calculating the multiples of '7'. 
"""

import datetime
from datetime import date

comp_date_1 = "05-15"
comp_date_2 = "09-18"


def diff_of_dates(date1, date2):
    return abs(date2-date1).days


def get_new_date(date, no_of_days):
    """
    calculates a date by dates to a given date
    """
    return date + datetime.timedelta(days=no_of_days)


def compare_days(start, end):
    """
    compares if the days in dates formed 
    using comp_date_1/comp_date_2 and start/end years
    """
    global comp_date_1, comp_date_2
    flag = 1 
    month_1, date_1 = (int(x) for x in comp_date_1.split('-'))
    month_2, date_2 = (int(x) for x in comp_date_2.split('-'))

    for year in range(start, end+1):   
        d_1 = date(year, month_1, date_1)
        d_2 = date(year, month_2, date_2)
        diff_dates = diff_of_dates(d_1,d_2)
        day_1 = datetime.date(year, month_1, date_1).weekday()
        day_2 = datetime.date(year, month_2, date_2).weekday()
        
        if day_1 != day_2:
           flag = 0 
           print("the days are not same in the year : ", year)
        """
        else:
            print("days are same; year : {}  day_1 : {} day_2 : {} ".format(year, day_1, day_2))
        """
    if flag == 0:
        return False
    else:
        return True


def multiples_of_7(num):
    """
    returns the multiples of '7' from '1' to a range of 'num' 
    """
    res = []
    for i in range(1,num+1):
        if i%7 == 0:
           res.append(i)
    return res
        
     
if __name__ == "__main__":
   start_year = 1980
   end_year   = 2000

   result = compare_days(start_year, end_year)
   if result == True:
       print("the dates have same days in every year from {} to {}".format(start_year, end_year))

