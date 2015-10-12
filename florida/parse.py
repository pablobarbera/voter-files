'''
florida/parse.py

Parses Florida voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode", "race"]

# correspondence of variables (0-index variables)
# voter_id = 1
# first_name = 4
# middle_name = 5
# last_name = 2
# birth_date = 21
# gender = 19
# turnout2008 = '11/04/2008' in votes
# turnout2010 = '11/02/2010' in votes
# turnout2012 = '11/06/2012' in votes
# turnout2014 = '11/04/2014' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 23
# residential_address = 7 + 9
# zipcode = 11
# race = 20

# voter file(s)
import os
vfsf = '/Volumes/tweets/voter-files/florida/20150831/'
vhs = '/Volumes/tweets/voter-files/florida/Volumes/Sep 21 2015/Voter History/VoterHistory/'
vfs = os.listdir(vfsf)
vfs = [f for f in vfs if 'txt' in f]

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/florida/'

county_keys = {}
county_keys["ALA"] = "Alachua"
county_keys["BAK"] = "Baker"
county_keys["BAY"] = "Bay"
county_keys["BRA"] = "Bradford"
county_keys["BRE"] = "Brevard"
county_keys["BRO"] = "Broward"
county_keys["CAL"] = "Calhoun"
county_keys["CHA"] = "Charlotte"
county_keys["CIT"] = "Citrus"
county_keys["CLA"] = "Clay"
county_keys["CLL"] = "Collier"
county_keys["CLM"] = "Columbia"
county_keys["DAD"] = "Miami-Dade"
county_keys["DES"] = "Desoto"
county_keys["DIX"] = "Dixie"
county_keys["DUV"] = "Duval"
county_keys["ESC"] = "Escambia"
county_keys["FLA"] = "Flagler"
county_keys["FRA"] = "Franklin"
county_keys["GAD"] = "Gadsden"
county_keys["GIL"] = "Gilchrist"
county_keys["GLA"] = "Glades"
county_keys["GUL"] = "Gulf"
county_keys["HAM"] = "Hamilton"
county_keys["HAR"] = "Hardee"
county_keys["HEN"] = "Hendry"
county_keys["HER"] = "Hernando"
county_keys["HIG"] = "Highlands"
county_keys["HIL"] = "Hillsborough"
county_keys["HOL"] = "Holmes"
county_keys["IND"] = "Indian River"
county_keys["JAC"] = "Jackson"
county_keys["JEF"] = "Jefferson"
county_keys["LAF"] = "Lafayette"
county_keys["LAK"] = "Lake"
county_keys["LEE"] = "Lee"
county_keys["LEO"] = "Leon"
county_keys["LEV"] = "Levy"
county_keys["LIB"] = "Liberty"
county_keys["MAD"] = "Madison"
county_keys["MAN"] = "Manatee"
county_keys["MRN"] = "Marion"
county_keys["MRT"] = "Martin"
county_keys["MON"] = "Monroe"
county_keys["NAS"] = "Nassau"
county_keys["OKA"] = "Okaloosa"
county_keys["OKE"] = "Okeechobee"
county_keys["ORA"] = "Orange"
county_keys["OSC"] = "Osceola"
county_keys["PAL"] = "Palm Beach"
county_keys["PAS"] = "Pasco"
county_keys["PIN"] = "Pinellas"
county_keys["POL"] = "Polk"
county_keys["PUT"] = "Putnam"
county_keys["SAN"] = "Santa Rosa"
county_keys["SAR"] = "Sarasota"
county_keys["SEM"] = "Seminole"
county_keys["STJ"] = "St. Johns"
county_keys["STL"] = "St. Lucie"
county_keys["SUM"] = "Sumter"
county_keys["SUW"] = "Suwannee"
county_keys["TAY"] = "Taylor"
county_keys["UNI"] = "Union"
county_keys["VOL"] = "Volusia"
county_keys["WAK"] = "Wakulla"
county_keys["WAL"] = "Walton"
county_keys["WAS"] = "Washington"

# voters by county
counties = {}
for vf in vfs:
    f = open(vfsf + vf)
    county = county_keys[vf[0:3]]
    print county
    for line in f:
        counties[county] = counties.get(county, 0) + 1

print counties

# {'Alachua': 176816, 'Osceola': 195321, 'Okaloosa': 146488, 'Jackson': 29796,
# 'Seminole': 280778, 'Gulf': 9841, 'Lake': 222666, 'Volusia': 358244, 'Duval': 604686,
# 'Sumter': 87885, 'Calhoun': 8568, 'Liberty': 4620, 'Hillsborough': 834029,
# 'Orange': 793743, 'Brevard': 416097, 'Miami-Dade': 1390651, 'Santa Rosa': 132216,
# 'Flagler': 79920, 'Desoto': 16244, 'Pasco': 336132, 'Indian River': 102990,
# 'Levy': 26869, 'Columbia': 39060, 'Lee': 448963, 'Walton': 44070, 'Citrus': 105755,
# 'Martin': 113247, 'Okeechobee': 20124, 'Manatee': 230622, 'Union': 7224,
# 'Hernando': 133122, 'Hamilton': 8161, 'Nassau': 59384, 'Broward': 1227203,
# 'Putnam': 46648, 'St. Lucie': 193164, 'Bradford': 15962, 'Hendry': 18574,
# 'Highlands': 66507, 'Gadsden': 30020, 'Baker': 14565, 'Bay': 123860,
# 'Wakulla': 19611, 'Gilchrist': 11137, 'Taylor': 12719, 'Glades': 7027,
# 'Franklin': 7586, 'Pinellas': 679125, 'Clay': 146304, 'Hardee': 12673,
# 'Holmes': 11465, 'Charlotte': 128812, 'Madison': 12185, 'Palm Beach': 925191,
# 'Dixie': 9993, 'Polk': 393073, 'Washington': 15340, 'St. Johns': 175864,
# 'Leon': 203567, 'Sarasota': 299577, 'Jefferson': 9575, 'Marion': 238744,
# 'Suwannee': 26012, 'Escambia': 213691, 'Collier': 213942, 'Lafayette': 4530, 'Monroe': 58614}

print(str(len(counties)) + ' counties')
# 67 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 13037192 registered voters

# preparing empty files by county
import csv
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# extracting voter variables into dict
import csv
i = 0

for vf in vfs:
    county = county_keys[vf[0:3]]
    print county
    voters = {}
    # preparing dict with vote history
    f = open(vhs + vf[0:4] + 'H_20150904.txt')
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if row[4] is not 'N':
            try:
                voters[row[1]].append(row[2])
            except:
                voters[row[1]] = []
                voters[row[1]].append(row[2])
    # reading voter history
    f = open(vfsf + vf)    
    data = {}
    data[county] = []
    reader = csv.reader(f, delimiter="\t")
    vars = reader.next()
    for row in reader:
        i += 1
        if i % 100000 == 0:
            print str(i) + '/13037192'
        try:
            votes = voters[row[1]]
        except:
            votes = []
        turnout2008 = 1 if '11/04/2008' in votes else 0
        turnout2010 = 1 if '11/02/2010' in votes else 0
        turnout2012 = 1 if '11/06/2012' in votes else 0
        turnout2014 = 1 if '11/04/2014' in votes else 0
        address = row[7].strip() + ' ' + row[8].strip() + ' ' + row[9].strip()
        values = [row[1], row[4], row[5], row[2], row[21], row[19],
            turnout2008, turnout2010, turnout2012, turnout2014,
            "NA", "NA", "NA", "NA", row[23].strip(), address, row[11], row[20]]
        data[county].append(values)
        # writing to disk
        outf = open(outfolder + county + '.csv', 'a')
        out = csv.writer(outf, delimiter=',', quotechar='"')
        for row in data[county]:
            out.writerow(row)
        outf.close()
        data[county] = []


