import csv
import json

import time

#turns the csv into a list of lists [[x, y, z,], [a, b, c]
exampleFile = open('dashboardinput.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

#list to hold the list of dictionaries
jsonList = []

#######IF YOU NEED TO ADD A NEW CATEGORY#######
#add it as a variable in the block around line 25
#add it to the end of the dictionary tied to "subDict['freq'] = ...."

#this takes the headers in the first rows and turns them into variables to be inserted into the json
#the reason for this is so that the key in the json always matches the title of the category in the csv even if we decide to change the title in the json later
#if we were not worried about the titles changing we woud have just hard coded them

#this entry is the origin/country/province
csv_type = exampleData[0][0]

#the rest of these variables more or less match their categories
#if you end up adding a column you'll want to add it here
aging = exampleData[0][1]
agriculture = exampleData[0][2]
animal_protection = exampleData[0][3]
arts_and_culture = exampleData[0][4]
civil_society_cap_build = exampleData[0][5]
disabilities = exampleData[0][6]
disaster_relief = exampleData[0][7]
econ_dev = exampleData[0][8]
edu = exampleData[0][9]
energy = exampleData[0][10]
environ = exampleData[0][11]
ethnic_affair = exampleData[0][12]
gender_issues = exampleData[0][13]
health = exampleData[0][14]
infrastructure = exampleData[0][15]
int_relations = exampleData[0][16]
labor = exampleData[0][17]
law_governance = exampleData[0][18]
lgbtq = exampleData[0][19]
media = exampleData[0][20]
migrants = exampleData[0][21]
poverty = exampleData[0][22]
religion = exampleData[0][23]
rural = exampleData[0][24]
sport = exampleData[0][25]
tech = exampleData[0][26]
tourism = exampleData[0][27]
trade = exampleData[0][28]
urban = exampleData[0][29]
youth = exampleData[0][30]

#removd the header row for the looping that follows
del exampleData[0]


#creates the json
for row in exampleData:
    #this is the dict for the entry
    subDict = {}

    #the structure for the file is '{province: beijing, freq: {dic of all the things}}

    #so the first entry is the provience and the location
    subDict[csv_type] = row[0]
    #and then the second entry maps a huge number of things in a dict to 'freq'
    subDict['freq'] = {aging: int(row[1]), agriculture: int(row[2]), animal_protection: int(row[3]), arts_and_culture: int(row[4]), civil_society_cap_build: int(row[5]), disabilities: int(row[6]), disaster_relief: int(row[7]), econ_dev: int(row[8]), edu: int(row[9]), energy: int(row[10]), environ: int(row[11]), ethnic_affair: int(row[12]), gender_issues: int(row[13]), health: int(row[14]), infrastructure: int(row[15]), int_relations: int(row[16]), labor: int(row[17]), law_governance: int(row[18]), lgbtq: int(row[19]), media: int(row[20]), migrants: int(row[21]), poverty: int(row[22]), religion: int(row[23]), rural: int(row[24]), sport: int(row[25]), tech: int(row[26]), tourism: int(row[27]), trade: int(row[28]), urban: int(row[29]), youth: int(row[30])}

    #once the entry for this entry is complete, add it to the json
    jsonList.append(subDict)



#print(jsonList)

#writes the json
with open('dashboardoutput.json', 'w') as outfile:
    json.dump(jsonList, outfile)
