'''
rhode_island/parse.py

Parses Rhode Island voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 0
# first_name = 3
# middle_name = 4
# last_name = 2
# birth_date = 37
# gender = 34
# turnout2008 = NA
# turnout2010 = NA
# turnout2012 = NA
# turnout2014 = NA
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 30
# residential_address = 7 + 8 + 9 + 12 + 16
# zipcode = 10

import csv

# voter file
vf = '/Volumes/tweets/voter-files/rhode_island/2015-01.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/rhode_island/'

towns = {}
towns["BARRINGTON"] = "BRISTOL"
towns["BRISTOL"] = "BRISTOL"
towns["BURRILLVILLE"] = "PROVIDENCE"
towns["CENTRAL FALLS"] = "PROVIDENCE"
towns["CHARLESTOWN"] = "WASHINGTON"
towns["COVENTRY"] = "KENT"
towns["CRANSTON"] = "PROVIDENCE"
towns["CUMBERLAND"] = "PROVIDENCE"
towns["EAST GREENWICH"] = "KENT"
towns["EAST PROVIDENCE"] = "PROVIDENCE"
towns["EXETER"] = "WASHINGTON"
towns["FOSTER"] = "PROVIDENCE"
towns["GLOCESTER"] = "PROVIDENCE"
towns["HOPKINTON"] = "WASHINGTON"
towns["JAMESTOWN"] = "NEWPORT"
towns["JOHNSTON"] = "PROVIDENCE"
towns["LINCOLN"] = "PROVIDENCE"
towns["LITTLE COMPTON"] = "NEWPORT"
towns["MIDDLETOWN"] = "NEWPORT"
towns["NARRAGANSETT"] = "WASHINGTON"
towns["NEW SHOREHAM"] = "WASHINGTON"
towns["NEWPORT"] = "NEWPORT"
towns["NORTH KINGSTOWN"] = "WASHINGTON"
towns["NORTH PROVIDENCE"] = "PROVIDENCE"
towns["NORTH SMITHFIELD"] = "PROVIDENCE"
towns["PAWTUCKET"] = "PROVIDENCE"
towns["PORTSMOUTH"] = "NEWPORT"
towns["PROVIDENCE"] = "PROVIDENCE"
towns["RICHMOND"] = "WASHINGTON"
towns["SCITUATE"] = "PROVIDENCE"
towns["SMITHFIELD"] = "PROVIDENCE"
towns["SOUTH KINGSTOWN"] = "WASHINGTON"
towns["TIVERTON"] = "NEWPORT"
towns["WARREN"] = "BRISTOL"
towns["WARWICK"] = "KENT"
towns["WEST GREENWICH"] = "KENT"
towns["WEST WARWICK"] = "KENT"
towns["WESTERLY"] = "WASHINGTON"
towns["WOONSOCKET"] = "PROVIDENCE"

# reading file
f = open(vf)
reader = csv.reader(f, delimiter="|")
vars = reader.next()
vars = reader.next()

# voters by county
counties = {}
for row in reader:
    county = towns[row[12]]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'PROVIDENCE': 424600, 'NEWPORT': 58302,
#  'WASHINGTON': 98022, 'KENT': 121938, 'BRISTOL': 37183}

print(str(len(counties)) + ' counties')
# 5 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 740,045 registered voters

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
vars = reader.next()

i = 0
data = {}
for county in counties:
    data[county] = []

for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    address = " ".join([row[7], row[8], row[9], row[12], row[16]])
    values = [row[0], row[3], row[4], row[2], row[37], row[34],
        "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA",
        row[30], address, row[10]]
    county = towns[row[12]]
    data[county].append(values)
   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


