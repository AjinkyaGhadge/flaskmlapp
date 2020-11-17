from os import listdir
from os.path import isfile, join
import os
mypath = os.getcwd()
print(mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    if i == "testscript.py":
    	continue
#    os.system("sudo curl -X POST -F file=@"+"".join(i)+" "+"https://flaskmlappcs532aj.herokuapp.com/predict")
    os.system("sudo curl -X POST -F file=@"+"".join(i)+" "+"http://127.0.0.1:5000/predict")
