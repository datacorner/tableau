import pandas as pd
import sys

infile = sys.argv[1]
f = open(infile, "r", encoding="utf-8") 
data = f.read()
myData = pd.DataFrame(data.split("\n"))
mydata2 = pd.DataFrame([data.split("\n")[i].split(" – ") for i in range(len(myData)-1)])
mydata2.columns = ["ID", "Description"]
mydata2.to_csv("REF_" + infile, index=False, doublequote=True)