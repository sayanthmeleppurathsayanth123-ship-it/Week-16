import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("logs.csv")
#data cleaning
df.columns=df.columns.str.strip()

df=df.drop_duplicates()

#time stamp to datetime
df["timestamp"]=pd.to_datetime(df["timestamp"],format="%d/%b/%Y:%H:%M:%S")

print("\n missing values : \n",df.isnull().sum())

print("\nData after cleaming:", df.shape)    #Returns the number of rows and columns

#anlaysis

print("\n Total requests:", len(df))         #returns the number of rows in the DataFrame.
print("Unique ip :",df["ip"].nunique())
print("\n status code \n", df["status"].value_counts())

#request per ip

ip_counts=df["ip"].value_counts()
print("\n top ip: \n", ip_counts.head())

#failed login attempts
failed=df[df["status"] == 403]
failed_counts= failed["ip"].value_counts()

print("\n Failed login attempts: \n", failed_counts.head())

#Time based attack
df["hour"]=df["timestamp"].dt.hour
hourly_activity=df.groupby("hour").size()
print("\n Hourly activity: \n", hourly_activity)

#visualization
#top ips
plt.figure()
ip_counts.head(10).plot(kind="bar")
plt.title("Top ip by requests")
plt.xlabel("Ip address")
plt.ylabel("Number of requests")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#status code
plt.figure()
df["status"].value_counts().plot(kind="bar")
plt.title("Status code count")
plt.xlabel("Status count")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#time based activity
plt.figure()
hourly_activity.plot(kind="line")
plt.title("Request by hour")
plt.xlabel("Hour of day")
plt.ylabel("Number of requests")
plt.grid()
plt.tight_layout()
plt.show()

#Failed login attempts
plt.figure()
failed_counts.head(5).plot(kind="bar")
plt.title("Top failed login ips")
plt.xlabel("ip address")
plt.ylabel("Failed attempts")
plt.tight_layout()
plt.show()