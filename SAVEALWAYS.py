import json
import csv

#this is for part 3 
with open('stations.csv') as file:
    stations_list = list(csv.DictReader(file))

with open('precipitation.json', 'r', encoding='utf-8') as file:
    content = json.load(file)


months = '01 02 03 04 05 06 07 08 09 10 11 12'.split()


#I need to get the for city in cities:
cities = {}
for station in stations_list:
    city = {}
    pre_permonth = {}

    relative= {}

    for month in months: 
        pre_permonth[month] = 0 
        relative[month] = 0 
    print(station["Station"])
    total = 0 
    for item in content:
        if item ['station'] == station["Station"]:
            #total 
            total += item["value"]
            for month in months: 
                if item['date'].startswith(f"2010-{month}"):
                    pre_permonth[month] += item['value']
        
    for month in pre_permonth:
        relative[month] = pre_permonth[month] / total 


# alternative way for the total: make a list (this works but it doesnt fit inside my for loop)
# totalpre = []
#for month in pre_permonth:
    #totalpre.append(pre_permonth[month])
    
#total = sum(totalpre)


    #here is my seattle dictionary which will print in the json file 
    city["pre_permonth"] = pre_permonth
    city["total_precipiation"] = total
    city["relative_precipitations"] = relative
    
    cities[station["Location"]] = city


with open('results.json', 'w') as file:
    json.dump(cities, file, indent=4)


#i really need this to remember to save, so this is very important
print("remember to save!")
