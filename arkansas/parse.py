'''
arkansas/parse.py

Parses Arkansas voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 1
# first_name = 9
# middle_name = 10
# last_name = 8
# birth_date = 5
# gender = NA
# turnout2008 = 150 [if not empty]
# turnout2010 = 162 [if not empty]
# turnout2012 = 194 [if not empty]
# turnout2014 = NA
# party_affiliation_2008 = 148
# party_affiliation_2010 = 156
# party_affiliation_2012 = 188
# party_affiliation_2014 = NA
# party_affiliation = 37
# residential_address = 12 to 21
# zipcode = 22

import csv

# voter file
vf = '/Volumes/tweets/voter-files/arkansas/VRVH.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/arkansas/'

# reading file
f = open(vf)
reader = csv.reader(f)
vars = reader.next()

# voters by county
counties = {}
for row in reader:
    counties[row[0]] = counties.get(row[0], 0) + 1

print counties

# {'Saline': 64582, 'Clark': 11845, 'Mississippi': 21296, 'Newton': 5833, 
# 'Jackson': 9925, 'Howard': 6471, 'Union': 25064, 'Carroll': 13992, 'Cross': 10438, 
# 'Montgomery': 5160, 'Pulaski': 220295, 'Phillips': 13566, 'Jefferson': 39891, 
# 'Crittenden': 27400, 'Stone': 7563, 'White': 39046, 'Crawford': 28451, 
# 'Faulkner': 66291, 'Independence': 19696, 'Lafayette': 4422, 'Bradley': 5105,
# 'Ouachita': 16342, 'Lee': 5074, 'Garland': 60265, 'Lawrence': 8284, 'Grant': 9332,
# 'Van Buren': 8940, 'Miller': 21708, 'Drew': 9740, 'Marion': 9528, 'Cleburne': 17269,
# 'Izard': 7227, 'Little River': 6692, 'Pike': 5414, 'Poinsett': 12279, 'Ashley': 11314,
# 'Sevier': 6316, 'Johnson': 12089, 'Hot Spring': 18310, 'Dallas': 4553, 'Benton': 117714,
# 'Calhoun': 3644, 'Greene': 19082, 'Searcy': 5293, 'Perry': 5952, 'Franklin': 9554,
# 'Boone': 21269, 'Clay': 9367, 'Columbia': 12684, 'Yell': 9149, 'Sebastian': 71049,
# 'Arkansas': 9753, 'Fulton': 6976, 'Baxter': 28415, 'Woodruff': 4151, 'Madison': 8887,
# 'Lincoln': 5915, 'Lonoke': 37142, 'Hempstead': 10311, 'Pope': 30069, 'Conway': 10741,
# 'Randolph': 9511, 'St. Francis': 13313, 'Craighead': 50509, 'Washington': 103672,
# 'Desha': 7386, 'Logan': 11151, 'Prairie': 4548, 'Scott': 5238, 'Cleveland': 4807,
# 'Sharp': 10775, 'Chicot': 6201, 'Nevada': 5162, 'Polk': 10805, 'Monroe': 4734}

print(str(len(counties)) + ' counties')
# 75 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 1581937 registered voters

# preparing empty files by county
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# extracting voter variables into dict
f = open(vf)
reader = csv.reader(f)
vars = reader.next()
i = 0
data = {}
for county in counties:
    data[county] = []

for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    address = row[12] + ' ' + row[13] + ' ' + row[14] + ' ' + \
        row[15] + ' ' + row[16] + ' ' + row[17] + ' ' + \
        row[18] + ' ' + row[19] + ' ' + row[20] + ' ' + row[21]
    values = [row[1], row[9], row[10], row[8], row[5], "NA", \
        1 if row[150] != '' else 0, 1 if row[162] != '' else 0, \
        1 if row[195] != '' else 0, 'NA', \
        row[148], row[156], row[188], "NA", row[37], address, row[22]]
    county = row[0]
    data[county].append(values)
   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


