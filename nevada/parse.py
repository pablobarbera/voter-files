'''
nevada/parse.py

Parses Nevada voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (position in line; note 0-indexed)
# voter_id = 0
# first_name = 2
# middle_name = 3
# last_name = 4
# birth_date = 5
# gender = NA
# turnout2008 = '11/04/2008' in votes
# turnout2010 = '11/02/2010' in votes
# turnout2012 = '11/06/2012' in votes
# turnout2014 = '11/04/2014' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 12
# residential_address = 7 + 8 + 9 + 10
# zipcode = 11


# voter file(s)
vf = '/Volumes/tweets/voter-files/nevada/VoterList.36170.092815105940/VoterList.ElgbVtr.36170.092815105940.txt'
vh = '/Volumes/tweets/voter-files/nevada/VoterList.36170.092815105940/VoterList.VtHst.36170.092815105940.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/nevada/'

# voters by county
import csv
counties = {}
f = open(vf)
reader = csv.reader(f)
for row in reader:
    county = row[1]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'Carson City': 27268, 'White Pine': 4572, 'Lincoln': 2935,
# 'Churchill': 12914, 'Lander': 2787, 'Humboldt': 7456, 'Clark': 996027,
# 'Esmeralda': 562, 'Elko': 21552, 'Lyon': 32522, 'Douglas': 31848,
# 'Eureka': 921, 'Washoe': 262968, 'Storey': 2832, 'Nye': 26446,
# 'Pershing': 2480, 'Mineral': 2860}

print(str(len(counties)) + ' counties')
# 17 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 1438950 registered voters

# preparing empty files by county
import csv
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# preparing dict with vote history
f = open(vh)
reader = csv.reader(f)
voters = {}
i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/6257535'
    voterid = row[1]
    elec = row[2]
    if elec in ['11/04/2008', '11/02/2010', '11/06/2012', '11/04/2014']:
        try:
            voters[voterid].append(elec)
        except:
            voters[voterid] = []
            voters[voterid].append(elec)


# reading voter history
f = open(vf) 
reader = csv.reader(f)   
data = {}
for county in counties:
    data[county] = []

i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/1438950'
    voterid = row[0]
    try:
        votes = voters[voterid]
    except:
        votes = []
    turnout2008 = 1 if '11/04/2008' in votes else 0
    turnout2010 = 1 if '11/02/2010' in votes else 0
    turnout2012 = 1 if '11/06/2012' in votes else 0
    turnout2014 = 1 if '11/04/2014' in votes else 0
    address = row[7] + ' ' + row[8] + ' ' + row[9] + ' ' + row[10]
    values = [voterid, row[2], row[3], row[4], row[5], "NA", 
        turnout2008, turnout2010, turnout2012, turnout2014,
        "NA", "NA", "NA", "NA", row[12], address, row[11]]
    county = row[1]
    data[county].append(values)

# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()
    data[county] = []


