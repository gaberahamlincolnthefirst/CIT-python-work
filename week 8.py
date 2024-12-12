def getfloatInput(spromped):
    fNumber = 0

    while fNumber <= 0 :

        try:   

            fNumber = float(input(spromped)) 

        except ValueError:

            print("Input must a numeric value")
    return fNumber
def getmedean(numberslist):
    fmedean = 0
    numberslist.sort()
    if len(numberslist) % 2 == 0:
#me and si couldnt figure out the right equation for the four options one
        fmedean = (numberslist[len(numberslist) // 2] +  numberslist[(len(numberslist) // 2) + 1]) / len(numberslist)
    else:
        fmeadean = numberslist[len(numberslist) // 2]
    return fmedean        
def main():
    numberslist = []
    while True:
        fnumber = getfloatInput('enter property sales value: ')
        numberslist.append(fnumber)
        schoise = input('enter another value Y or N: ')
        if schoise == 'N':
            break
    fmedean = getmedean(numberslist)
    print(fmedean)
    icounter = 1
    for property in numberslist:
        print(f"property {icounter} ${property}")
        icounter += 1
    print(min(numberslist))
    print(max(numberslist))
    print(sum(numberslist)) 
    print(sum(numberslist)/len(numberslist))

main()
