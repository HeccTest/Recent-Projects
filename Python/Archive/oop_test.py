monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class date: # class
    def __init__(self, day, month, year): # constructor
        self.day = checkDay(day, month)
        self.month = checkMonth(month)
        self.year = year

    def setDay(self, newDay):
        self.day = checkDay(newDay, month)

    def setMonth(self, newMonth):
        self.month = checkMonth(newMonth)

    def setYear(self, newYear):
        self.year = newYear

    def print(self):
        print(f"{self.day} of {monthList[self.month - 1]} of {self.year}")

days31 = [1,3,5,7,8,10,12]
days30 = [4,6,9,11]
def checkDay(day, month):
    if month in days31 and day <= 31: # valid case
        return day
    elif month in days30 and day <= 30: # valid case
        return day
    elif month == 2 and day <= 29: # valid case
        return day
    elif month < 1 or month > 12: # check month will catch this error later
        return -1
    else:
        print("DAY ERROR")
        return -1

def checkMonth(month):
    if month > 12: # invalid case
        print("MONTH TOO HIGH")
        return -1
    elif month < 1: # invalid case
        print("MONTH TOO LOW")
        return -1
    else:
        return month

def printAll():
    for i in calendar:
        i.print()

calendar = []
choice = -1
print("CALENDAR APP")

calendar.append(date(10,11,2000))
calendar.append(date(19,11,2000))
calendar.append(date(1,5,2000))
calendar.append(date(29,1,2000))
calendar.append(date(30,12,2000))
calendar.append(date(31,12,2000))

while choice != 5:
    print("Choices: \n1. Create a new date\n2. Edit a date\n3. Remove a date\n4. Show all dates\n5. Exit")

    choice = int(input("What would you like to do: "))

    if choice == 1:
        entry = input("Enter a date (DD-MM-YYYY)") # 05-06-1998
        entry = entry.split("-")
        day = int(entry[0])
        month = int(entry[1])
        year = int(entry[2])
        calendar.append(date(day, month, year))

    if choice == 4:
        printAll()

    choice = 5