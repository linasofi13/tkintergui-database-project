import re
from datetime import datetime, date  # to have todays date
import calendar  # to check if year is leap
from tkinter import *
from tkinter import messagebox
import ast
import form_checker

birth_pattern = "[\d]{4}-[\d]{1,2}-[\d]{1,2}" # YYYY-MM-DD (valid format for DATE in mysql)

# deleting soon 
# pattern3 = "[\d]{1,2}\s(JAN|FEB|MAR|MAY|APR|JUN|JUL|AUG|SEPT|OCT|NOV|DEC)\s[\d]{4}"  # 10 OCT 2015
# pattern4 = "[\d]{1,2}\s(ENERO|FEBRERO|MARZO|ABRIL|MAYO|JUNIO|JULIO|AGOSTO|SEPTIEMBRE|OCTUBRE|NOVIEMBRE|DICIEMBRE)\s[\d]{4}"  # 10 OCTUBRE 2015

pattern_date = "[\d]{1,2}/[\d]{1,2}"
pattern_date2 = "[\d]{1,2}-[\d]{1,2}"

capital_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alph = "abcdefghijklmnopqrstuvwxyz"
special_chars_list = ['$', '@', '_', '*', '!', '¡', '-', '#']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

months = {"JAN": '01', "FEB": '02', "MAR": '03', "MAY": '04', "APR": '05', "JUN": '06', "JUL": '07', "AUG": '08', "SEPT": '09', "OCT": '10',
          "NOV": '11', "DEC": '12'}
spanish_months = {"ENERO": '01', "FEBRERO": '02', "MARZO": '03', "MAYO": '04', "ABRIL": '05', "JUNIO": '06', "JULIO": '07', "AGOSTO": '08',
                  "SEPTIEMBRE": '09', "OCTUBRE": '10', "NOVIEMBRE": '11', "DICIEMBRE": '12'}


def nameChecker(name): # only characters
    name = name.upper().replace(" ", "")
    if (len(name) == 0 or len(name) > 200) or containsSpecialSymbols(name): # VARCHAR(?????) # TODO
        return False
    else:
        return True
    
# 

def checkDigitValues(numericValue): # only numeric data
    numericValue = numericValue.upper().replace(" ", "")
    if numericValue.isnumeric():
        return True, "Given data is correct"
    else:
        return False, "Given data is incorret"
    


def usernameChecker(username): # not needed
    username = username.strip()
    if 8 <= len(username) < 16:
        return True
    else:
        return False

def getDayMonthYear(date_user):
    if re.search(birth_pattern, date_user):
        year, month, day = date_user.split('-')

    if day[0] == '0':
        day = day[1]

    if month[0] == '0':
        month = month[1]

    day = int(day)
    month = int(month)
    year = int(year)

    return day, month, year

def birthDateChecker(date_user): # date of birth of pet updated
    date_user = date_user.strip().upper()
    if re.search(birth_pattern, date_user):
        day, month, year = getDayMonthYear(date_user)
        if (32 > day > 0) and (13 > month > 0) and (2023 > year > 1950): # correct format
            today = date.today()
            result = today.year - year - ((today.month, today.day) < (month, day))
            return True
        else:
            return False
    else:
        return False


def tillYourBirthday(day, month, year):
    today = date.today()
    birthdate_day_year = date(today.year, month, day).timetuple().tm_yday
    todays_day_year = datetime.now().timetuple().tm_yday

    birthdate_day_year = int(birthdate_day_year)
    todays_day_year = int(todays_day_year)

    numberOfDays = birthdate_day_year - todays_day_year

    if (
    numberOfDays) > 0:  # if the difference is negative, your birthday has already passed, so we need to do the count of next years num of day
        return f"There are {numberOfDays} days left until your birthday"
    else:
        todaysYear = int(today.year)
        birthdate_day_year = date(todaysYear + 1, month, day).timetuple().tm_yday
        if calendar.isleap(todaysYear):  # if its leap it has 366 days
            tillYearIsOver = 366 - todays_day_year  # num of days till year is over
            days = birthdate_day_year + tillYearIsOver
            return f"There are {days} days left until your birthday"
        else:
            tillYearIsOver = 365 - todays_day_year  # normal year
            days = birthdate_day_year + tillYearIsOver
            return f"There are {days} days left until your birthday"


def containsCapitals(password): # not needed
    numberOfUppers = len(re.findall(r'[A-Z]', password))
    if numberOfUppers >= 1:
        return True
    else:
        return False


def containsLowerCase(password):
    numberOfLowers = len(re.findall(r'[a-z]', password))
    if numberOfLowers >= 1:
        return True
    else:
        return False


def containsNumbers(password):
    amount = 0
    for character in password:
        if character.isdigit():
            amount += 1
    if amount >= 1:
        return True
    else:
        return False


def containsSpecialSymbols(password):
    amount = 0
    for character in password:
        if character in special_chars_list:
            amount += 1
    if amount >= 1:
        return True
    else:
        return False


def containsWeirdSymbols(password):
    for char in password:
        if (char not in capital_alph) and (char not in small_alph) and (char not in special_chars_list) and (
                char not in numbers):
            return True
        else:
            return False


def checkEmail(email):
    email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
    email_pattern2 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)+\.(com)"
    if re.search(email_pattern, email) or re.search(email_pattern2, email):
        return True
    else:
        return False

def duplicate_frame(frame):
    new_frame = Frame(frame.master, bd=1, relief='solid')
    for child in frame.winfo_children():
        new_child = child.__class__(new_frame)
        new_child.configure(**child.configure())
        new_child.pack(side='left', expand=True, fill='both')
    return new_frame


