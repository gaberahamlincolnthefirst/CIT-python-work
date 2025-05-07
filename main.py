#gabe duponte planetary waight calculator.
import pickle
def importdb():
    dictPlanetaryHistory = {}
   # this dict saves the data for later
    eof = False
    try:
        input_file = open('gdPlanetaryWeights.db', 'rb')
        while not eof:
            #egnores the program if the file does not exist
            try:
                dictPlanetaryHistory = pickle.load(input_file)
            except EOFError:
                eof = True
        input_file.close()
    except FileNotFoundError:
        pass
    return dictPlanetaryHistory


def main():
    dictPersonsWaight = {}
    dictPlanetConv = {
            "Mercury:" :0.38,
            "Venus:"   :0.91,
            "Moon:"    :0.165,
            "Mars:"    :0.38,
            "Jupiter:" :2.34,
            "Saturn:"  :0.93,
            "Uranus:"  :0.92,
            "Neptune:" :1.12,
            "Pluto:"   :0.066}
    # ask for the history/data that we preveusly put into the pickle file
    dictPlanetaryHistory = importdb()
    YesorNo = input("would you like to see the history y/n: ").lower()
    if YesorNo == 'y':
        for name, dictWeights in dictPlanetaryHistory.items():
            print(f"{name}, here are your weights on Solar System's planets")
            # print(key, value)
            for planet, weight in dictWeights.items():
                print(f"Weight on {planet:10s} {weight:10,.2f}")
    while True:
       #loops through name and waight functions
        sName = input("whats your name (enter kay to quit): ", ).title()
        if not sName: break
        #checks for reoccurnces in name unput
        if sName in dictPlanetaryHistory: print("is already in the history file. Enter a unique name.")
        if sName not in dictPlanetaryHistory:
            fWeight = float(input(" What is your weight: "))
           # calculates your waight compared to planets
            for planet, factor in dictPlanetConv.items():
                fCalculatedWeight = fWeight * factor
                dictPersonsWaight[planet] = fCalculatedWeight
                dictPlanetaryHistory[sName] = dictPersonsWaight
                print(f"{planet:10s}{fCalculatedWeight:10,.2f}")
    # dumps information into our pickle file
    with open("gdPlanetaryWeights.db", "wb") as file:
        pickle.dump(dictPlanetaryHistory, file)
main()
