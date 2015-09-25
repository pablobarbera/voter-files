# voter-files

This repository contains a set of python and R scripts to parse voting registration files in the United States into csv files with the same variables: 

- `voter_id`
- `first_name`
- `middle_name`
- `last_name`
- `birth_date`
- `gender`
- `turnout2012`
- `turnout2008`
- `party_affiliation_2012`
- `party_affiliation_2008`
- `residential_address`
- `zipcode`

When any of these variables is not available, that column will be empty. The idea is to be able to merge all these files if so desired.

Pull requests, comments, and suggestions are very welcome!

## Availability of voter files across states

The following lists contains details about if/where voting registration records for each state are available, how much it would cost to obtain them, and other details.

### Alabama 

I couldn't find anything on the website of the [Secretary of State](http://www.sos.alabama.gov/).

### Alaska 

It appears to be possible to [request it via email](http://www.elections.alaska.gov/er_lr.php). A list with contact information is [here](http://www.elections.alaska.gov/csm_contact_reo.php).

### Arizona 

I couldn't find anything on the website of the [Secretary of State](http://www.azsos.gov/).

### Arkansas 

The voter registration file can be requested using the form [here](http://www.sos.arkansas.gov/elections/Documents/ARSOS_Data_Request_Form.pdf), which has to be mailed along with $5.

### California 

http://www.sos.ca.gov/elections/contact/email-elections-division/

### Colorado 
### Connecticut 
### Delaware 
### Florida 
### Georgia 

Voter history files are freely available [here](http://elections.sos.ga.gov/Elections/voterhistory.do), but these do not include voters information. These need to be requested (and will be delivered on a CD) with this [form](http://sos.ga.gov/admin/uploads/Voter_List_Order_Form_june_2015v2.pdf). There's more information [here](http://sos.ga.gov/index.php/elections/order_voter_registration_lists_and_files). I also found [this github repo](https://github.com/stucka/voterhist) with python scripts to parse these files.

### Hawaii 
### Idaho 
### Illinois 
### Indiana 
### Iowa 
### Kansas 
### Kentucky 

I also found [this github repo](https://github.com/courierjournal/kentucky-voterdb-parser) with python scripts to parse these files.


### Louisiana 
### Maine 
### Maryland 
### Massachusetts 
### Michigan 
### Minnesota 
### Mississippi 
### Missouri 
### Montana 

The voter file is available online [here](https://app.mt.gov/voterfile/), but the cost of obtaining the statewide dataset is $1,000.

### Nebraska 
### Nevada 

The voter file is available online [here](http://nvsos.gov/index.aspx?page=332), but it is first necessary to send a signed official request via fax or mail.

### New Hampshire 
### New Jersey 

 I also found [this github repo](https://github.com/pwolanin/import-voters) with PHP scripts to parse these files.

### New Mexico 
### New York 

https://github.com/civic-data/NYS-Voter-File

### North Carolina 

https://github.com/offensivepolitics/wake-county-voter-file-analysis

### North Dakota 
### Ohio 
### Oklahoma 
### Oregon 

The voter file can be requested [here](http://sos.oregon.gov/elections/Pages/data-request.aspx) at a cost of $500 for the statewide voter list.

### Pennsylvania 
### Rhode Island 
### South Carolina 

The voter file is available online [here](http://www.scvotes.org/sale_of_voter_registration_lists), but the cost of obtaining the statewide dataset is $2,500.

### South Dakota 
### Tennessee 
### Texas 
### Utah 
### Vermont 
### Virginia 
### Washington 

The Voter registration database is freely available for download [here](https://www.sos.wa.gov/elections/vrdb-download-form.aspx). A list of database fields can be found [here](http://www.sos.wa.gov/_assets/elections/VRDBDatabaseFields.pdf).

### West Virginia 
### Wisconsin 
### Wyoming
