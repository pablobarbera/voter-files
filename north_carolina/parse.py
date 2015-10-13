'''
north_carolina/parse.py

Parses North Carolina voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode", "race", "ethnicity"]

# correspondence of variables (position in line; note 0-indexed)
# voter_id = 67
# first_name = 10
# middle_name = 11
# last_name = 9
# birth_date = 2013 - [29]
# gender = 28
# turnout2008 = '11/04/2008' in votes
# turnout2010 = '11/02/2010' in votes
# turnout2012 = '11/06/2012' in votes
# turnout2014 = NA
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 27
# residential_address = 13 + 14 + 15
# zipcode = 16
# race = 25
# ethnicity = 26


# voter file(s)
vf = '/Volumes/tweets/voter-files/north_carolina/voter-file.csv'
vh = '/Volumes/tweets/voter-files/north_carolina/voter-history.csv'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/north_carolina/'

# voters by county
import csv
counties = {}
f = open(vf)
reader = csv.reader(f)
vars = reader.next()
for row in reader:
    county = row[1]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'CHOWAN': 11855, 'COLUMBUS': 41795, 'CURRITUCK': 19532, 'GASTON': 145449,
# 'FORSYTH': 274766, 'BUNCOMBE': 208197, 'HARNETT': 76233, 'DAVIE': 31195,
# 'BERTIE': 16419, 'CABARRUS': 130400, 'HYDE': 4014, 'HERTFORD': 17097,
# 'CALDWELL': 58237, 'JACKSON': 30630, 'MACON': 28499, 'BRUNSWICK': 92329,
# 'GRAHAM': 7416, 'DARE': 31508, 'CASWELL': 17321, 'GATES': 9077,
# 'BLADEN': 25621, 'MCDOWELL': 31352, 'CUMBERLAND': 235487, 'LENOIR': 44356,
# 'POLK': 17768, 'ONSLOW': 105394, 'HOKE': 32232, 'PITT': 128558,
# 'PAMLICO': 10926, 'MONTGOMERY': 18521, 'GREENE': 12637, 'ANSON': 19048,
# 'PENDER': 40644, 'BEAUFORT': 36779, 'CLAY': 10029, 'CARTERET': 57184,
# 'HALIFAX': 42448, 'CHATHAM': 51577, 'MITCHELL': 13311, 'ORANGE': 125988,
# 'JONES': 8563, 'LINCOLN': 57387, 'MOORE': 72882, 'ALAMANCE': 106064,
# 'PERSON': 28561, 'EDGECOMBE': 43881, 'MARTIN': 20138, 'GUILFORD': 393752,
# 'HAYWOOD': 47706, 'RANDOLPH': 21273, 'IREDELL': 120037, 'DUPLIN': 32992,
# 'DURHAM': 235611, 'CAMDEN': 8052, 'ALLEGHANY': 8266, 'GRANVILLE': 40262,
# 'PERQUIMANS': 10959, 'MECKLENBURG': 722603, 'NEW HANOVER': 177828,
# 'BURKE': 64064, 'HENDERSON': 87411, 'MADISON': 18423, 'PASQUOTANK': 32394,
# 'LEE': 38463, 'AVERY': 13585, 'ASHE': 20794, 'NORTHAMPTON': 17288,
# 'CRAVEN': 78858, 'CHEROKEE': 23638, 'FRANKLIN': 43981, 'CLEVELAND': 69751,
# 'CATAWBA': 113762, 'JOHNSTON': 119677, 'NASH': 75234, 'DAVIDSON': 114237,
# 'ALEXANDER': 26823}

print(str(len(counties)) + ' counties')
# 76 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 5427029 registered voters

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
vars = reader.next()
voters = {}
i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/28422832'
    voterid = row[10]
    elec = row[3]
    if elec in ['11/04/2008', '11/02/2010', '11/06/2012']:
        try:
            voters[voterid].append(elec)
        except:
            voters[voterid] = []
            voters[voterid].append(elec)

# reading voter history
f = open(vf) 
reader = csv.reader(f)  
vars = reader.next() 
data = {}
for county in counties:
    data[county] = []

i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/5427029'
    voterid = row[67]
    try:
        votes = voters[voterid]
    except:
        votes = []
    turnout2008 = 1 if '11/04/2008' in votes else 0
    turnout2010 = 1 if '11/02/2010' in votes else 0
    turnout2012 = 1 if '11/06/2012' in votes else 0
    turnout2014 = 1 if '11/04/2014' in votes else 0
    address = row[13] + ' ' + row[14] + ' ' + row[15]
    values = [voterid, row[10], row[11], row[9], str(2013 - int(row[29])), 
        row[28], turnout2008, turnout2010, turnout2012, "NA",
        "NA", "NA", "NA", "NA", row[27], address, row[16],
        row[25], row[26]]
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


