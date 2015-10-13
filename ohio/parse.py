'''
ohio/parse.py

Parses Ohio voter file into csv files, one per county,
with the following variables:

'''

newvars = ["voter_id", "first_name", "middle_name", \
    "last_name", "birth_date", "gender", "turnout2008", "turnout2010", \
    "turnout2012", "turnout2014", "party_affiliation2008", \
    "party_affiliation2010", "party_affiliation2012", "party_affiliation2014", \
    "party_affiliation", "residential_address", "zipcode"]

# correspondence of variables (0-indexed)
# voter_id = 0
# first_name = 4
# middle_name = 5
# last_name = 3
# birth_date = 7
# gender = NA
# turnout2008 = if [70] is 'X'
# turnout2010 = if [80] is 'X'
# turnout2012 = if [85] is 'X'
# turnout2014 = if [91] is 'X'
# party_affiliation_2008 = [68]
# party_affiliation_2010 = [77]
# party_affiliation_2012 = [84]
# party_affiliation_2014 = [90]
# party_affiliation = 10
# residential_address = 11 + 13 + 14
# zipcode = 15

import csv

# voter file
vf1 = '/Volumes/tweets/voter-files/ohio/SWVF_1_44.TXT'
vf2 = '/Volumes/tweets/voter-files/ohio/SWVF_45_88.TXT'

# outfolder
outfolder = '/Volumes/tweets/voter-files/OUTPUT/ohio/'

county_keys = {}

county_keys["01"] ="ADAMS"     
county_keys["02"] ="ALLEN"     
county_keys["03"] ="ASHLAND"   
county_keys["04"] ="ASHTABULA" 
county_keys["05"] ="ATHENS"    
county_keys["06"] ="AUGLAIZE"  
county_keys["07"] ="BELMONT"   
county_keys["08"] ="BROWN"     
county_keys["09"] ="BUTLER"    
county_keys["10"] = "CARROLL"   
county_keys["11"] = "CHAMPAIGN" 
county_keys["12"] = "CLARK"     
county_keys["13"] = "CLERMONT"  
county_keys["14"] = "CLINTON"   
county_keys["15"] = "COLUMBIANA"
county_keys["16"] = "COSHOCTON" 
county_keys["17"] = "CRAWFORD"  
county_keys["18"] = "CUYAHOGA"  
county_keys["19"] = "DARKE"     
county_keys["20"] = "DEFIANCE"  
county_keys["21"] = "DELAWARE"  
county_keys["22"] = "ERIE"      
county_keys["23"] = "FAIRFIELD" 
county_keys["24"] = "FAYETTE"   
county_keys["25"] = "FRANKLIN"  
county_keys["26"] = "FULTON"    
county_keys["27"] = "GALLIA"    
county_keys["28"] = "GEAUGA"    
county_keys["29"] = "GREENE"    
county_keys["30"] = "GUERNSEY"  
county_keys["31"] = "HAMILTON"  
county_keys["32"] = "HANCOCK"   
county_keys["33"] = "HARDIN"    
county_keys["34"] = "HARRISON"  
county_keys["35"] = "HENRY"     
county_keys["36"] = "HIGHLAND"  
county_keys["37"] = "HOCKING"   
county_keys["38"] = "HOLMES"    
county_keys["39"] = "HURON"     
county_keys["40"] = "JACKSON"   
county_keys["41"] = "JEFFERSON" 
county_keys["42"] = "KNOX"      
county_keys["43"] = "LAKE"      
county_keys["44"] = "LAWRENCE"  
county_keys["45"] = "LICKING"   
county_keys["46"] = "LOGAN"     
county_keys["47"] = "LORAIN"    
county_keys["48"] = "LUCAS"     
county_keys["49"] = "MADISON"   
county_keys["50"] = "MAHONING"  
county_keys["51"] = "MARION"    
county_keys["52"] = "MEDINA"    
county_keys["53"] = "MEIGS"     
county_keys["54"] = "MERCER"    
county_keys["55"] = "MIAMI"     
county_keys["56"] = "MONROE"    
county_keys["57"] = "MONTGOMERY"
county_keys["58"] = "MORGAN"    
county_keys["59"] = "MORROW"    
county_keys["60"] = "MUSKINGUM" 
county_keys["61"] = "NOBLE"     
county_keys["62"] = "OTTAWA"    
county_keys["63"] = "PAULDING"  
county_keys["64"] = "PERRY"     
county_keys["65"] = "PICKAWAY"  
county_keys["66"] = "PIKE"      
county_keys["67"] = "PORTAGE"   
county_keys["68"] = "PREBLE"    
county_keys["69"] = "PUTNAM"    
county_keys["70"] = "RICHLAND"  
county_keys["71"] = "ROSS"      
county_keys["72"] = "SANDUSKY"  
county_keys["73"] = "SCIOTO"    
county_keys["74"] = "SENECA"    
county_keys["75"] = "SHELBY"    
county_keys["76"] = "STARK"     
county_keys["77"] = "SUMMIT"    
county_keys["78"] = "TRUMBULL"  
county_keys["79"] = "TUSCARAWAS"
county_keys["80"] = "UNION"     
county_keys["81"] = "VANWERT"   
county_keys["82"] = "VINTON"    
county_keys["83"] = "WARREN"    
county_keys["84"] = "WASHINGTON"
county_keys["85"] = "WAYNE"     
county_keys["86"] = "WILLIAMS"  
county_keys["87"] = "WOOD"      
county_keys["88"] = "WYANDOT"

