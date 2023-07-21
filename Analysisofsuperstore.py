from google.colab import drive
drive.mount('/content/drive')

cd drive/

cd MyDrive

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("SampleSuperstore.csv")
df.head()

df.drop(columns="Postal Code")

df.drop(columns="Postal Code", inplace=True)

df.head()

print(df["Ship Mode"].unique())
print(df["Segment"].unique())
print(df["Country"].unique())
print(df["Category"].unique())
print(df["City"].unique())
print(df["State"].unique())
print(df["Region"].unique())
print(df["Sub-Category"].unique())
print(df["Sales"].unique())
print(df["Quantity"].unique())
print(df["Discount"].unique())
print(df["Profit"].unique())

df.describe()

df.info()

df.isna().sum()

df.groupby("Region")["Sales"].sum().plot.bar()

df.groupby("Region")["Profit"].sum().plot.bar()

df.groupby("Region")["Sales"].sum().plot.pie(autopct="%1.0f%%")

df.groupby("Region")["Profit"].sum().plot.pie(autopct="%1.0f%%")

df.groupby("Segment")["Sales"].sum().plot.bar()

df.groupby("Segment")["Profit"].sum().plot.bar()

df.groupby("Category")["Sales"].sum().plot.bar()

df.groupby("Category")["Profit"].sum().plot.bar()

df.groupby("Category")["Sales"].sum().plot.pie(autopct="%1.0f%%")

df.groupby("Category")["Profit"].sum().plot.pie(autopct="%1.0f%%")

df.groupby("State")["Sales"].sum().plot.bar()

df.groupby("State")["Profit"].sum().plot.bar()

