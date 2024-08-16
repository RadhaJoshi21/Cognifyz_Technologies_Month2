import pandas as pd

file_path = "C:\\Users\\joshi\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)

source_freq = data['Source_Station_Name'].value_counts()
destination_freq = data['Destination_Station_Name'].value_counts()

freq_df = pd.DataFrame({'Source_Frequency': source_freq, 'Destination_Frequency': destination_freq}).fillna(0)

equal_freq_stations = freq_df[freq_df['Source_Frequency'] == freq_df['Destination_Frequency']]

print("Stations that are both source and destination with equal frequency:")
print(equal_freq_stations)

train_by_day = data['days'].value_counts()

print("\nTrain operations distribution by day of the week:")
print(train_by_day)

highest_traffic_day = train_by_day.idxmax()
highest_traffic_count = train_by_day.max()

print(f"\nDay with the highest traffic: {highest_traffic_day} with {highest_traffic_count} train operations")

duplicated_routes = data[data.duplicated(['Source_Station_Name', 'Destination_Station_Name'], keep=False)]

if not duplicated_routes.empty:
    print("\nDuplicated routes found:")
    print(duplicated_routes[['Train_No', 'Source_Station_Name', 'Destination_Station_Name']].head(10))

route_counts = data.groupby(['Source_Station_Name', 'Destination_Station_Name']).size().reset_index(name='count')

high_frequency_threshold = route_counts['count'].quantile(0.99)
high_frequency_routes = route_counts[route_counts['count'] > high_frequency_threshold]

print(f"\nRoutes with unusually high frequency (Top 1% of routes):")
print(high_frequency_routes)

low_frequency_threshold = route_counts['count'].quantile(0.01)
low_frequency_routes = route_counts[route_counts['count'] < low_frequency_threshold]

print(f"\nRoutes with unusually low frequency (Bottom 1% of routes):")
print(low_frequency_routes)
