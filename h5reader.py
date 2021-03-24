import h5py

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
    
def retrieveGroups(path):
  with h5py.File(path) as log:
    groups = list(log.keys())
    return groups

def groupStructure(path, group):
  with h5py.File(path) as log:
    dataset = list(log[group])
    return dataset

def readData(path, group, dataset):
  with h5py.File(path) as log:
    groupobject = log[group]
    datasetItem = groupobject.__getitem__(dataset)
    return list(datasetItem)

