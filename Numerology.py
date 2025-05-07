class Numerology:
    def __init__(self, sName, DateofBirth):

        self.name = sName
        self.birthdate = DateofBirth

        self.lifePath = 0
        for letter in self.birthdate.replace("-", "").replace("/", ""):

            self.lifePath += int(letter)
        self.lifePath = self.reduceNum(self.lifePath)


        self.birthday = 0
        iBirthdayDay = int(self.birthdate[3:5])

        self.birthday = self.reduceNum(iBirthdayDay)


        self.iattitude = 0
        for strNum in self.birthdate.replace("-", "").replace("/", "")[:4]:

            self.iattitude += int(strNum)
        self.iattitude = self.reduceNum(self.iattitude)

        self.dictCharacters = {"A": 1, "J": 1, "S": 1, "B": 2, "K": 2, "T": 2, "C": 3, "L": 3, "U": 3, "D": 4, "M": 4, "V": 4, "E": 5, "N": 5, "W": 5, "F": 6, "O": 6, "X": 6, "G": 7, "P": 7, "Y": 7, "H": 8, "Q": 8, "Z": 8, "I": 9, "R": 9}
            # assigning values for calculations
        self.soul = 0

        self.personality = 0

        for sLetter in self.name.upper():

            if sLetter in "AEIOU":
                self.soul += self.dictCharacters.get(sLetter, 0)
            else: self.personality += self.dictCharacters.get(sLetter, 0)

        self.soul = self.reduceNum(self.soul)


        self.personality = self.reduceNum(self.personality)


        self.power = 0

        self.power = self.reduceNum(self.soul + self.personality)



    def reduceNum(self, number):
        strNumber = str(number)
        while len(strNumber) > 1:
            number = int(strNumber[0]) + int(strNumber[1])
            strNumber = str(number)
        return number

    def getName(self): return self.name

    def getBirthDay(self): return self.birthday

    def getBirthdate(self): return self.birthdate

    def getLifePath(self): return self.lifePath

    def getAttitude(self): return self.iattitude

    def getSoul(self): return self.soul

    def getPowerName(self): return self.power

    def getPersonality(self): return self.personality

    def __str__(self):
        return f"""Name: {self.getName()}
        Birthdate: {self.getBirthdate()}
        Life Path: {self.getLifePath()}
        Birthday: {self.getBirthDay()}
        Attitude: {self.getAttitude()}
        Soul: {self.getSoul()}
        Personality: {self.getPersonality()}
        Power: {self.getPowerName()}"""

# in your hints you said we needed two classes? i was following along with mikey and nate and the first class seemed to make my program run just fine and i tried writing a second but it was just confusing me i dont know