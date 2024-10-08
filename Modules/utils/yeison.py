import os
import json

MY_DATABASE = 'data/usuarios.json'

def NewFile(data):
    with open(MY_DATABASE, "w") as md:
        json.dump(data,md,indent=4)
        
def LeerFile():
    if os.path.isfile(MY_DATABASE):
        with open (MY_DATABASE) as al:
            return json.load(al)
    else:
        return {}
    
def checkFile(initialDta):
    if not os.path.isfile(MY_DATABASE):
        NewFile(initialDta)