import os
import sys
import pickle

with open("report01.pkl", "rb") as file:
    file_upload = pickle.load(file)
    

print("\n Report restored")
print(file_upload)