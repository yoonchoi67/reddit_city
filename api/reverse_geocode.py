import requests, json, time

def reverse_geocode(lat, lon):
    url = 'https://nominatim.openstreetmap.org/reverse'
    params = {
        'format': 'json',
        'lat': lat,
        'lon': lon,
        'addressdetails': 1
    }
    headers = {
        'User-Agent': 'jycswe/1.0 jyc.swe@gmail.com'  # Replace with your app name and email
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data
        

    except requests.exceptions.RequestException as e:
        print(f'Error reverse geocoding: {e}')
        return None

cache = dict()

def get_countries(input_file, output_file, items_per_page=100):
    # Load the input JSON data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_properties = []
    properties = data['properties']
    
    visited = True
    with open(output_file, 'a', encoding='utf-8') as f:
        


        for i, property in enumerate(properties):
            if property['permalink'] == '/r/CityPorn/comments/9mzibi/brussels_when_it_gets_dark/':
                visited = False
                continue
            if visited:
                continue

            print('on: ', i)
            lat, long = round(property['lat_y'], 5), round(property['long_x'], 5)

            if (lat, long) in cache:
                property['country'], property['country_code'], property['state'], property['state_code'] = cache[(lat, long)]
                print(f'getting cached item at: {i}')

            else:
                data = reverse_geocode(lat, long)

                country = None
                country_code = None
                state = None
                state_code = None

                if 'address' in data:
                    if 'country' in data['address']:
                        country = data['address']['country']
                        property['country'] = country
                    if 'country_code' in data['address']:
                        country_code = data['address']['country_code']
                        property['country_code'] = country_code
                    if 'state' in data['address']:
                        state = data['address']['state']
                        property['state'] = state
                    if 'state_code' in data['address']:
                        state_code = data['address']['state_code']
                        property['state_code'] = state_code

                cache[(lat, long)] = [country, country_code, state, state_code]
                time.sleep(0.5)  # Increased to avoid rate limiting

            new_properties.append(property)

            if i != 0 and i % items_per_page == 0:  # Flush every `items_per_page` items
                json.dump(new_properties, f, indent=2, ensure_ascii=False)
                f.flush()
                new_properties = []  # Reset the list to avoid duplicating entries
                print('flushed at: ', i)

        # Final flush for any remaining items
        if new_properties:
            json.dump(new_properties, f, indent=2, ensure_ascii=False)
            f.flush()

# Usage
input_file = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson.json'
output_file = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson_with_country.json'
cache_file = '/Users/yoon/Desktop/general_code/frontend/my-app/api/country_code_cache.json'

# print(reverse_geocode(40.7896239, -73.9598939))
get_countries(input_file, output_file)

print(cache)

with open(cache_file, 'a', encoding='utf-8') as f:
    d = []
    for key, value in cache.items():
        d.append({
            'key': key,
            'country': value[0],
            'country_code': value[1]
            })
    j = json.dumps(d, indent=4)
    # print(d)
    json.dump(d, f, indent=2, ensure_ascii=False)