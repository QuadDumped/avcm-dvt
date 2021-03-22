import h5py
import h5reader

selectedgroup = h5reader.retrieveGroups()[0]
print(h5reader.newGroupStructure(selectedgroup))