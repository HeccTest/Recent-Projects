import sys # used for exitting

stringMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

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
        print(f"{self.day} of {stringMonths[self.month - 1]} of {self.year}")

days31 = [1,3,5,7,8,10,12] # months with 31 days
days30 = [4,6,9,11] # months with 30 days. NOTE: Feb has 29 days for our example
def checkDay(day, month):
    if month in days31 and day <= 31: # valid case
        return day
    elif month in days30 and day <= 30: # valid case
        return day
    elif month == 2 and day <= 29: # valid case
        return day
    elif month < 1 or month > 12: # invalid month entered, cannot compute if day is correct
        return -1
    else:
        sys.exit("INVALID DAY ENTERED")

def checkMonth(month):
    if month < 1 or month > 12:
        sys.exit("INVALID MONTH ENTERED")
    else:
        return month

def printAll():
    print() # formatting
    for i in calendar:
        i.print()
    print() # formatting

def printByMonth(month):
    print() # formatting
    for i in calendar:
        if i.month == int(month):
            i.print()
    print() # formatting

def printRange(month1, month2): # print between the range of two months (ie. jan to march)
    print() # formatting
    for i in calendar:
        if i.month >= month1 and i.month <= month2:
            i.print()
    print() # formatting

calendar = []
choice = -1
print("CALENDAR APP")

# adding some default dates for testing, comment out if not using
calendar.append(date(10,11,2000))
calendar.append(date(19,11,2000))
calendar.append(date(1,5,2000))
calendar.append(date(29,1,2000))
calendar.append(date(30,12,2000))
calendar.append(date(31,12,2000))

while choice != 7:
    print("Choices: \n1. Create a new date\n2. Edit a date\n3. Remove a date\n4. Show all dates\n5. Print dates by month\n6. Print in range\n7. Exit")

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

    if choice == 5:
        inputMonth = input("Which month would you like to print? (MM)")
        printByMonth(inputMonth)

    if choice == 6:
        inputRange = input("Between which months? (MM-MM)")
        inputRange = inputRange.split("-")
        printRange(int(inputRange[0]), int(inputRange[1]))


# Extra: dates are not sorted. Can implement a sorting system
# Extra: printing between months may not be sufficient. Can implement printing between dates (using day, month, and year); can be tedious!