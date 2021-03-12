import h5py

path = "C:/Users/HP/Documents/Python/Projekt/log_210129_124838_1611920928.h5"


def groupStructure():
    with h5py.File(path, "r") as f:
      #hitta första gruppen
      a_group_key = list(f.keys())[0]
    
      #hämta data
      data = list(f[a_group_key])
      indexes = list(range(0, 7))
    
      print("Group: " + a_group_key)
      for itemIndex in indexes:
          print(data[itemIndex])

def groupItem(itemName):
    with h5py.File(path, "r") as f:

      a_group_key = list(f.keys())[0]
    
      data = list(f[a_group_key])

      #anropa gruppens som objekt
      group = f[a_group_key]
      #hämta ut item i gruppen som objekt med getitem-metod, i det här fallet "app"
      app = group.__getitem__(itemName)
      #lista allt som app innehåller
      print(list(app))
    

groupStructure()



#print(list(f["0 VCM1"]))