# gabe's Compound Interest with Loops code for week 6
while True:
    try:
        principle = float(input('What is the original Deposit (positive value): '))
        if principle > 0:
            break
        else:
            print('input must be positive: ')
    except ValueError:
        print('your input must be numeric')
while True:
    try:
        rate = float(input('what is the interest rate: ')) / 100 / 12
        if rate > 0:
            break
        else:
            print('input must be positive')
    except ValueError:
        print('your input must be numeric')
while True:
    try:
        time = int(input('what is the number of months: '))
        if time > 0:
            break
        else:
            print('input must be positive')
    except ValueError:
        print('your input must be numeric')

while True:
    try:
        goal = float(input('what is the goal: '))
        if goal >= 0:
            break
        else:
            print('input must be positive')
    except ValueError:
        print('your input must be numeric')
month = 1
# increase principle by multipling it to rate
while month <= time:
    principle = principle + (principle * rate)
    print(f'Month: {month} Account Balance is: ${principle:,.2f}')
    month = month + 1
if goal > 0:    
    month = time
    while principle <= goal:
        principle = principle + (principle * rate)
        month = month + 1
    print(f'It will take {month} months to reach the goal of ${goal:,.2f}')
# for how long it will take to reach goal ^
