import json

def paginate_properties(input_file, output_file, items_per_page=100):
    # Load the input JSON data
    with open(input_file, 'r') as f:
        data = json.load(f)

    properties = data['properties']
    total_items = len(properties)
    total_pages = (total_items // items_per_page) + (1 if total_items % items_per_page != 0 else 0)
    
    paginated_data = {"properties": {}}

    for page in range(1, total_pages + 1):
        start_index = (page - 1) * items_per_page
        end_index = start_index + items_per_page
        paginated_data["properties"][f"page{page}"] = properties[start_index:end_index]

    # Write the paginated JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(paginated_data, f, indent=2, ensure_ascii=False)

# Usage
input_file = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson.json'
output_file = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson_paginated.json'
paginate_properties(input_file, output_file)
