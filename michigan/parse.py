'''
michigan/parse.py

Parses Michigan voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (position in line; note 0-indexed)
# voter_id = 448+13
# first_name = 35+20
# middle_name = 55+20
# last_name = 0+35
# birth_date = 78+4
# gender = 82+1
# turnout2008 = '102000017' in votes
# turnout2010 = '102000638' in votes
# turnout2012 = '102000648' in votes
# turnout2014 = '102000665' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = NA
# residential_address = 92+7, 101+2, 105+30, 135+6, 141+2, 156+35, 191+2
# zipcode = 193+5


# voter file(s)
# (first, put it together into a single file)
# cat foia_voters/* > michigan-voter-file.txt
# cat foia_history/* > michigan-voter-history.txt
vf = '/Volumes/tweets/voter-files/michigan/michigan-voter-file.txt'
vh = '/Volumes/tweets/voter-files/michigan/michigan-voter-history.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/michigan/'

# reading country keys
ck = '/Volumes/tweets/voter-files/michigan/countycd.lst.txt'
county_keys = {}
f = open(ck)
for line in f:
    county_keys[line[0:2]] = line[2:(len(line)-2)].strip()

# function to extract fwf
def ext(line, init, length):
    return(line[init:(init+length)])

# voters by county
counties = {}
f = open(vf)
for line in f:
    county = ext(line, 461, 2)
    county = county_keys[county]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'SCHOOLCRAFT': 6674, 'ALCONA': 9314, 'SAGINAW': 153478, 'BERRIEN': 125842,
#  'GRATIOT': 26369, 'BARRY': 44094, 'CHEBOYGAN': 21435, 'WASHTENAW': 277724,
# 'HILLSDALE': 33573, 'OGEMAW': 16417, 'MACOMB': 619113, 'HOUGHTON': 24170,
# 'ALLEGAN': 81355, 'SHIAWASSEE': 52552, 'MUSKEGON': 128898, 'IONIA': 42719,
# 'BENZIE': 14633, 'MONROE': 115566, 'LAKE': 8906, 'MECOSTA': 27273,
# 'ISABELLA': 42082, 'MIDLAND': 65537, 'BARAGA': 6383, 'ALPENA': 23350,
# 'ALGER': 7247, 'ST JOSEPH': 44045, 'DICKINSON': 21918, 'GRAND TRAVERSE': 71646,
# 'GENESEE': 331975, 'BRANCH': 31814, 'KALKASKA': 14263, 'PRESQUE ISLE': 10801,
# 'LIVINGSTON': 139938, 'CLINTON': 55407, 'IRON': 9516, 'OTSEGO': 20290,
# 'MARQUETTE': 49332, 'MONTCALM': 42009, 'EMMET': 27732, 'OSCODA': 6673,
# 'IOSCO': 22091, 'CHIPPEWA': 23884, 'JACKSON': 113436, 'CASS': 39985,
# 'GLADWIN': 21239, 'CLARE': 23087, 'OCEANA': 19323, 'OSCEOLA': 17147,
# 'ARENAC': 12246, 'LAPEER': 66235, 'CALHOUN': 101078, 'MASON': 22615,
# 'MANISTEE': 19625, 'WAYNE': 1348658, 'EATON': 80777, 'MONTMORENCY': 7970,
# 'TUSCOLA': 40899, 'BAY': 80161, 'LENAWEE': 72370, 'GOGEBIC': 13519, 'KALAMAZOO': 194539,
# 'ST CLAIR': 122508, 'HURON': 25193, 'NEWAYGO': 35364, 'KEWEENAW': 1913,
# 'SANILAC': 29320, 'INGHAM': 196154, 'LEELANAU': 19673, 'VAN BUREN': 55423,
# 'CHARLEVOIX': 22233, 'OTTAWA': 187981, 'LUCE': 4317, 'ROSCOMMON': 21812,
# 'ANTRIM': 20076, 'WEXFORD': 24911, 'KENT': 441197, 'DELTA': 29092,
# 'ONTONAGON': 5752, 'MACKINAC': 9589, 'MENOMINEE': 19313, 'OAKLAND': 938251,
# 'CRAWFORD': 11177, 'MISSAUKEE': 10741}

print(str(len(counties)) + ' counties')
# 83 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 7424937 registered voters

# preparing empty files by county
import csv
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# preparing dict with vote history
f = open(vh)
voters = {}
i = 0
for line in f:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/63986183'
    voterid = ext(line, 0, 13).strip()
    elec = ext(line, 25, 13).strip()
    if elec in ['102000017', '102000638', '102000648', '102000665']:
        try:
            voters[voterid].append(elec)
        except:
            voters[voterid] = []
            voters[voterid].append(elec)

# reading voter history
f = open(vf)    
data = {}
for county in counties:
    data[county] = []

i = 0
for line in f:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/7424937'
    voterid = ext(line, 448, 13).strip()
    try:
        votes = voters[voterid]
    except:
        votes = []
    turnout2008 = 1 if '102000017' in votes else 0
    turnout2010 = 1 if '102000638' in votes else 0
    turnout2012 = 1 if '102000648' in votes else 0
    turnout2014 = 1 if '102000665' in votes else 0
    address = ext(line, 92, 7).strip() + ' ' + ext(line, 101, 2).strip() + \
        ' ' + ext(line, 105, 30).strip() + ' ' + ext(line, 135, 6).strip() + \
        ' ' + ext(line, 141, 2).strip() + ' ' + ext(line, 156, 35).strip() + \
        ' ' + ext(line, 191, 2).strip()
    values = [voterid, ext(line, 35, 20).strip(), ext(line, 55, 20).strip(),
        ext(line, 0, 35).strip(), ext(line, 78, 4).strip(), ext(line, 82, 1),
        turnout2008, turnout2010, turnout2012, turnout2014,
        "NA", "NA", "NA", "NA", "NA", address, ext(line, 193, 5)]
    county = ext(line, 461, 2)
    county = county_keys[county]
    data[county].append(values)

# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()
    data[county] = []


