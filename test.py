import pandas as pd
import re
df = pd.read_csv('Result_13.csv')
# If you know the name of the column skip this
city = df.City
name = df.Name
street = df.Street
Name_list = []
Street_list = []
Zip_list = []
Address_lit = []
print(len(city))
for i in range(0, len(city)):
    Zip = re.findall(r'\d+', city[i])[0]
    Address = ''.join([i for i in city[i] if not i.isdigit()])
    Name_list.append(name[i])
    Street_list.append(street[i])
    Zip_list.append(Zip)
    Address_lit.append(Address)
    dict = {'Name': Name_list, 'Street': Street_list, 'Zip Code': Zip_list, 'Address': Address_lit}

    df = pd.DataFrame(dict)

    df.to_csv('Result.csv')