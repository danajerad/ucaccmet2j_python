import json

with open('ucaccmet2j_python/precipitation.json', 'r', encoding='utf-8') as file:
    content = json.load(file)


cities = {"Cinicinnati, Seattle, Maui, San Diego"}.split()

for city in cities:
    if city['date'].startswith(f"2010-{month}"):
        pre_permonth[month] += item['value']


Cincinnati,OH,GHCND:USW00093814
Seattle,WA,GHCND:US1WAKG0038
Maui,HI,GHCND:USC00513317
San Diego,CA,GHCND:US1CASD0032

