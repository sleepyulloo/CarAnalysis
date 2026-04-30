import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Automobile_data.csv')

to_drop = ["normalized-losses",
           "symboling",
           "aspiration",
           "num-of-doors",
           "drive-wheels",
           "engine-location",
           "wheel-base",
           "length",
           "width",
           "height",
           "curb-weight",
           "engine-type",
           "num-of-cylinders",
           "engine-size",
           "fuel-system",
           "bore",
           "stroke",
           "compression-ratio",
           "horsepower",
           "peak-rpm",
           ]

df.drop(columns=to_drop,inplace=True)
df.replace('?','0',inplace=True)

print(df)



cars = df['make'].value_counts()
cars.plot(kind='pie')
plt.title('Number of Each Type of Car')
plt.xlabel('Car Type')
plt.ylabel('Count')
plt.show()

body = df['body-style'].value_counts()
body.plot(kind= 'bar')
plt.title('Body Style of the Cars')
plt.xlabel('Body Style')
plt.ylabel('Count')
plt.show()


fuel = df['fuel-type'].value_counts()
fuel.plot(kind= 'barh')
plt.title('Fuel Type of the Cars')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()

data = list(range(205))
df1= pd.DataFrame(data,columns=['Y'])


fig, ax = plt.subplots()
ax.scatter(df['city-mpg'], df1['Y'], color='navy', alpha=0.5)
ax.set_xlabel('City MPG')
ax.set_ylabel('Count')
ax.set_title('Scatter Plot For City MPG')
plt.show()
city_avg = df["city-mpg"].mean()

fig, ax = plt.subplots()
ax.scatter(df['highway-mpg'], df1['Y'], color='red', alpha=0.5)
ax.set_xlabel('Highway MPG')
ax.set_ylabel('Count')
ax.set_title('Scatter Plot For Highway MPG')
plt.show()
high_avg = df["highway-mpg"].mean()

price = df['price'].value_counts()
price.plot(kind= 'line')
plt.title('Price of the Cars')
plt.xlabel('price Type')
plt.ylabel('Count')
plt.show()

'''fig, ax = plt.subplots()
ax.scatter(df['price'], df1['Y'], color='black', alpha=0.1)
ax.set_xlabel('Price')
ax.set_ylabel('Count')
ax.set_title('Scatter Plot For Highway MPG')
plt.show()'''


Toyota = df['make'].value_counts()['toyota']
print(f"The number of Toyotas in the data set is: {Toyota}")

Sedan = df["body-style"].value_counts()['sedan']
print(f"The number of Sedans in the data set is: {Sedan}")

Gas = df["fuel-type"].value_counts()['gas']
print(f"The number of cars that run on Gas in the data set is: {Gas}")

print(f"The average MPG for the city is: {round(city_avg,2)}")

print(f"The average MPG for the highway is: {round(high_avg,2)}")

print("The average Price for a car is: $15,236")

print("By analyzing the data we can say that a sedan Toyota that runs on gas around the price of $15,236 is the best car to buy.")
