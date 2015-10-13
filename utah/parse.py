'''
utah/parse.py

Parses Utah voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 0
# first_name = 2
# middle_name = 3
# last_name = 1
# birth_date = 26
# gender = NA
# turnout2008 = if [82] != ""
# turnout2010 = if [86] != ""
# turnout2012 = if [90] != ""
# turnout2014 = NA
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 10
# residential_address = 16 + 17 + 18 + 19 + 20 + 21 + 24 + ' UT'
# zipcode = 25

import csv

# voter file
vf = '/Volumes/tweets/voter-files/utah/voters.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/utah/'

# reading file
f = open(vf)
reader = csv.reader(f)
vars = reader.next()

# voters by county
counties = {}
for row in reader:
    county = row[14]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'San Juan': 9611, 'Iron': 24973, 'Wasatch': 16288, 'Sevier': 10758,
# 'Millard': 6278, 'Cache': 67260, 'Wayne': 1806, 'Rich': 1307,
# 'Grand': 6860, 'Weber': 112401, 'Juab': 5885, 'Tooele': 29302,
# 'Utah': 260487, 'Sanpete': 12534, 'Carbon': 13746, 'Piute': 977,
# 'Emery': 7575, 'Duchesne': 8984, 'Morgan': 5687, 'Davis': 170319,
# 'Daggett': 851, 'Kane': 4258, 'Washington': 74447, 'Garfield': 3050,
# 'Summit': 26578, 'Salt Lake': 547822, 'Beaver': 3668, 'Uintah': 19211,
# 'Box Elder': 28553}

print(str(len(counties)) + ' counties')
# 29 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 1,481,476 registered voters

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
    address = " ".join([row[16], row[17], row[18], row[19],
        row[20], row[21], row[24], 'UT'])
    try:
        turnout2008 = 1 if row[82] != "" else 0
    except:
        turnout2008 = 0
    try:
        turnout2010 = 1 if row[86] != "" else 0
    except:
        turnout2010 = 0
    try:
        turnout2012 = 1 if row[90] != "" else 0
    except:
        turnout2012 = 0
    values = [row[0], row[2], row[3], row[1], row[26], "NA",
        turnout2008, turnout2010, turnout2012,
        "NA", "NA", "NA", "NA", "NA",
        row[10], address, row[25]]
    county = row[14]
    data[county].append(values)
   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


