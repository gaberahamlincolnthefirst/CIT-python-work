
import sqlite3
import csv

dbConnection = sqlite3.connect("myDatabase.db")
dbCursor = dbConnection.cursor()

try:
    sCreateTable = "Create Employee Table(EmployeeID int, Name text)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    sCreateTable = "Create Pay Table(EmployeeID int, year int, Earnings real)"
    dbConnection.execute(sCreateTable), print(sCreateTable)

    sCreateTable = "Create SocialSecurity Table(Year int, Minimum real)"
    dbConnection.execute(sCreateTable), print(sCreateTable)
    dbConnection.commit()

except sqlite3.OperationalError: print("Could not create table")



sInsertPay = "INSERT INTO Pay(EmployeeID, year, Earnings) VALUES("
sInsertPayReset = sInsertPay

with open("Pay.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        sInsertPay += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertPay)

        try:
            dbConnection.execute(sInsertPay)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")

        sInsertPay = sInsertPayReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")


sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurityMinimum(Year, Minimum) VALUES("
sInsertSocialSecurityMinimumReset = sInsertSocialSecurityMinimum

with open("SocialSecurityMinimum.txt", "r") as file:

    iRows = 0
    reader = csv.reader(file)

    next(reader)

    for row in reader:


        sInsertSocialSecurityMinimum += f"{row[0]}, {row[1]})"
        print(sInsertSocialSecurityMinimum)

        try:
            dbConnection.execute(sInsertSocialSecurityMinimum)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        sInsertSocialSecurityMinimum = sInsertSocialSecurityMinimumReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")


sInsertEmployee = "insert into Emoloyee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee

with open("Employee.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        sInsertEmployee += f"{row[0]}, '{row[1]}')"
        print(sInsertEmployee)

        try:
            dbConnection.execute(sInsertEmployee)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        sInsertEmployee = sInsertEmployeeReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")


print(f"{'Employee name':<20} {'year':<5} {'earnings':>15} {'minimum':>15} {'include':>15}")
for row in dbCursor.fetchall():

    fResult = ""

    if row[2] >= row[-1]: fResult = "Yes"
    else: fResult = "No"
    '''
    file1 = open("Pay.txt", "r")
    file2 = open("SocialSecurityMinimum.txt", "r")
    file3 = open("Employee.txt", "r")

    br = file1.read()
    brr = file2.read()
    brrr = file3.read()

    file1.close()
    file2.close()
    file3.close()

    destiny_file = open('concatenated.txt', 'w')

    destiny_file.write(br + brr + brr)

    destiny_file(close)
    '''