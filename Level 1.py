import pandas as pd

file_path = "C:\\Users\\joshi\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)

print("First 10 rows of the dataset:")
print(data.head(10))

print("\nBasic structure of the data:")
data.info()

print("\nMissing values in the dataset:")
print(data.isnull().sum())

num_trains = data['Train_No'].nunique()
print(f"\nNumber of trains: {num_trains}")

unique_source_stations = data['Source_Station_Name'].nunique()
unique_destination_stations = data['Destination_Station_Name'].nunique()
print(f"Count of unique source stations: {unique_source_stations}")
print(f"Count of unique destination stations: {unique_destination_stations}")

common_source_station = data['Source_Station_Name'].mode()[0]
common_destination_station = data['Destination_Station_Name'].mode()[0]
print(f"Most common source station: {common_source_station}")
print(f"Most common destination station: {common_destination_station}")

data['Source_Station_Name'] = data['Source_Station_Name'].str.upper()
data['Destination_Station_Name'] = data['Destination_Station_Name'].str.upper()

print("\nCleaned data (first 10 rows):")
print(data.head(10))
