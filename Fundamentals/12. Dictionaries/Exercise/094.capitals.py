country = input().split(", ")
capital = input().split(", ")
dict = {country: capital for country, capital in zip(country, capital)}
for country, capital in dict.items():
    print(f"{country} -> {capital}")