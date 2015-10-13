'''
pennsylvania/parse.py

Parses Pennsylvania voter file into csv files, one per county,
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
# birth_date = 7
# gender = 6
# turnout2008 = see dict below
# turnout2010 = see dict below
# turnout2012 = see dict below
# turnout2014 = 'NA'
# party_affiliation_2008 = see dict below
# party_affiliation_2010 = see dict below
# party_affiliation_2012 = see dict below
# party_affiliation_2014 = 'NA'
# party_affiliation = 11
# residential_address = 12, 13, 14, 17, 18
# zipcode = 19

import csv
import os
import re

# voter file folder
vf = '/Volumes/tweets/voter-files/pennsylvania/Voter Export Files/'
vs = os.listdir(vf)
vs = [v for v in vs if '.txt' in v]

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/pennsylvania/'

# voters by county
counties = {}

# reading voter files
for v in vs:
    f = open(vf + v, 'rb')
    county = re.match('(.*) FVE.*', v).group(1)
    print county
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        counties[county] = counties.get(county, 0) + 1

print counties

# {'BEDFORD': 32378, 'NORTHAMPTON': 198648, 'COLUMBIA': 39188, 'ADAMS': 59874,
# 'LAWRENCE': 60095, 'SULLIVAN': 4248, 'POTTER': 10744, 'NORTHUMBERLAND': 53727,
# 'PHILADELPHIA': 1028967, 'LUZERNE': 196108, 'SCHUYLKILL': 84574,
# 'JEFFERSON': 28624, 'CHESTER': 331842, 'BEAVER': 109333, 'CARBON': 38455,
# 'ERIE': 177985, 'DAUPHIN': 174380, 'MONROE': 100812, 'CLEARFIELD': 51314,
# 'WESTMORELAND': 239736, 'PIKE': 40459, 'MONTOUR': 11865, 'CUMBERLAND': 147913,
# 'ARMSTRONG': 40950, 'LYCOMING': 65588, 'DELAWARE': 385251, 'LEBANON': 80202,
# 'FAYETTE': 80881, 'MONTGOMERY': 540552, 'GREENE': 22118, 'FOREST': 3273,
# 'SNYDER': 21171, 'CAMERON': 3619, 'BUCKS': 429505, 'SOMERSET': 49156,
# 'WARREN': 29220, 'VENANGO': 31658, 'LANCASTER': 307014, 'ELK': 19637,
# 'SUSQUEHANNA': 25422, 'CENTRE': 107929, 'UNION': 23142, 'HUNTINGDON': 28983,
# 'WYOMING': 16958, 'WASHINGTON': 139484, 'CLARION': 22885, 'BUTLER': 120427,
# 'LEHIGH': 217879, 'PERRY': 26842, 'YORK': 267829, 'BERKS': 245179,
# 'INDIANA': 57038, 'McKEAN': 23983, 'MERCER': 72063, 'JUNIATA': 13615,
# 'BRADFORD': 39664, 'TIOGA': 25468, 'CLINTON': 22854, 'BLAIR': 84330,
# 'MIFFLIN': 24511, 'WAYNE': 31822, 'CAMBRIA': 84890, 'FRANKLIN': 87375,
# 'ALLEGHENY': 881456, 'CRAWFORD': 52509, 'FULTON': 8995, 'LACKAWANNA': 146971}

print(str(len(counties)) + ' counties')
# 67 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 8,231,567 registered voters

# preparing empty files by county
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# file with election correspondences
elections = {}
elf = '/Volumes/tweets/voter-files/pennsylvania/Election Map Files/'
for county in counties.keys():
    print county
    elections[county] = ["0", "0", "0", "0", "0", "0"]
    ff = open(elf + county + " Election Map 20130701.txt")
    reader = csv.reader(ff, delimiter="\t")
    for row in reader:
        if row[3] == '11/06/2012':
            elections[county][0] = int(row[1])
        if row[3] == "11/02/2010":
            elections[county][1] = int(row[1])
        if row[3] == "11/04/2008":
            elections[county][2] = int(row[1])
        if row[3] == '04/24/2012':
            elections[county][3] = int(row[1])
        if row[3] == "05/18/2010":
            elections[county][4] = int(row[1])
        if row[3] == "04/22/2008":
            elections[county][5] = int(row[1])

# preparing empty dict for data
i = 0
data = {}
for county in counties:
    data[county] = []

# extracting voter variables into dict
for v in vs:
    f = open(vf + v, 'rb')
    county = re.match('(.*) FVE.*', v).group(1)
    print county
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        i += 1
        if i % 100000 == 0:
            print str(i) + '/' + str(voters)
        address = " ".join([row[12], row[13], row[14], row[17], row[18]])
        values = [row[0], row[3], row[4], row[2], row[7], row[6],
            1 if row[70+(elections[county][0]*2)-2] is not '' else 0,
            1 if row[70+(elections[county][1]*2)-2] is not '' else 0,
            1 if row[70+(elections[county][2]*2)-2] is not '' else 0,
            "NA",
            row[70+(elections[county][3]*2)-2+1],
            row[70+(elections[county][4]*2)-2+1],
            row[70+(elections[county][5]*2)-2+1],
            "NA", row[11], address, row[19]]
        data[county].append(values)

   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


