import json
from datetime import date

with open('ucaccmet2j_python/precipitation.json', 'r', encoding='utf-8') as file:
    content = json.load(file)


months = '01 02 03 04 05 06 07 08 09 10 11 12'.split()
pre_permonth = {}

for month in months: 
    pre_permonth[month] = 0 

print(pre_permonth)

for item in content:
    if item ['station'] == "GHCND:US1WAKG0038":
        #Originally I had this for getting the total precipiation of january 
        #split the date to 
        for month in months:
            if item['date'].startswith(f"2010-{month}"):
                pre_permonth[month] += item['value'] 




with open('results.json', 'w') as file:
    json.dump(pre_permonth, file, indent=4)