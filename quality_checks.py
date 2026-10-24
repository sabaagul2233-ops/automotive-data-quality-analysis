import pandas as pd

df = pd.read_csv("vehicles_raw.csv")

print("AUTOMOTIVE DATA QUALITY REPORT")
print("------------------------------")
print("Total records:", len(df))

print("\n1. Missing Values:")
print(df.isnull().sum())

print("\n2. Duplicate VIN Records:")
duplicates = df[df.duplicated(subset=["vin"], keep=False)]
print(duplicates)

print("\n3. Invalid Prices:")
print(df[df["price"] <= 0])

print("\n4. Invalid Mileage:")
print(df[df["mileage"] < 0])

print("\n5. Invalid Manufacturing Years:")
print(df[(df["year"] < 1886) | (df["year"] > 2027)])

print("\nData Quality Checks Completed!")
