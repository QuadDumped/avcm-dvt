import h5py

path = "log_210129_124838_1611920928.h5"

def groupItem(itemName):
    with h5py.File(path, "r") as log:

      a_group_key = list(log.keys())[0]
    
      data = list(log[a_group_key])

      #anropa gruppens som objekt
      group = log[a_group_key]
      #hämta ut item i gruppen som objekt med getitem-metod, i det här fallet "app"
      app = group.__getitem__(itemName)
      #lista allt som app innehåller
      print(list(app))

      valueList = list(app)
      return valueList
    
def retrieveGroups():
  with h5py.File(path) as log:
    groups = list(log.keys())
    return groups

def groupStructure(group):
  with h5py.File(path) as log:
    data = list(log[group])
    return data


