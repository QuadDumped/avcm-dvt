import h5py
import matplotlib

import matplotlib.pyplot as plt


def plotFunction(dataList):
  #hämtar ut y-värden i dataList, x ökas för varje item eller "row" i dataList
  #lägger sedan till dessa i individuella x och y-listor som kan plottas ut med plt.plot
  #detta är endast utformat för "ttTask" och måste ändras om strukturen på listan är annorlunda
  x = []
  y = []

  i = 0

  for row in dataList:
    i+=1
    x.append(i)
    y.append(row[1])

  plt.plot(x, y)
  plt.show()

#annan variant, maxValues är hur många värden från listan du vill skriva ut, detta eftersom listan kan innehålla många items
def plotFunction(dataList, maxValues):
  x = []
  y = []

  i = 0

  for row in dataList:
    i+=1
    if len(x) < maxValues:
      x.append(i)
      y.append(row[1])

  plt.plot(x, y)
  plt.show()

#Xincrement är om x ska ökas med 1 för varje värde i dataList, eller som det ska hämtas direkt som ett x värde 
#X och Y-index väljer vilka indexes i värdet som anger x och y
def plotFunctionPlus(dataList, maxValues = math.inf, Xincrement = True, Yindex = 0, Xindex = None):
  x = []
  y = []

  i=0

  for row in dataList:
    i+=1
    if len(x) < maxValues:
      
      if Xincrement == True:
        x.append(i)
      else:
        x.append(row[Xindex])

      y.append(row[Yindex])

  plt.plot(x, y)
  plt.show()






#exempel
#plotFunction(groupItem("ttTask"))
#plotFunction(groupItem("ttTask"), 1000)
#plotFunctionPlus(groupItem("ttTask"), 1000, True, 1)