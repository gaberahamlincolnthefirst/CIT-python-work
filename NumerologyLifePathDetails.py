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

    def Name(self): return self.name

    def BirthDay(self): return self.birthday

    def Birthdate(self): return self.birthdate

    def LifePath(self): return self.lifePath

    def Attitude(self): return self.iattitude

    def Soul(self): return self.soul

    def PowerName(self): return self.power

    def Personality(self): return self.personality

    def __str__(self):
        return f"""Name: {self.Name()}
        Birthdate: {self.Birthdate()}
        Life Path: {self.LifePath()}
        Birthday: {self.BirthDay()}
        Attitude: {self.Attitude()}
        Soul: {self.Soul()}
        Personality: {self.Personality()}
        Power: {self.PowerName()}"""


class NumerologyExtended(Numerology):
    def __init__(self, sName, sDOB):
        Numerology.__init__(self, sName, sDOB)

        self.__lifePathDescription = {

            1: "The Independent: Wants to work/think for themselves", 2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention", 4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert", 6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality", 8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"}

    @property # this part i really had to watch and learn from the si's in revew because i still don't have a full understanding of decoraters
    def LifePathDescription(self):
        return self.__lifePathDescription.get(self.lifePath)

    def __str__(self): return \
        f"{Numerology.__str__(self)}\
        \n{'Life Path Description: ':25s}{self.LifePathDescription}\n"
''