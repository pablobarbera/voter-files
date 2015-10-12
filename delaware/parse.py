'''
delaware/parse.py

Parses Delaware voter file into csv files, one per county,
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
# birth_date = 5
# gender = NA
# turnout2008 = if '2008' in votes
# turnout2010 = if '2010' in votes
# turnout2012 = if '2012' in votes
# turnout2014 = if '2014' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 20
# residential_address = 6 + 7 + 8 + 9 + 10
# zipcode = 11

import csv

# voter file
vf = '/Volumes/tweets/voter-files/delaware/ActiveReg.csv'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/delaware/'

# reading file
f = open(vf)
reader = csv.reader(f)
vars = reader.next()

# voters by county
counties = {}
for row in reader:
    if row[12] == 'S':
        county = 'Sussex'
    if row[12] == 'K':
        county = 'Kent'
    if row[12] == 'N':
        county = 'New Castle'
    counties[county] = counties.get(county, 0) + 1


print counties

# {'New Castle': 386624, 'Sussex': 144608, 'Kent': 114094}

print(str(len(counties)) + ' counties')
# 3 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 645,326 registered voters

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
    address = " ".join(row[6:10])
    votes = row[27:32]
    values = [row[0], row[2], row[3], row[1], row[5], "NA", \
        1 if '2008' in votes else 0, 1 if '2010' in votes else 0,
        1 if '2012' in votes else 0, 1 if '2014' in votes else 0,
        "NA", "NA", "NA", "NA", row[20], address, row[11]]
    if row[12] == 'S':
        county = 'Sussex'
    if row[12] == 'K':
        county = 'Kent'
    if row[12] == 'N':
        county = 'New Castle'
    data[county].append(values)
   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


