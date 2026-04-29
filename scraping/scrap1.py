from bs4 import BeautifulSoup as bs
import requests 
import csv
import pandas as pd

url="https://www.scrapethissite.com/pages/simple/"
response=requests.get(url)#collecting data from site
#print(response)

soup=bs(response.text)#defining soup
# print(type(soup))
# print(soup.find('title').text)#find text inside title tag
data=soup.find_all('div',class_="col-md-4 country")#find base4d in division
# print(data[:2])#print only first two contry
#country_1=data[0]#taking data from first country

country_list=[]

for country_1 in data: #printing all data

    country_name=country_1.find('h3',class_="country-name").text.strip()
    #print(country_name)#print first country name
    capital_name=country_1.find('span',class_="country-capital").text
    #print(capital_name)#print first country capital name
    population=country_1.find('span',class_="country-population").text
    #print(population)
    area=country_1.find('span',class_="country-area").text
    #print(area)
    country_list.append((country_name,capital_name,population,area))
    #print(country_list) #appending to list
#converting to csv
with open("countries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Capital", "Population", "Area"])
    writer.writerows(country_list)

df = pd.DataFrame(country_list, columns=["Country", "Capital", "Population", "Area"])
df["Population"] = pd.to_numeric(df["Population"])
df["Area"] = pd.to_numeric(df["Area"])#converting to numeric
#print(df)
print(df.head(5))#print first 5 raw
print("Total countries:", len(df))#finding total number of contries
print("Average population:" , df["Population"].mean())#average population
print(df[df["Population"] == df["Population"].max()]["Country"].values[0])#find maximum population
print(df[df["Population"] == df["Population"].min()]["Country"].values[0])#country with minimum poulation
print(df[df["Population"] > 50000000])#population>5million
df["Density"] = df["Population"] / df["Area"]# adding densirty column
print(df["Density"].describe())
print("Large countries:", len(df[df["Area"] > 1000000]))
