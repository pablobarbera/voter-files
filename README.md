# voter-files

This repository contains a set of python and R scripts to parse voting registration files in the United States into csv files with the same variables: 

- `voter_id`
- `first_name`
- `middle_name`
- `last_name`
- `birth_date`
- `gender`
- `turnout2008`
- `turnout2010`
- `turnout2012`
- `turnout2014`
- `party_affiliation_2008`
- `party_affiliation_2010`
- `party_affiliation_2012`
- `party_affiliation_2014`
- `party_affiliation` (current)
- `residential_address`
- `zipcode`
- `race`, `ethnicity` (in Florida and North Carolina)

When any of these variables is not available, that column will be left empty (`NA`). The idea is to be able to easily merge all these files if so desired.

Pull requests, comments, and suggestions are very welcome!

## Availability of voter files across states

The following lists contains details about if/where voting registration records for each state are available, how much it would cost to obtain them, and other details. (I will expand this list over the next few months.)

To be clear: this repository does __NOT__ contain any data.

Classification:

- :smile: Available at low cost ($100 or less) or free
- :money_with_wings: Available at high cost (more than $100)
- :disappointed: No information online about how to acquire voter file


### :disappointed: Alabama 

I couldn't find anything on the website of the [Secretary of State](http://www.sos.alabama.gov/).

### Alaska 

It appears to be possible to [request it via email](http://www.elections.alaska.gov/er_lr.php). A list with contact information is [here](http://www.elections.alaska.gov/csm_contact_reo.php).

### :disappointed: Arizona 

I couldn't find anything on the website of the [Secretary of State](http://www.azsos.gov/).

### :smile: Arkansas 

The voter registration file can be requested using the form [here](http://www.sos.arkansas.gov/elections/Documents/ARSOS_Data_Request_Form.pdf), which has to be mailed along with $5.

### California 

http://www.sos.ca.gov/elections/contact/email-elections-division/

### :smile: Colorado 

The registed voter list and voter history list can be requested using the form [here](http://www.sos.state.co.us/pubs/elections/forms/dataRequests.pdf), at a cost of [$50 each](http://www.sos.state.co.us/pubs/info_center/fees/elections.html). There appears to be a free copy of all the files on [this website](http://coloradovoters.info/download.html) as well.

### :smile: Connecticut 

The voter registry file can be purchased at a cost of $300 by contacting the Secrety of State as detailed [here](http://www.ct.gov/sots/cwp/view.asp?a=3179&q=532994). A copy of the voter list appears to be also available online for free on [this website](http://connvoters.com/download.html).

### :smile: Delaware 

The voter file can be requested using the form [here](http://elections.delaware.gov/candidate/pdfs/Statewide_CD_Order_Form.pdf), at a cost of $10 (in CD format). A copy of the voter list appears to be also available online for free on [this website](http://delawarevoters.info/downloads.html).

### :smile: Florida 

The voter file can be requested using the form [here](http://dos.myflorida.com/elections/data-statistics/voter-registration-statistics/voter-registration-file-request/), at a cost of $5 (in CD format). A copy of the voter list appears to be also available online for free on [this website](http://flvoters.com/downloads.html).

### :money_with_wings: Georgia 

Voter history files are freely available [here](http://elections.sos.ga.gov/Elections/voterhistory.do), but these do not include voters information. These need to be requested (and will be delivered on a CD) with this [form](http://sos.ga.gov/admin/uploads/Voter_List_Order_Form_june_2015v2.pdf) at a cost of $500. There's more information [here](http://sos.ga.gov/index.php/elections/order_voter_registration_lists_and_files). I also found [this github repo](https://github.com/stucka/voterhist) with python scripts to parse these files.

### Hawaii 
### Idaho 
### Illinois 
### Indiana 
### Iowa 
### :money_with_wings: Kansas 

Voter files can be requested from the [Office of the Secretary of State](http://www.kssos.org/elections/elections_registration.html) using the form [here](http://www.kssos.org/forms/elections/CVR.pdf). The full state costs $200 with additional costs for other options and delivery is by CD or email, depending on the request. 

### Kentucky 

I also found [this github repo](https://github.com/courierjournal/kentucky-voterdb-parser) with python scripts to parse these files.


### Louisiana 
### Maine 
### Maryland 
### Massachusetts 
### :smile: Michigan 

A copy of the voter list appears to be also available online for free on [this website](http://michiganvoters.info/download.html).

### Minnesota 
### Mississippi 
### Missouri 
### :money_with_wings: Montana 

The voter file is available online [here](https://app.mt.gov/voterfile/), but the cost of obtaining the statewide dataset is $1,000.

### Nebraska 
### :smile: Nevada 

The voter file is available online [here](http://nvsos.gov/index.aspx?page=332), but it is first necessary to send a signed official request via fax or mail.

### New Hampshire 
### New Jersey 

 I also found [this github repo](https://github.com/pwolanin/import-voters) with PHP scripts to parse these files.

### New Mexico 
### :smile: New York

There's an [online form to request voter registration data](http://form.jotform.us/form/50913672751154), documented on their [FOIL page](https://www.elections.ny.gov/FoilRequests.html). There's no cost, and data is sent on CD via USPS, arriving in about a week.

Repos on working with New York voter files:

- https://github.com/civic-data/NYS-Voter-File
- https://github.com/sajacy/nys-voters

### North Carolina 

- https://github.com/offensivepolitics/wake-county-voter-file-analysis
- http://dl.ncsbe.gov/
- http://dl.ncsbe.gov/index.html

### North Dakota 
### :smile: Ohio 



### :smile: Oklahoma 

A copy of the voter list appears to be also available online for free on [this website](http://oklavoters.com/download.html).

### :money_with_wings: Oregon 

The voter file can be requested [here](http://sos.oregon.gov/elections/Pages/data-request.aspx) at a cost of $500 for the statewide voter list.

### Pennsylvania 
### Rhode Island 

A copy of the voter list appears to be also available online for free on [this website](http://rivoters.com/).

### :money_with_wings: South Carolina 

The voter file is available online [here](http://www.scvotes.org/sale_of_voter_registration_lists), but the cost of obtaining the statewide dataset is $2,500.

### South Dakota 
### Tennessee 
### Texas 
### :money_with_wings: Utah 

The voter file can be requested [here](http://elections.utah.gov/voterdatabase) at a cost of $1,050. Note that this file does not include voters' birth dates. And old version of this file was available [here](http://utvoters.com/).

### Vermont 
### Virginia 
### :smile: Washington 

The Voter registration database is freely available for download [here](https://www.sos.wa.gov/elections/vrdb-download-form.aspx). A list of database fields can be found [here](http://www.sos.wa.gov/_assets/elections/VRDBDatabaseFields.pdf).

### West Virginia 
### :money_with_wings: Wisconsin

Voter files (sliced various ways, etc.) can be requested via an [online system](https://badgervoters.wi.gov/) ([documentation](https://elections.wi.gov/clerks/svrs/voter-data)) for $25 plus $5 per thousand voters, up to a maximum cost of $12,500.

### Wyoming

### Washington DC

Available on [this GitHub repository](https://github.com/ajschumacher/dc_voter_reg).
