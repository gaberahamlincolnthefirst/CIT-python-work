print("Gabe B. Duponte's Temp converter: ")
Temp = float(input("Enter a temperature: " ))
f = float(((9.0 / 5.0) * Temp ) + 32)
c = float((5.0 / 9) * (Temp - 32))
type = input("Is the temp F for Fahrenheit or C for Celsius? " )
if c > 100:
    print("Temp can not be > 100")
elif f > 212:
    print("Temp can not be > 212") 
else:    
    if type == 'F':
        print("The Celsius equivalent is: ", round(c, 1))
    elif type == 'C':
        print("The Fahrenheit equivalent is", round(f, 1))
    else:
        print("You must enter a F or C")
