'''
connecticut/parse.py

Parses Connecticut voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (in fixed character width file)
# voter_id = [4:13]
# first_name = [50:70]
# middle_name = [71:86]
# last_name = [14:49]
# birth_date = [423:433]
# gender = [457:458]
# turnout2008 = '11/04/2008' in votes
# turnout2010 = '11/02/2010' in votes
# turnout2012 = '11/06/2012' in votes
# turnout2014 = '11/04/2014' in votes
# party_affiliation_2008 = NA
# party_affiliation_2010 = NA
# party_affiliation_2012 = NA
# party_affiliation_2014 = NA
# party_affiliation = [445:450]
# residential_address = [179:185] + [195:235] + line[236:254] + [255:257]
# zipcode = [258:263]

# voter file(s)
# [first put them all together]
# cat SSP/ELCT/VOTER/EXT1 SSP\ 2/ELCT/VOTER/EXT3 /
#   SSP\ 3/ELCT/VOTER/EXT4 SSP\ 4/ELCT/VOTER/EXT2 > connecticut-voter-file.txt
vf = '/Volumes/tweets/voter-files/connecticut/connecticut-voter-file.txt'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/connecticut/'

# list of towns and counties
# NOTE: voter file does not contain county names, so we identify these by
# town names
towns = {}

towns["Bethel"] = 'Fairfield'
towns["Bridgeport"] = 'Fairfield'
towns["Brookfield"] = 'Fairfield'
towns["Danbury"] = 'Fairfield'
towns["Darien"] = 'Fairfield'
towns["Easton"] = 'Fairfield'
towns["Fairfield"] = 'Fairfield'
towns["Greenwich"] = 'Fairfield'
towns["Monroe"] = 'Fairfield'
towns["New Canaan"] = 'Fairfield'
towns["New Fairfield"] = 'Fairfield'
towns["Newtown"] = 'Fairfield'
towns["Norwalk"] = 'Fairfield'
towns["Shelton"] = 'Fairfield'
towns["Sherman"] = 'Fairfield'
towns["Stamford"] = 'Fairfield'
towns["Stratford"] = 'Fairfield'
towns["Redding"] = 'Fairfield'
towns["Ridgefield"] = 'Fairfield'
towns["Trumbull"] = 'Fairfield'
towns["Weston"] = 'Fairfield'
towns["Westport"] = 'Fairfield'
towns["Wilton"] = 'Fairfield'

towns["Avon"] = 'Hartford'
towns["Berlin"] = 'Hartford'
towns["Bloomfield"] = 'Hartford'
towns["Bristol"] = 'Hartford'
towns["Burlington"] = 'Hartford'
towns["Canton"] = 'Hartford'
towns["East Granby"] = 'Hartford'
towns["East"] = 'Hartford'
towns["Hartford"] = 'Hartford'
towns["East Windsor"] = 'Hartford'
towns["Enfield"] = 'Hartford'
towns["Farmington"] = 'Hartford'
towns["Glastonbury"] = 'Hartford'
towns["Granby"] = 'Hartford'
towns["Hartford"] = 'Hartford'
towns["Hartland"] = 'Hartford'
towns["Manchester"] = 'Hartford'
towns["Marlborough"] = 'Hartford'
towns["New Britain"] = 'Hartford'
towns["Newington"] = 'Hartford'
towns["Plainville"] = 'Hartford'
towns["Rocky  Hill"] = 'Hartford'
towns["Simsbury"] = 'Hartford'
towns["Southington"] = 'Hartford'
towns["South Windsor"] = 'Hartford'
towns["Suffield"] = 'Hartford'
towns["West Hartford"] = 'Hartford'
towns["Wethersfield"] = 'Hartford'
towns["Windsor"] = 'Hartford'
towns["Windsor Locks"] = 'Hartford'



towns["Barkhamsted"] = 'Litchfield'
towns["Bethlehem"] = 'Litchfield'
towns["Bridgewater"] = 'Litchfield'
towns["Canaan"] = 'Litchfield'
towns["Colebrook"] = 'Litchfield'
towns["Cornwall"] = 'Litchfield'
towns["Goshen"] = 'Litchfield'
towns["Harwinton"] = 'Litchfield'
towns["Kent"] = 'Litchfield'
towns["Litchfield"] = 'Litchfield'
towns["Morris"] = 'Litchfield'
towns["New Hartford"] = 'Litchfield'
towns["New Milford"] = 'Litchfield'
towns["Norfolk"] = 'Litchfield'
towns["North Canaan"] = 'Litchfield'
towns["Plymouth"] = 'Litchfield'
towns["Roxbury"] = 'Litchfield'
towns["Salisbury"] = 'Litchfield'
towns["Sharon"] = 'Litchfield'
towns["Thomaston"] = 'Litchfield'
towns["Torrington"] = 'Litchfield'
towns["Warren"] = 'Litchfield'
towns["Washington"] = 'Litchfield'
towns["Watertown"] = 'Litchfield'
towns["Winchester"] = 'Litchfield'
towns["Woodbury"] = 'Litchfield'


towns["Chester"] = 'Middlesex'
towns["Clinton"] = 'Middlesex'
towns["Cromwell"] = 'Middlesex'
towns["Deep River"] = 'Middlesex'
towns["Durham"] = 'Middlesex'
towns["East Haddam"] = 'Middlesex'
towns["East Hampton"] = 'Middlesex'
towns["Essex"] = 'Middlesex'
towns["Haddam"] = 'Middlesex'
towns["Killingworth"] = 'Middlesex'
towns["Middlefield"] = 'Middlesex'
towns["Middletown"] = 'Middlesex'
towns["Old Saybrook"] = 'Middlesex'
towns["Portland"] = 'Middlesex'
towns["Westbrook"] = 'Middlesex'


towns["Ansonia"] = 'New Haven'
towns["Beacon Falls"] = 'New Haven'
towns["Bethany"] = 'New Haven'
towns["Branford"] = 'New Haven'
towns["Cheshire"] = 'New Haven'
towns["Derby"] = 'New Haven'
towns["East Haven"] = 'New Haven'
towns["Guilford"] = 'New Haven'
towns["Hamden"] = 'New Haven'
towns["Madison"] = 'New Haven'
towns["Meriden"] = 'New Haven'
towns["Middlebury"] = 'New Haven'
towns["Milford"] = 'New Haven'
towns["Naugatuck"] = 'New Haven'
towns["New Haven"] = 'New Haven'
towns["North Branford"] = 'New Haven'
towns["North Haven"] = 'New Haven'
towns["Orange"] = 'New Haven'
towns["Oxford"] = 'New Haven'
towns["Prospect"] = 'New Haven'
towns["Seymour"] = 'New Haven'
towns["Southbury"] = 'New Haven'
towns["Wallingford"] = 'New Haven'
towns["Waterbury"] = 'New Haven'
towns["West Haven"] = 'New Haven'
towns["Wolcott"] = 'New Haven'
towns["Woodbridge"] = 'New Haven'

towns["Bozrah"] = 'New London'
towns["Colchester"] = 'New London'
towns["East Lyme"] = 'New London'
towns["Franklin"] = 'New London'
towns["Griswold"] = 'New London'
towns["Groton"] = 'New London'
towns["Lebanon"] = 'New London'
towns["Ledyard"] = 'New London'
towns["Lisbon"] = 'New London'
towns["Lyme"] = 'New London'
towns["Montville"] = 'New London'
towns["New London"] = 'New London'
towns["North Stonington"] = 'New London'
towns["Norwich"] = 'New London'
towns["Old Lyme"] = 'New London'
towns["Preston"] = 'New London'
towns["Salem"] = 'New London'
towns["Sprague"] = 'New London'
towns["Stonington"] = 'New London'
towns["Voluntown"] = 'New London'
towns["Waterford"] = 'New London'

towns["Andover"] = 'Tolland'
towns["Bolton"] = 'Tolland'
towns["Columbia"] = 'Tolland'
towns["Coventry"] = 'Tolland'
towns["Ellington"] = 'Tolland'
towns["Hebron"] = 'Tolland'
towns["Mansfield"] = 'Tolland'
towns["Somers"] = 'Tolland'
towns["Stafford"] = 'Tolland'
towns["Tolland"] = 'Tolland'
towns["Union"] = 'Tolland'
towns["Vernon"] = 'Tolland'
towns["Willington"] = 'Tolland'

towns["Ashford"] = 'Windham'
towns["Brooklyn"] = 'Windham'
towns["Canterbury"] = 'Windham'
towns["Chaplin"] = 'Windham'
towns["Eastford"] = 'Windham'
towns["Hampton"] = 'Windham'
towns["Killingly"] = 'Windham'
towns["Plainfield"] = 'Windham'
towns["Pomfret"] = 'Windham'
towns["Putnam"] = 'Windham'
towns["Scotland"] = 'Windham'
towns["Sterling"] = 'Windham'
towns["Thompson"] = 'Windham'
towns["Windham"] = 'Windham'
towns["Woodstock"] = 'Windham'

# reading file
f = open(vf)

# voters by county
counties = {}
for line in f:
    try:
        county = towns[line[236:254].strip()]
    except:
        continue
    # NOTE: exclude voter records without town information (around 8%)
    counties[county] = counties.get(county, 0) + 1

print counties

# {'New London': 134129, 'New Haven': 569170, 'Middlesex': 109559, 
# 'Litchfield': 120786, 'Fairfield': 577059, 'Tolland': 98293, 
# 'Windham': 56098, 'Hartford': 519317}

print(str(len(counties)) + ' counties')
# 8 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 2184411 registered voters

# preparing empty files by county
import csv
for county in counties.keys():
    outf = open(outfolder + county + '.csv', 'w')
    out = csv.writer(outf)
    out.writerow(newvars)
    outf.close()

# extracting voter variables into dict
f = open(vf)
i = 0
data = {}
for county in counties:
    data[county] = []

for line in f:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    votes = line[470:len(line)]
    votes = votes.split(',')
    turnout2008 = 1 if '11/04/2008' in votes else 0
    turnout2010 = 1 if '11/02/2010' in votes else 0
    turnout2012 = 1 if '11/06/2012' in votes else 0
    turnout2014 = 1 if '11/04/2014' in votes else 0
    address = line[179:185].strip() + ' ' + line[195:235].strip() + \
    ' ' + line[236:254].strip() + ' ' + line[255:257]
    values = [line[4:13], line[50:70].strip(), line[71:86].strip(), 
        line[14:49].strip(), line[423:433], line[457:458], 
        turnout2008, turnout2010, turnout2012, turnout2014, 
        "NA", "NA", "NA", "NA", line[445:450].strip(), address,
        line[258:263].strip()]
    try:
        county = towns[line[236:254].strip()]
    except:
        continue
    data[county].append(values)


# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf, delimiter=',', quotechar='"')
    for row in data[county]:
        out.writerow(row)
    outf.close()


