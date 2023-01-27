class dayOfYear:
    def __init__(self, day, month): # constructor with parameters: day, month
        self.day = day
        self.month = month

    def setDay(self, newDay): # a method called setDay taking in parameter: newDay
        # set constraints here if desired (ie. newDay belongs to the range [1, 31])
        self.day = newDay

    def setMonth(self, newMonth):
        self.month = newMonth

    def print(self):
        print(f"{self.day} day of month: {self.month}") # f is used to denote a formatted string literal. allows the use of curly braces, which lets us use our object.


calendar = [] # an arrayList the will hold our class element: dayOfYear
choice = -1

print("Calendar app!")

while choice != 5:
    print("Choices: \n1. Create a new date\n2. Edit a date\n3. Remove a date\n4. Show all dates\n5. Exit")
    choice = int(input("what would you like to do? "))

    if choice == 1:
        newDate = input("Enter a new date (day month): ")
        newDate = newDate.split(" ")
        day = int(newDate[0])
        month = newDate[1]
        calendar.append(dayOfYear(day, month))    
    elif choice == 2: # not implemented beyond this point. The remainder of the content is fairly self explanatory
        print("2")
    elif choice == 3:
        print("3")
    elif choice == 4:
        print("4")
    else:
        break # if choice is not in range [1, 5]


for i in calendar: # prints all items in arrayList calendar
    i.print()