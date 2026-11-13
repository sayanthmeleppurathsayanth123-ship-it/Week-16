import re
import pandas as pd

pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST) (.*?) HTTP.*" (\d+) (\d+)'

data=[]
with open(r"C:\Users\User\OneDrive\Desktop\WEEK-16\Mini_Project\access.log", "r") as file:
        for line in file:
            match=re.search(pattern,line)

            if match:
             ip=match.group(1)
             timestamp=match.group(2)
             method=match.group(3)
             url=match.group(4)
             status=match.group(5)
             size=match.group(6)

             data.append([timestamp,ip,method,url,status,size])

df=pd.DataFrame(data,columns=[
    "timestamp","ip","method","url","status","size"
])

df.to_csv("logs.csv",index=False)
print("csv created successfuly")

