'''
washington/parse.py

Parses Michigan voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (position in line; note 0-indexed)
# voter_id = 0
# first_name = 3
# middle_name = 4
# last_name = 5
# birth_date = 7
# gender = 8
# turnout2008 = '102000017' in votes
# turnout2010 = '102000638' in votes
# turnout2012 = '102000648' in votes
# turnout2014 = '102000665' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = NA
# residential_address = 9:18
# zipcode = 19


# voter file(s)
vf = '/Volumes/tweets/voter-files/washington/vrdb-current/201508_VRDB_Extract.txt'

# put together into a single file
#cat Pre2009-Voting_History.txt 2009.thru.2012-Voting_History.txt 2011-2012-2013-VotingHistory.txt \
#    2013-2014_VotingHistoryExtract.txt > voting-history.txt
vh = '/Volumes/tweets/voter-files/washington/vrdb-current/voting-history.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/washington/'

# reading country keys
county_keys = {}
county_keys["AD"] = "Adams"
county_keys["AS"] = "Asotin"
county_keys["BE"] = "Benton"
county_keys["CH"] = "Chelan"
county_keys["CM"] = "Clallam"
county_keys["CR"] = "Clark"
county_keys["CU"] = "Columbia"
county_keys["CZ"] = "Cowlitz"
county_keys["DG"] = "Douglas"
county_keys["FE"] = "Ferry"
county_keys["FR"] = "Franklin"
county_keys["GA"] = "Garfield"
county_keys["GR"] = "Grant"
county_keys["GY"] = "Grays Harbor"
county_keys["IS"] = "Island"
county_keys["JE"] = "Jefferson"
county_keys["KI"] = "King"
county_keys["KP"] = "Kitsap"
county_keys["KS"] = "Kittitas"
county_keys["KT"] = "Klickitat"
county_keys["LE"] = "Lewis"
county_keys["LI"] = "Lincoln"
county_keys["MA"] = "Mason"
county_keys["OK"] = "Okanogan"
county_keys["PA"] = "Pacific"
county_keys["PE"] = "Pend Oreille"
county_keys["PI"] = "Pierce"
county_keys["SJ"] = "San Juan"
county_keys["SK"] = "Skagit"
county_keys["SM"] = "Skamania"
county_keys["SN"] = "Snohomish"
county_keys["SP"] = "Spokane"
county_keys["ST"] = "Stevens"
county_keys["TH"] = "Thurston"
county_keys["WK"] = "Wahkiakum"
county_keys["WL"] = "Walla Walla"
county_keys["WM"] = "Whatcom"
county_keys["WT"] = "Whitman"
county_keys["YA"] = "Yakima"

import csv

# voters by county
counties = {}
reader = csv.reader(open(vf), delimiter="\t")
vars = reader.next()
for row in reader:
    try:
        county = county_keys[row[20]]
        counties[county] = counties.get(county, 0) + 1
    except:
        continue

print counties

# {'San Juan': 12783, 'Pend Oreille': 10132, 'Snohomish': 460819, 'Grant': 43296,
# 'Lincoln': 7450, 'Douglas': 21841, 'Mason': 38416, 'Jefferson': 25158,
# 'Whatcom': 139157, 'Wahkiakum': 3089, 'Cowlitz': 66031, 'Columbia': 2916,
# 'Thurston': 180352, 'Yakima': 115085, 'Klickitat': 14933, 'Okanogan': 23011,
# 'Kitsap': 168852, 'Clallam': 51512, 'King': 1289285, 'Pierce': 501027,
# 'Spokane': 311444, 'Whitman': 25133, 'Grays Harbor': 44649, 'Island': 56138,
# 'Benton': 103389, 'Franklin': 35219, 'Ferry': 4997, 'Kittitas': 24938,
# 'Skagit': 73633, 'Skamania': 7532, 'Clark': 279522, 'Walla Walla': 34948,
# 'Lewis': 47631, 'Stevens': 32997, 'Pacific': 14337, 'Garfield': 1725,
# 'Adams': 6708, 'Chelan': 43478, 'Asotin': 15707}

print(str(len(counties)) + ' counties')
# 39 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 4339270 registered voters

# preparing empty files by county
import csv
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# preparing dict with vote history
reader = csv.reader(open(vh), delimiter="\t")
voters = {}
i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/81603232'
    elec = row[2]
    voterid = row[1]
    if elec in ['11/04/2008', '11/02/2010', '11/06/2012', '11/04/2014']:
        try:
            voters[voterid].append(elec)
        except:
            voters[voterid] = []
            voters[voterid].append(elec)

# reading voter history
reader = csv.reader(open(vf), delimiter="\t")
data = {}
for county in counties:
    data[county] = []

i = 0
for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/4339270'
    try:
        county = county_keys[row[20]]
    except:
        continue
    voterid = row[0]
    try:
        votes = voters[voterid]
    except:
        votes = []
    turnout2008 = 1 if '11/04/2008' in votes else 0
    turnout2010 = 1 if '11/02/2010' in votes else 0
    turnout2012 = 1 if '11/06/2012' in votes else 0
    turnout2014 = 1 if '11/04/2014' in votes else 0
    address = " ".join(row[9:18])
    values = [voterid, row[3], row[4], row[5], row[7], row[8],
        turnout2008, turnout2010, turnout2012, turnout2014,
        "NA", "NA", "NA", "NA", "NA", address, row[19]]
    data[county].append(values)

# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()
    data[county] = []


