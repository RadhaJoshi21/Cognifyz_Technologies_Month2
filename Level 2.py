import pandas as pd

file_path = "C:\\Users\\joshi\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)

print("First 10 rows of the dataset:")
print(data.head(10))

print("\nBasic structure of the data:")
data.info()

print("\nMissing values in the dataset:")
print(data.isnull().sum())

saturday_trains = data[data['days'].str.contains('Saturday')]

specific_station = 'MADGOAN JN.'.upper()
trains_from_specific_station = data[data['Source_Station_Name'] == specific_station]

print("\nTrains operating on Saturdays:")
print(saturday_trains.head(10))

print("\nTrains starting from MADGOAN JN.:")
print(trains_from_specific_station.head(10))

trains_per_station = data.groupby('Source_Station_Name').size().reset_index(name='Train_Count')

day_map = data['days'].str.split(', ').explode().reset_index()
day_map.columns = ['index', 'day']

data_expanded = data.merge(day_map, left_index=True, right_on='index').drop(columns=['index'])

avg_trains_per_day = data_expanded.groupby(['Source_Station_Name', 'day']).size().groupby('Source_Station_Name').mean().reset_index(name='Avg_Trains_Per_Day')

print("\nNumber of trains originating from each station:")
print(trains_per_station.head(10))

print("\nAverage number of trains per day for each source station:")
print(avg_trains_per_day.head(10))

def categorize_days(days):
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    weekends = {'Saturday', 'Sunday'}
    day_set = set(days.split(', '))
    
    if day_set.issubset(weekdays):
        return 'Weekday'
    elif day_set.issubset(weekends):
        return 'Weekend'
    else:
        return 'Mixed'

data['Day_Category'] = data['days'].apply(categorize_days)

print("\nEnhanced dataset with 'Day_Category':")
print(data.head(10))
