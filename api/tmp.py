
file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson_with_country.json'
file_path = '/Users/yoon/Desktop/general_code/frontend/my-app/api/final_geojson_with_country.json'
import json
start_strings = [
    'created_at',
    "created_at", 
    "created_at", 
    "display",
    "permalink",
    "lat_y",
    'ng_x',
    "score",
    "country",
    "country_code",
    "state",
    "id",
    "title"
    ]
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
d = defaultdict(int)


def fill_missing_states(data):
    # Create a dictionary mapping (latitude, longitude) to state
    lat_lon_to_state = {}
    for item in data:
        if 'state' in item and item['state']:
            lat_lon_to_state[(item['lat_y'], item['long_x'])] = item['state']

    # Fill in missing state values
    for item in data:
        if 'state' not in item or not item['state']:
            state = lat_lon_to_state.get((item['lat_y'], item['long_x']), None)
            if state:
                item['state'] = state

    return data


print(continent_to_country_codes)
def check_and_print_lines(file_path):
    # List of strings to check at the beginning of the line
    # start_strings = ["ceated_at", "display"]

    with open(file_path, 'r') as file:
        data = json.load(file)

        print(len(data['properties']))
        for property in data['properties']:
            # print(property['country_code'])
            for k, v in continent_to_country_codes.items():
                if property['country_code'] in v:
                    d[k] += 1
                    continue
                
check_and_print_lines('/Users/yoon/Desktop/general_code/frontend/my-app/api/geojson_with_country.json')
print(d)


        # second_prev_line = ""
        # prev_line = ""
        # for i, line in enumerate(file):
        #     if i==300000:
        #         break
        #     stripped_line = line.strip()
        #     prev_stripped_line = prev_line.strip()
        #     second_prev_stripped_line = second_prev_line.strip()


        #     # Check if the line starts with any of the specified strings
        #     # if any(stripped_line.startswith(s) for s in start_strings):
        #     if any(s in stripped_line for s in start_strings):
        #         # print("JIWEOF")
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue

        #     # Check if the second previous line was "}", the previous line is "," and the current line isn't "{"
        #     if second_prev_stripped_line == "}" and prev_stripped_line == "," and stripped_line == "{":
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue
        #         # print(line, end='')
        #     if prev_stripped_line == "}" and stripped_line == ",":
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue

        #     # Check if the line matches specific patterns to ignore
        #     if (prev_stripped_line == "}," or prev_stripped_line == "},\n" or prev_stripped_line == "}\n,{"):
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue
            
        #     if prev_stripped_line == '},' and stripped_line == '{':
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue

        #     if stripped_line == '},' and any(s in prev_stripped_line for s in start_strings):
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue

        #     if stripped_line == '}' and any(s in prev_stripped_line for s in start_strings):
        #         second_prev_line = prev_line
        #         prev_line = line
        #         continue

        #     # Print the line if it does not meet the above conditions
        #     print('bad:', stripped_line)
        #     print(f'line number: {i}')
        #     print('========================')
        #     # Update the previous lines
        #     second_prev_line = prev_line
        #     prev_line = line

t = '    "created_at": 1298816706,'.strip()
# print(any(s in '"long_x": -87.7309534' for s in start_strings))
# Specify the path to your large JSON file
check_and_print_lines(file_path)