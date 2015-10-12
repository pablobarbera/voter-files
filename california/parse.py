'''
california/parse.py

Parses California voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-index variables)
# voter_id = county + '_' + 1
# first_name = 3
# middle_name = 4
# last_name = 2
# birth_date = 26
# gender = 27
# turnout2008 = 'PG8' in votes
# turnout2010 = 'GG10' in votes
# turnout2012 = 'PG12' in votes
# turnout2014 = NA
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = 28
# residential_address = [6] + [9] + [10] + row[14] + row[15]
# zipcode = [16]

# voter file(s)
import os
vfsf = '/Volumes/tweets/voter-files/california/voter-records/'
vfs = os.listdir(vfsf)
vfs = [f for f in vfs if 'csv' in f]

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/california/'

# voters by county
counties = {}
for vf in vfs:
    f = open(vfsf + vf)
    print vf.replace('.csv', '')
    for line in f:
        county = vf.replace('.csv', '')
        counties[county] = counties.get(county, 0) + 1

print counties

# {'monterey': 138443, 'san diego': 1556363, 'humboldt': 79977,
# 'fresno': 408188, 'siskiyou': 25161, 'merced': 95310, 'yolo': 100568,
# 'yuba': 28213, 'san luis obispo': 148008, 'sonoma': 244616, 'calaveras': 27546,
# 'tehama': 34246, 'kings': 47151, 'imperial': 58481, 'san mateo': 326897,
# 'santa clara': 826962, 'nevada': 57895, 'glenn': 12662, 'lake': 33665,
# 'el dorado': 108815, 'santa cruz': 170343, 'madera': 54211, 'san francisco': 688036,
# 'plumas': 11633, 'tuolumne': 32704, 'napa': 84886, 'orange': 1369197, 'tulare': 144024,
# 'riverside': 875190, 'mendocino': 48325, 'alameda': 683973, 'colusa': 7395,
# 'trinity': 8197, 'solano': 177288, 'shasta': 93126, 'sacramento': 687451,
# 'contra costa': 497933, 'del norte': 12089, 'marin': 152338, 'sierra': 2091,
# 'amador': 20918, 'modoc': 5437, 'lassen': 15470, 'butte': 121465,
# 'san bernardino': 861565, 'stanislaus': 231863, 'alpine': 759, 'mariposa': 9841,
# 'san joaquin': 286960, 'placer': 206925, 'mono': 5177, 'sutter': 41455, 'kern': 332278,
# 'ventura': 425996, 'los angeles': 4858887, 'san benito': 28001, 'inyo': 10534, 'santa barbara': 188263}

print(str(len(counties)) + ' counties')
# 58 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 17811391 registered voters

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
data = {}
for county in counties:
    data[county] = []

for vf in vfs:
    f = open(vfsf + vf)
    print vf.replace('.csv', '')
    reader = csv.reader(f, delimiter="\t")
    vars = reader.next()
    for row in reader:
        i += 1
        if i % 100000 == 0:
            print str(i) + '/' + str(voters)
        votes = row[58:len(row)]
        turnout2008 = 1 if 'PG8' in votes else 0
        turnout2010 = 1 if 'GG10' in votes else 0
        turnout2012 = 1 if 'PG12' in votes else 0
        address = row[6].strip() + ' ' + row[9].strip() + \
            ' ' + row[10].strip() + ' ' + row[14].strip() + \
            ' ' + row[15]
        values = [vf.replace('.csv', '') + '_' + row[1], row[3],
            row[4], row[2], row[26], row[27].strip(), turnout2008, 
            turnout2010, turnout2012, "NA", 
            "NA", "NA", "NA", "NA", row[28].strip(), address, row[16]]
        county = vf.replace('.csv', '')
        data[county].append(values)
    # writing to disk
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()
    data[county] = []


