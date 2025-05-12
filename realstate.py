import csv

def getDataInput():
    listData = []

    with open('RealEstateData.csv', 'r') as file:
        salesData = csv.reader(file)
        next(salesData)
        for row in salesData:
            listData.append(row)
    #print(listData)
    return listData

def getMedian(lstList1):
   lstList1.sort()
   iListLength = len(lstList1)


   if iListLength % 2 == 0:
       print(f"The length if the list is even: {iListLength}")
       fMedianRight = lstList1[iListLength // 2]
       fMedianLeft = lstList1[(iListLength // 2) - 1]


       fMedian = (fMedianLeft + fMedianRight) / 2

   else:
       print(f"The length if the list is odd: {iListLength}")
       fMedian = lstList1[iListLength // 2]


   return fMedian
def main():
   lstData = getDataInput() # can I just say i had the hardest time figuring out how to bring the getDataInput into the main() without errors, it was painfull
   lstPrices = []

   dictPropertyType = {}
   dictCity = {}
   dictZip = {}

   for row in lstData:

       sCity = row[1]
       sPType = row[7]
       fPrice = float(row[8])

       sZip = row[2]


       if sPType in dictPropertyType:
           dictPropertyType[sPType] += fPrice
       else:
           dictPropertyType[sPType] = fPrice


       if sCity in dictCity:
           dictCity[sCity] += fPrice
       else:
           dictCity[sCity] = fPrice


       if sZip in dictZip:
           dictZip[sZip] += fPrice
       else:
           dictZip[sZip] = fPrice


       lstPrices.append(fPrice)

   print("Summary by Property Type:")
   for propertyType, fTotal in dictPropertyType.items():

       print(f"{propertyType:20s}{fTotal:15,.2f}")

   print("Summary by City:")
   for sCity, fTotal in dictCity.items():
       print(f"{sCity:20s}{fTotal:15,.2f}")


   print(f"{'The min is: ':20s}{min(lstPrices):15,.2f}")

   print(f"{'The max is: ':20s}{max(lstPrices):15,.2f}")

   print(f"{'The sum is: ':20s}{sum(lstPrices):15,.2f}")

   print(f"{'The average is ':20s}{sum(lstPrices) / len(lstPrices):15,.2f}")

   print(f"{'The Median is ':20s}{getMedian(lstPrices):15,.2f}")


main()

