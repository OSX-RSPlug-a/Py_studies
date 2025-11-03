import os
import sys
import pickle

report = {
    "client": "Dude Bug",
    "total": 999.99,
    "items": ["Notebook gamer", "Mouse Game", "Keyboard gamer"],
    "payment": True
}

with open("report01.pkl", "wb") as file:
    pickle.dump(report, file)
    

print("Report fiel created seuccesfuly")