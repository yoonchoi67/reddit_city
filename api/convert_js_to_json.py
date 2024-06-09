import json
# Define the path to your large JSON file
file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson.js'
output_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson.json'

# Initialize an empty list to hold the properties
properties_list = []

# Open the input file and process it line by line
with open(file_path, 'r') as file:
    for line in file:
        data = json.loads(line.strip()[:-1])
        properties = data.get('properties', {})
        properties_list.append(properties)

# Create the final dictionary structure
final_data = {
    'properties': properties_list
}

# Write the final data to the output file
# with open(output_path, 'w') as outfile:
#     json.dump(final_data, outfile, indent=1, ensure_ascii=False)

print(f"Processed data has been written to {output_path}")
