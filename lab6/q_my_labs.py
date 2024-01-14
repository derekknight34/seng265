#!/usr/bin/env python3

import datetime

def every_lab(foo):
    print("This is outrageous! Unfair!")
    return None

def main():
    """
    Create a datetime object for today's date
    """
    todays_date = datetime.datetime(2023, 3, 3)
    date_list = every_lab(todays_date)
    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """
    print(date_list)

def every_lab(todays_date):
    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    lab_date = todays_date
    last_date = datetime.datetime(2023, 4, 7)
    date_list = []
    while lab_date <= last_date:
        date_list.append(lab_date)
        lab_date = lab_date + datetime.timedelta(days=7)

    for index in range(len(date_list)):
        date_list[index] = date_list[index].strftime("%a, %d %b %y")
    return date_list


if __name__ == "__main__":
    main()
