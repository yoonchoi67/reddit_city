import datetime
import json
import calendar
from collections import defaultdict

# Define the path to your large JSON file
file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson.json'
output_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/submission_freq.json'

# Initialize an empty list to hold the properties
properties_list = []
final_dict = defaultdict(dict)


# Open the input file and process it line by line
with open(file_path, 'r') as file:
    data = json.load(file)
    properties_list = data['properties']
    
for property in properties_list:
    timestamp = property['created_at']
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # Extract year, month, and day from the datetime object
    year = dt_object.year
    month_number = dt_object.month
    month_name = calendar.month_name[month_number]

    if month_name not in final_dict[year]:
        final_dict[year][month_name] = 0
    final_dict[year][month_name] += 1

print(final_dict)

# Create the final dictionary structure
final_data = {
    'submissions frequency': final_dict
}

# Write the final data to the output file
with open(output_path, 'w') as outfile:
    json.dump(final_data, outfile, indent=1, ensure_ascii=False)

print(f"Processed data has been written to {output_path}")


{
 "properties": [
  {
   "created_at": 1298816706,
   "display": "Hometown, Cook County, Illinois, United States of America",
   "id": "ftp2y",
   "permalink": "/r/CityPorn/comments/ftp2y/my_hometown_of_columbus_oh_usa_1800x1350/",
   "title": "My Hometown of Columbus, OH, USA [1800x1350]",
   "lat_y": 41.731246,
   "long_x": -87.7309534,
   "score": 18
  }]}



{
 "Submission Freq by Year": {
   2020: {
       "january": 33,
       "february": 2,
   },
   2021: {
       "january": 33,
       "february": 2,
   }
 }
}