# voters by county
counties = {}

# reading voter file 1
reader = csv.reader(open(vf1))
vars = reader.next()
for row in reader:
    county = county_keys[row[1]]
    counties[county] = counties.get(county, 0) + 1

# reading voter file 2
reader = csv.reader(open(vf2))
vars = reader.next()
for row in reader:
    county = county_keys[row[1]]
    counties[county] = counties.get(county, 0) + 1

print counties

# {'ADAMS': 17869, 'LAWRENCE': 41441, 'TRUMBULL': 134330, 'ASHLAND': 34081,
# 'ERIE': 50745, 'MONROE': 9300, 'PIKE': 18402, 'SHELBY': 33184, 'CHAMPAIGN': 24806,
# 'SUMMIT': 358853, 'PUTNAM': 22940, 'HAMILTON': 540539, 'ASHTABULA': 58018,
# 'MERCER': 27865, 'LAKE': 147125, 'WILLIAMS': 23728, 'ROSS': 41408, 'MAHONING': 159027,
# 'HARDIN': 18243, 'CARROLL': 17272, 'MONTGOMERY': 351537, 'GREENE': 106428,
# 'COLUMBIANA': 62543, 'JACKSON': 20545, 'LUCAS': 286424, 'UNION': 33659,
# 'WASHINGTON': 39978, 'WAYNE': 72222, 'HENRY': 18618, 'WARREN': 142170,
# 'CLINTON': 24965, 'RICHLAND': 79630, 'SANDUSKY': 38227, 'OTTAWA': 29655,
# 'WOOD': 87630, 'FULTON': 27713, 'AUGLAIZE': 31856, 'GEAUGA': 61704, 'HIGHLAND': 26295,
# 'CRAWFORD': 27172, 'SENECA': 32952, 'MEIGS': 14472, 'DEFIANCE': 24409, 'GALLIA': 17874,
# 'JEFFERSON': 45515, 'KNOX': 37963, 'BROWN': 27046, 'DELAWARE': 123204,
# 'FAYETTE': 15348, 'GUERNSEY': 23291, 'VANWERT': 18933, 'VINTON': 7984,
# 'PICKAWAY': 31974, 'COSHOCTON': 22096, 'MIAMI': 72369, 'HANCOCK': 48434,
# 'LICKING': 109919, 'FAIRFIELD': 94145, 'HARRISON': 9784, 'HOCKING': 17626,
# 'PREBLE': 26554, 'SCIOTO': 44221, 'PAULDING': 12222, 'BELMONT': 45242,
# 'FRANKLIN': 825847, 'MORGAN': 8537, 'HURON': 35943, 'DARKE': 32748,
# 'PERRY': 21037, 'TUSCARAWAS': 56073, 'WYANDOT': 15262, 'CLERMONT': 136002,
# 'LORAIN': 194414, 'ATHENS': 37759, 'MORROW': 24071, 'BUTLER': 232542,
# 'ALLEN': 66123, 'HOLMES': 17277, 'PORTAGE': 98993, 'STARK': 239494,
# 'MARION': 38155, 'MEDINA': 123823, 'MUSKINGUM': 51579, 'NOBLE': 7918,
# 'MADISON': 22949, 'CUYAHOGA': 834861, 'CLARK': 85471, 'LOGAN': 29304}

print(str(len(counties)) + ' counties')
# 88 counties

voters = sum(counties.values())
print(str(voters) + ' registered voters')
# 7,507,906 registered voters

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

# extracting voter variables into dict (file 1)
reader = csv.reader(open(vf1))
vars = reader.next()

for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    address = " ".join([row[11], row[13], row[14]])
    values = [row[0], row[4], row[5], row[3], row[7], "NA", 
        1 if row[70] is 'X' else 0, 1 if row[80] is 'X' else 0, 
        1 if row[85] is 'X' else 0, 1 if row[91] is 'X' else 0, 
        row[68], row[77], row[84], row[90], row[10],
        address, row[15]]
    county = county_keys[row[1]]
    data[county].append(values)

# extracting voter variables into dict (file 2)
reader = csv.reader(open(vf2))
vars = reader.next()

for row in reader:
    i += 1
    if i % 100000 == 0:
        print str(i) + '/' + str(voters)
    address = " ".join([row[11], row[13], row[14]])
    values = [row[0], row[4], row[5], row[3], row[7], "NA", 
        1 if row[70] is 'X' else 0, 1 if row[80] is 'X' else 0, 
        1 if row[85] is 'X' else 0, 1 if row[91] is 'X' else 0, 
        row[68], row[77], row[84], row[90], row[10],
        address, row[15]]
    county = county_keys[row[1]]
    data[county].append(values)
   
# writing to disk
for county in counties:
    outf = open(outfolder + county + '.csv', 'a')
    out = csv.writer(outf)
    for row in data[county]:
        out.writerow(row)
    outf.close()


