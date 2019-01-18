
## About
Program to check if two dates fall on same day in a given range of
years. 

- Two dates of an year, will always fall on same day as long as the following conditions holds true:
  1. The months of these dates lie either in range of [March, Dec] or [Jan,Feb];
     if month is 'Feb' date should be on or before 28th
  2. As long as the difference of two dates is a multiple of '7'
     Eg: May 15th and Sep 18th

- We can calculate the all the pairs of dates which have same day irrespective if the year is a leap year or not
  by calculating the multiples of '7'.

- To use the program do: <br>
  python get_day.py

- Be sure to change the 'start_year', 'end_year', 'comp_date_1', 'comp_date_2' variables according to your need
