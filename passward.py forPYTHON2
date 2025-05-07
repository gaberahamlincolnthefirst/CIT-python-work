#gabriel duponte password validater
def main(): #to store for later use
    sName = input("Enter full name such as John Smith: ", )
    sInitials = ""
    sInitials += sName[0] + sName [sName. find (" ")+1] # to fetch initials from sName
    print(sInitials)
    sPassword = ""
    bIsValid = False
    while not bIsValid:
        bLength = bPass = bInitials = cUpper = cLower = bDigit = bSpecial = bCount = False # i will say, im not sure why this line does not work as an if statement, would make more sense
        dictCharacters ={}
        sPassword = input("Enter new password: ", )
        bLength = True if len(sPassword) in range(8, 13) else print("Password must be between 8 and 12 characters.")
        bPass = True if not sPassword.lower ().startswith("pass") else print("Password can't start with Pass")
        bInitials = True if not sInitials.lower() in sPassword.lower() else print("Password must not contain user initsals")

        for char in sPassword:
            if char.isupper(): cUpper = True
            elif char.islower(): cLower = True
            elif char.isdigit():  bDigit = True
            elif char in '! @#$%^': bSpecial = True
            if char in dictCharacters:
                continue
            iCount = sPassword.lower().count(char.lower())
            if iCount > 1: dictCharacters[char.lower()] = iCount

        if not cUpper: print("Password must contain at least 1 uppercase letter.")
        if not cLower: print("Password must contain at least 1 lowercase letter.")
        if not bDigit: print("Password must contain at least 1 number.")
        if not bSpecial: print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ")
        bcount = True if not dictCharacters else print(f"These characters occur more then once:\n{dictCharacters}")
        if bLength and bPass and bInitials and cUpper and cLower and bDigit and bSpecial and bCount: bIsValid = True
        print("Password is valid and OK to use.")
main()

