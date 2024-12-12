name = input("Name of person that we are calculating the grades for: ")
one = int(input("Test 1: "))
two = int(input("Test 2: "))
three = int(input("Test 3: "))
four = int(input("Test 4: "))
lowest = input("do you want to drop the lowest grade Y or N? ", )

if one <= 0:
    print("Test scores must be greater then 0")
elif two <= 0:
    print("Test scores must be greater then 0")
elif three <= 0:
    print("Test scores must be greater then 0")
elif four <= 0:
    print("Test scores must be greater then 0")
if lowest == "Y":
    if one <= two and one <= three and one <= four:
        lowestgrade = one
    elif two <= three and two <= four:
        lowestgrade = two
    elif three <= four:
        lowestgrade = three
    else: lowestgrade = four
    average = (one + two + three + four - lowestgrade) / 3 
elif lowest == "N":
    average = (one + two + three + four) / 4
else: print("use N or Y to drop the lowest grade")

if average >= 94:
    print("Letter Grade for the test is: A+")
elif 94 <= average <= 96.9:
    print("Letter Grade for the test is: A")
elif 90 <= average <= 93.9:
    print("Letter Grade for the test is: A-")
elif 87 <= average <=89.9:
    print("Letter Grade for the test is: B+")
elif 84 <= average <= 86.9:
    print("Letter Grade for the test is: B")
elif 80 <= average <= 83.9:
    print("Letter Grade for the test is: B-")
elif 77 <= average <= 79.9:
    print("Letter Grade for the test is: C+")
elif 74 <= average <= 76.9:
    print("Letter Grade for the test is: C")
elif 70 <= average <= 73.9:
    print("Letter Grade for the test is: C-")
elif 67 <= average <= 69.9:
    print("Letter Grade for the test is: D+")
elif 64 <= average <= 66.9:
    print("Letter Grade for the test is: D")
elif 60 <= average <= 63.9:
    print("Letter Grade for the test is: D-")
elif average <= 59.9:
    print("Letter Grade for the test is: F")
print(name, "test avrige is: " , average)

