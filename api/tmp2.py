import time

src_file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson_with_country.json'
dest_file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/final_geojson_with_country.json'
import json
continent_to_country_codes = {
    "africa": set([
        "dz", "ao", "bj", "bw", "bf", "bi", "cv", "cm", "cf", "td", "km", "cg", "cd",
        "dj", "eg", "gq", "er", "sz", "et", "ga", "gm", "gh", "gn", "gw", "ci", "ke",
        "ls", "lr", "ly", "mg", "mw", "ml", "mr", "mu", "yt", "ma", "mz", "na", "ne",
        "ng", "re", "rw", "sh", "st", "sn", "sc", "sl", "so", "za", "ss", "sd", "tz",
        "tg", "tn", "ug", "eh", "zm", "zw"
    ]),
    "asia": set([
        "af", "am", "az", "bh", "bd", "bt", "bn", "kh", "cn", "cy", "ge", "in", "id",
        "ir", "iq", "il", "jp", "jo", "kz", "kw", "kg", "la", "lb", "my", "mv", "mn",
        "mm", "np", "kp", "om", "pk", "ps", "ph", "qa", "kr", "sa", "sg", "lk", "sy",
        "tj", "th", "tl", "tr", "tm", "ae", "uz", "vn", "ye"
    ]),
    "europe": set([
        "al", "ad", "at", "by", "be", "ba", "bg", "hr", "cy", "cz", "dk", "ee", "fi",
        "fr", "ge", "de", "gr", "hu", "is", "ie", "it", "kz", "xk", "lv", "li", "lt",
        "lu", "mt", "md", "mc", "me", "nl", "mk", "no", "pl", "pt", "ro", "ru", "sm",
        "rs", "sk", "si", "es", "se", "ch", "ua", "gb", "va"
    ]),
    "north america": set([
        "ag", "bs", "bb", "bz", "ca", "cr", "cu", "dm", "do", "sv", "gd", "gt", "ht",
        "hn", "jm", "mx", "ni", "pa", "kn", "lc", "vc", "tt", "us"
    ]),
    "oceania": set([
        "as", "au", "ck", "fj", "pf", "gu", "ki", "mh", "fm", "nr", "nc", "nz", "nu",
        "mp", "pw", "pg", "pn", "ws", "sb", "tk", "to", "tv", "vu", "wf"
    ]),
    "south america": set([
        "ar", "bo", "br", "cl", "co", "ec", "fk", "gf", "gy", "py", "pe", "sr", "uy", "ve"
    ])
}
usa_states = {
    "Alabama": 0,
    "Alaska": 0,
    "Arizona": 0,
    "Arkansas": 0,
    "California": 0,
    "Colorado": 0,
    "Connecticut": 0,
    "Delaware": 0,
    "Florida": 0,
    "Georgia": 0,
    "Hawaii": 0,
    "Idaho": 0,
    "Illinois": 0,
    "Indiana": 0,
    "Iowa": 0,
    "Kansas": 0,
    "Kentucky": 0,
    "Louisiana": 0,
    "Maine": 0,
    "Maryland": 0,
    "Massachusetts": 0,
    "Michigan": 0,
    "Minnesota": 0,
    "Mississippi": 0,
    "Missouri": 0,
    "Montana": 0,
    "Nebraska": 0,
    "Nevada": 0,
    "New Hampshire": 0,
    "New Jersey": 0,
    "New Mexico": 0,
    "New York": 0,
    "North Carolina": 0,
    "North Dakota": 0,
    "Ohio": 0,
    "Oklahoma": 0,
    "Oregon": 0,
    "Pennsylvania": 0,
    "Rhode Island": 0,
    "South Carolina": 0,
    "South Dakota": 0,
    "Tennessee": 0,
    "Texas": 0,
    "Utah": 0,
    "Vermont": 0,
    "Virginia": 0,
    "Washington": 0,
    "West Virginia": 0,
    "Wisconsin": 0,
    "Wyoming": 0
}

from collections import defaultdict
cache = defaultdict(int)
final_arr = []

def read_data(file_path):
    # read the data
    with open(file_path, 'r') as file:
        properties = json.load(file)['properties']
    
    for property in properties:
        if property['country_code'] == 'us':
            if 'state' in property:
                cache[ (property['lat_y'], property['long_x']) ] = property['state']
        else:
            continue

read_data(src_file_path)

import requests
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


def fill_missing_states(input_file, dest_file_path):
    final_arr = []
    with open(input_file, 'r', encoding='utf-8') as file:
        properties = json.load(file)['properties']
        print(len(properties))

        for i, property in enumerate(properties):
            if i < 40001:
                continue
            print(f'on: {i}')

            if property['country_code'] == 'us':
                if 'state' in property:
                    final_arr.append(property)
                if 'state' not in property:
                    lat, long = property['lat_y'], property['long_x']
                    if (lat, long) in cache:
                        property['state'] = cache[(lat, long)]
                    else:
                        data = reverse_geocode(lat, long)
                        print('getting new data')
                        state = None
                        state_code = None

                        if 'address' in data:
                            if 'state' in data['address']:
                                state = data['address']['state']
                                property['state'] = state
                            if 'state_code' in data['address']:
                                state_code = data['address']['state_code']
                                property['state_code'] = state_code

                        cache[(lat, long)] = state
                        time.sleep(0.5)  # Increased to avoid rate limiting
                        final_arr.append(property)

                cache[ (property['lat_y'], property['long_x']) ] = property['state']
            else:
                final_arr.append(property)

            if i != 0 and i % 10000 == 0:  # Flush every `items_per_page` items
                with open(dest_file_path, 'a', encoding='utf-8') as dest_file:
                    json.dump(final_arr, dest_file, indent=2, ensure_ascii=False)
                    file.flush()
                    final_arr = []  # Reset the list to avoid duplicating entries
                    print('flushed at: ', i)

        if final_arr:
            with open(dest_file_path, 'a', encoding='utf-8') as dest_file:
                json.dump(final_arr, dest_file, indent=2, ensure_ascii=False)
                file.flush()
            
fill_missing_states(src_file_path, dest_file_path)
