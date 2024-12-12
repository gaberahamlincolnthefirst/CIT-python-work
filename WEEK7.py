
import math
def getfloatInput(spromped):
    fNumber = 0
    while fNumber <= 0 :
        try:   
            fNumber = float(input(spromped)) 
        except ValueError:
            print("Input must a numeric value")
    return fNumber
def getgallonsofpaint(fsqairfeet, ffeatpgalon):
    fresult = fsqairfeet / ffeatpgalon
    fresult = math.ceil(fresult)
    return fresult
def getlaborhours(llaborhours, igallons):
    fresult = llaborhours * igallons
    return fresult
def getlaborcost(llaborhours, llaborcharge, igallons):
    fresult = (llaborhours * llaborcharge)* igallons
    return fresult
def getpaintcost(igallons, fpaintprice ):
    fresult = igallons * fpaintprice
    return fresult
def getsalestax(sstate):
    Ftxrate = 0
    if sstate == "MA":
        Ftaxrate = .0625
    elif sstate == "CT":
        Ftaxrate = .06
    elif sstate == "ME":
        Ftaxrate = .085
    elif sstate == "NH":
        Ftaxrate = 0
    elif sstate == "RI":
        Ftaxrate = .07
    elif sstate == "VT":
        Ftaxrate = .06
    else:
        Ftaxrate = 0
    return Ftaxrate
def showcostestimet(sstate, slastname, igallons, flaborhours, fpaintcost, flaborcost, ftaxcost, ftotal):
    print(sstate)
    print(slastname)
    print(igallons)
    print(flaborhours)
    print(f"${fpaintcost:,.2f}")
    print(f"${flaborcost:,.2f}")
    print(f"${ftaxcost:,.2f}")
    print(f"${ftotal:,.2f}")
def main():
    fsqairfeet = getfloatInput("Enter wall space in square feet: ")
    fpaintprice = getfloatInput("Enter paint price per gallon: ") 
    ffeatpgalon = getfloatInput("Enter feet per gallon: ")
    llaborhours = getfloatInput("Labor hours per galllon: ")
    llaborcharge = getfloatInput("labor charge per hour: ")
    slastname = input("Customer lat name: ")
    sstate = input("State job is in: ")
    igallons = getgallonsofpaint(fsqairfeet, ffeatpgalon)
#    print(igallons)
    flaborhours = getlaborhours(llaborhours, igallons)
#    print(flaborhours)
    flaborcost = getlaborcost(llaborhours, llaborcharge, igallons)
#    print(flaborcost)
    fpaintcost = getpaintcost(igallons, fpaintprice)
#    print(fpaintcost)
    ftaxrate = getsalestax(sstate)
    ftaxcost = (flaborcost + fpaintcost)* ftaxrate
#    print(ftaxcost)
    ftotal = flaborcost + fpaintcost + ftaxcost
#    print(ftotal)
    showcostestimet(sstate, slastname, igallons, flaborhours, fpaintcost, flaborcost, ftaxcost, ftotal)
    with open(f"{slastname}_paintjoboutput.txt","w") as file:
        file.write(f"{sstate}\n")
        file.write(f"{slastname}\n")
        file.write(f"{str(igallons)}\n")
        file.write(f"{str(flaborhours)}\n")
        file.write(f"{str(fpaintcost)}\n")
        file.write(f"{str(flaborcost)}\n")
        file.write(f"{str(ftaxcost)}\n")
        file.write(f"{str(ftotal)}\n")
main()
