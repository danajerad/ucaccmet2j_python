import json
import csv
#intercity rains 

with open('ucaccmet2j_python/precipitation.json', 'r', encoding='utf-8') as file:
    content = json.load(file)

Seattle = {}

months = '01 02 03 04 05 06 07 08 09 10 11 12'.split()
pre_permonth = {}

relative= {}
total = 0 

for month in months: 
    pre_permonth[month] = 0 
    relative[month] = 0 

for item in content:
    if item ['station'] == "GHCND:US1WAKG0038":
            #total 
        total += item["value"]
        for month in months: 
            if item['date'].startswith(f"2010-{month}"):
                pre_permonth[month] += item['value']
            relative[month] = pre_permonth[month] / total 


# alternative way for the total: make a list (this works) 
# totalpre = []
#for month in pre_permonth:
    #totalpre.append(pre_permonth[month])
    
#total = sum(totalpre)



print("remember to save!")


Seattle["pre_permonth"] = pre_permonth
Seattle["total_precipiation"] = total
Seattle["relative_precipitations"] = relative

with open('results.json', 'w') as file:
    json.dump(Seattle, file, indent=4)