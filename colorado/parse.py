'''
colorado/parse.py

Parses Colorado voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 0
# first_name = 4
# middle_name = 5
# last_name = 3
# birth_date = 29
# gender = 30
# turnout2008 = NA
# turnout2010 = NA
# turnout2012 = NA
# turnout2014 = NA
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 34
# residential_address = 20
# zipcode = 23

import csv

# voter file(s)
# [first put them all together]
# cat Registered_Voters_List_\ Part* > colorado-voter-file.txt
vf = '/Volumes/tweets/voter-files/colorado/colorado-voter-file.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/colorado/'

# reading file
f = open(vf)
reader = csv.reader(f, delimiter="|")
vars = reader.next()

# voters by county
counties = {}
for row in reader:
    counties[row[2]] = counties.get(row[2], 0) + 1

print counties

#{'San Juan': 724, 'San Miguel': 5721, 'Otero': 10949, 'Gilpin': 4674,
# 'Jackson': 1160, 'Chaffee': 13335, 'Elbert': 17654, 'Park': 12736,
# 'Gunnison': 11505, 'Lake': 5055, 'Douglas': 216521, 'Moffat': 9450,
# 'Phillips': 3128, 'Jefferson': 393003, 'Cheyenne': 1385, 'Grand': 10786,
# 'Mineral': 810, 'Boulder': 240788, 'Archuleta': 9872, 'La Plata': 40024,
# 'Custer': 3410, 'Clear Creek': 7387, 'Montrose': 24838, 'Fremont': 27551,
# 'Saguache': 4237, 'Kit Carson': 4741, 'El Paso': 413333, 'Kiowa': 998,
# 'Costilla': 2731, 'Delta': 20249, 'Conejos': 5598, 'Arapahoe': 378183,
# 'Mesa': 107171, 'Yuma': 5968, 'Teller': 17555, 'Broomfield': 42764,
# 'Pueblo': 105284, 'Lincoln': 2968, 'Alamosa': 8787, 'Weld': 156086,
# 'Adams': 238482, 'Montezuma': 18449, 'Dolores': 1619, 'Washington': 3140,
# 'Logan': 12387, 'Summit': 24445, 'Denver': 469135, 'Morgan': 14333,
# 'Hinsdale': 670, 'Sedgwick': 1668, 'Routt': 18052, 'Huerfano': 4613,
# 'Rio Blanco': 4320, 'Bent': 2719, 'Baca': 2696, 'Pitkin': 14051,
# 'Prowers': 6775, 'Ouray': 4091, 'Crowley': 1980, 'Rio Grande': 7631,
# 'Eagle': 30739, 'Garfield': 31434, 'Larimer': 227955, 'Las Animas': 9597}

print(str(len(counties)) + ' counties')
# 64 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 3500100 registered voters

# preparing empty files by county
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# extracting voter variables into dict
f = open(vf)
reader = csv.reader(f, delimiter="|")
vars = reader.next()
i = 0
data = {}
for county in counties:
    data[county] = []

for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    values = [row[0], row[4], row[5], row[3], row[29], row[30], \
        "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", \
        row[34], row[20], row[23]]
    county = row[2]
    data[county].append(values)

  
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()


