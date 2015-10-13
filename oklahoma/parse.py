'''
oklahoma/parse.py

Parses Oklahoma voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 5
# first_name = 2
# middle_name = 3
# last_name = 1
# birth_date = 15
# gender = NA
# turnout2008 = if '20081104' in votes
# turnout2010 = if '20101102' in votes
# turnout2012 = if '20121106' in votes
# turnout2014 = 'NA'
# party_affiliation_2008 = 'NA'
# party_affiliation_2010 = 'NA'
# party_affiliation_2012 = 'NA'
# party_affiliation_2014 = 'NA'
# party_affiliation = 6
# residential_address = 8 + 9 + 10 + 11 + 12 + 13 + 20
# zipcode = 14

import csv
import sys
csv.field_size_limit(sys.maxsize)

# voter file folder
vf = '/Volumes/tweets/voter-files/oklahoma/'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/oklahoma/'

county_keys = {}

county_keys["01"] = "Adair"
county_keys["02"] = "Alfalfa"
county_keys["03"] = "Atoka"
county_keys["04"] = "Beaver"
county_keys["05"] = "Beckham"
county_keys["06"] = "Blaine"
county_keys["07"] = "Bryan"
county_keys["08"] = "Caddo"
county_keys["09"] = "Canadian"
county_keys["10"] = "Carter"
county_keys["11"] = "Cherokee"
county_keys["12"] = "Choctaw"
county_keys["13"] = "Cimarron"
county_keys["14"] = "Cleveland"
county_keys["15"] = "Coal"
county_keys["16"] = "Comanche"
county_keys["17"] = "Cotton"
county_keys["18"] = "Craig"
county_keys["19"] = "Creek"
county_keys["20"] = "Custer"
county_keys["21"] = "Delaware"
county_keys["22"] = "Dewey"
county_keys["23"] = "Ellis"
county_keys["24"] = "Garfield"
county_keys["25"] = "Garvin"
county_keys["26"] = "Grady"
county_keys["27"] = "Grant"
county_keys["28"] = "Greer"
county_keys["29"] = "Harmon"
county_keys["30"] = "Harper"
county_keys["31"] = "Haskell"
county_keys["32"] = "Hughes"
county_keys["33"] = "Jackson"
county_keys["34"] = "Jefferson"
county_keys["35"] = "Johnston"
county_keys["36"] = "Kay"
county_keys["37"] = "Kingfisher"
county_keys["38"] = "Kiowa"
county_keys["39"] = "Latimer"
county_keys["40"] = "LeFlore"
county_keys["41"] = "Lincoln"
county_keys["42"] = "Logan"
county_keys["43"] = "Love"
county_keys["44"] = "McClain"
county_keys["45"] = "McCurtain"
county_keys["46"] = "McIntosh"
county_keys["47"] = "Major"
county_keys["48"] = "Marshall"
county_keys["49"] = "Mayes"
county_keys["50"] = "Murray"
county_keys["51"] = "Muskogee"
county_keys["52"] = "Noble"
county_keys["53"] = "Nowata"
county_keys["54"] = "Okfuskee"
county_keys["55"] = "Oklahoma"
county_keys["56"] = "Okmulgee"
county_keys["57"] = "Osage"
county_keys["58"] = "Ottawa"
county_keys["59"] = "Pawnee"
county_keys["60"] = "Payne"
county_keys["61"] = "Pittsburg"
county_keys["62"] = "Pontotoc"
county_keys["63"] = "Pottawatomie"
county_keys["64"] = "Pushmataha"
county_keys["65"] = "Roger Mills"
county_keys["66"] = "Rogers"
county_keys["67"] = "Seminole"
county_keys["68"] = "Sequoyah"
county_keys["69"] = "Stephens"
county_keys["70"] = "Texas"
county_keys["71"] = "Tillman"
county_keys["72"] = "Tulsa"
county_keys["73"] = "Wagoner"
county_keys["74"] = "Washington"
county_keys["75"] = "Washita"
county_keys["76"] = "Woods"
county_keys["77"] = "Woodwar"

# voters by county
counties = {}

# reading voter files
for ccode in county_keys.keys():
    f = open(vf + ccode + '.dat')
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        county = county_keys[row[0][0:2]]
        counties[county] = counties.get(county, 0) + 1

print counties

# {'LeFlore': 26525, 'Ellis': 2479, 'Comanche': 50421, 'McIntosh': 11434,
# 'Harper': 1962, 'Pontotoc': 19714, 'Delaware': 21706, 'Hughes': 6499,
# 'Cherokee': 23144, 'Pawnee': 8982, 'Woodwar': 10957, 'Jefferson': 3517,
# 'Murray': 7314, 'Seminole': 11301, 'Okfuskee': 5615, 'Mayes': 20627,
# 'Texas': 9444, 'Noble': 6150, 'Jackson': 11833, 'Washita': 6157,
# 'Tulsa': 326736, 'Latimer': 6287, 'Tillman': 4326, 'Garfield': 27987,
# 'Payne': 38181, 'Greer': 2868, 'Haskell': 6848, 'Grady': 29947,
# 'Caddo': 13225, 'Atoka': 7085, 'Grant': 2870, 'Oklahoma': 384500,
# 'Harmon': 1415, 'Bryan': 22994, 'Lincoln': 17916, 'McClain': 20917,
# 'Rogers': 52143, 'Canadian': 64825, 'Adair': 11501, 'Custer': 15135,
# 'McCurtain': 11293, 'Major': 4154, 'Ottawa': 15274, 'Creek': 36166,
# 'Okmulgee': 19963, 'Kiowa': 4749, 'Wagoner': 39028, 'Johnston': 6078,
# 'Kay': 23770, 'Carter': 28273, 'Alfalfa': 2918, 'Muskogee': 37094,
# 'Osage': 25363, 'Love': 5572, 'Beckham': 10345, 'Stephens': 24918,
# 'Pittsburg': 25530, 'Cotton': 3658, 'Marshall': 7414, 'Roger Mills': 2270,
# 'Washington': 29627, 'Sequoyah': 20680, 'Coal': 4095, 'Craig': 7781,
# 'Cimarron': 1688, 'Logan': 25060, 'Woods': 4841, 'Pushmataha': 6892,
# 'Blaine': 5313, 'Choctaw': 8928, 'Cleveland': 141662, 'Beaver': 3182,
# 'Dewey': 2830, 'Kingfisher': 7937, 'Nowata': 5908, 'Pottawatomie': 35349,
# 'Garvin': 14561}

print(str(len(counties)) + ' counties')
# 77 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 1,983,651 registered voters

# preparing empty files by county
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# preparing empty dict for data
i = 0
data = {}
for county in counties:
    data[county] = []

# extracting voter variables into dict
for ccode in county_keys.keys():
    f = open(vf + ccode + '.dat')
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        county = county_keys[row[0][0:2]]
        i += 1
        if i % 100000 == 0:
            print str(i) + '/' + str(voters)
        address = " ".join([row[8], row[9], row[10], row[11], row[12], row[13], 'OK'])
        try:
            votes = row[22:len(row)]
            values = [row[5], row[2], row[3], row[1], row[15], 'NA',
                1 if '20081104' in votes else 0, 1 if '20101102' in votes else 0, 
                1 if '20121106' in votes else 0, 'NA',
                'NA', 'NA', 'NA', 'NA', row[6], address, row[14]]
        except:
            'Error!'
            continue
        data[county].append(values)

   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


