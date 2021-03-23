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


### :money_with_wings: Alabama 

The [Secretary of State](https://www.sos.alabama.gov/alabama-votes) links to an [interactive site](https://www.alabamainteractive.org/sos/voter/voterWelcome.action) that searches by multiple critiera and provides an instant price. As of March 2021, there were 3.5M active voters for a cost of $35K.

### Alaska 

It appears to be possible to [request it via email](http://www.elections.alaska.gov/er_lr.php). A list with contact information is [here](http://www.elections.alaska.gov/csm_contact_reo.php).
### :money_with_wings: Arizona 

Costs used to be much higher, but are now somewhat lower due to a [lawsuit](https://www.azcentral.com/story/news/politics/arizona/2017/06/29/arizona-settles-lawsuit-voter-registration-data-lower-cost-project-vote/437629001/).

Individual county recorders offices [are responsible](https://law.justia.com/codes/arizona/2011/title16/section16-166/) for maintaining the permenant voter files in AZ.

- [Apache County](https://www.co.apache.az.us/wp-content/uploads/2018/08/Voter-Records-request-Public-Records.pdf)
- [Cochise County](https://www.cochise.az.gov/recorder/downloads)
- [Coconino County](http://coconino.az.gov/195/Elections) (Unclear if available)
- [Gila County](http://www.gilacountyaz.gov/government/recorder/docs/Request%20for%20Information%202018.pdf)
- [Graham County](https://www.graham.az.gov/DocumentCenter/View/593/Voter-Data-Request-PDF)
- [Greenlee County](https://www.co.greenlee.az.us/recorder/pdfs/Public%20Records%20Request.pdf)
- [La Paz County](http://www.co.la-paz.az.us/213/Recorder) (Unclear if available)
- [Maricopa County](https://recorder.maricopa.gov/pdf/voterpublicdatarecordrequest.pdf)
- [Mohave County](https://www.mohavecounty.us/default.aspx#) (Unclear if available)
- [Navajo County](http://www.navajocountyaz.gov/Departments/Elections/Voter-Information) (Unclear if available)
- [Pima County](http://webcms.pima.gov/government/elections_department/) (Unclear if available)
- [Pinal County](http://www.pinalcountyaz.gov/elections/Documents/PublicRecordsRequest.pdf)
- [Santa Cruz County](https://www.santacruzcountyaz.gov/287/Recorder) (Unclear if available)
- [Yavapai County](http://www.yavapai.us/Portals/26/Forms/PublicDataRequestNon-Commercial.pdf)
- [Yuma County](https://www.yumacountyaz.gov/government/recorder) (Unclear if available)

### :smile: Arkansas 

The voter registration file can be requested using the form [here](https://www.sos.arkansas.gov/uploads/elections/Data%20Request%20Form.pdf), which has to be mailed along with $2.50 per file. A copy of the voter list appears to be also available online for free on [this website](https://arkvoters.com/download.html).

### California 

http://www.sos.ca.gov/elections/contact/email-elections-division/

### :smile: Colorado 

The registed voter list and voter history list can be requested using the form [here](http://www.sos.state.co.us/pubs/elections/forms/dataRequests.pdf), at a cost of [$50 each](http://www.sos.state.co.us/pubs/info_center/fees/elections.html). There appears to be a free copy of all the files on [this website](http://coloradovoters.info/download.html) as well.

### :smile: Connecticut 

The voter registry file can be purchased at a cost of $300 by contacting the Secrety of State as detailed [here](http://www.ct.gov/sots/cwp/view.asp?a=3179&q=532994). A copy of the voter list appears to be also available online for free on [this website](http://connvoters.com/download.html).

### :smile: Delaware 

The voter file can be requested using the form [here](https://elections.delaware.gov/services/candidate/pdfs/Statewide%20CD%20Order%20Form.pdf), at a cost of $10 (in CD format). A copy of the voter list appears to be also available online for free on [this website](http://delawarevoters.info/downloads.html).

### :smile: Florida 

The voter file can be requested using the form [here](http://dos.myflorida.com/elections/data-statistics/voter-registration-statistics/voter-registration-file-request/), at a cost of $5 (in CD format). A copy of the voter list appears to be also available online for free on [this website](http://flvoters.com/downloads.html).

### :money_with_wings: Georgia 

Voter history files are freely available [here](http://elections.sos.ga.gov/Elections/voterhistory.do), but these do not include voters information. These need to be requested (and will be delivered on a CD) with this [form](http://sos.ga.gov/admin/uploads/Voter_List_Order_Form_june_2015v2.pdf) at a cost of $500. There's more information [here](http://sos.ga.gov/index.php/elections/order_voter_registration_lists_and_files). I also found [this github repo](https://github.com/stucka/voterhist) with python scripts to parse these files.

### Hawaii 
### Idaho 

The Idaho voter file is available through a public records request for non-commercial purposes. The Secratary of State provides the following statement on [their FAQ](https://idahovotes.gov/faq/):
> "Idaho law requires the Secretary of State’s office to provide this information in response to public records requests."

### Illinois 

Illinois makes their voter information available via paper medium "for election, scholarly, journalistic, political or governmental purposes"[1](https://www.cookcountyclerk.com/service/registration-file-requests) Digital records are available to political organizations that complete a [D-1 Statement of Organization](https://www.elections.il.gov/downloads/campaigndisclosure/pdf/d1.pdf).

### :money_with_wings: Indiana 

Indiana makes computerized access to the list available to political parties and media organizations, along with elected officials. A request must be made to the
Indiana Election Division. The "election division shall charge each person [...] an annual subscription fee of five thousand dollars ($5,000)" More information can be found in the [Indiana Code](http://iga.in.gov/legislative/laws/2020/ic/titles/003#3-7-26.3-4).

### :money_with_wings: Iowa 

Individuals can request an Iowa statewide voter registration list through the Iowa Secratary of State [here](https://sos.iowa.gov/elections/voterreg/voterlistrequests.html). The statewide list with updates is provided at the cost of $1,500 a year.

### :money_with_wings: Kansas 

Voter files can be requested from the [Office of the Secretary of State](http://www.kssos.org/elections/elections_registration.html) using the form [here](http://www.kssos.org/forms/elections/CVR.pdf). The full state costs $200 with additional costs for other options and delivery is by CD or email, depending on the request. 

### Kentucky 

I also found [this github repo](https://github.com/courierjournal/kentucky-voterdb-parser) with python scripts to parse these files.


### :money_with_wings: Louisiana 

Statewide lists are available to approved entities upon request at a cost not to exceed $5,000. Requests must be made through the Secratary of State's [web request application](https://voterportal.sos.la.gov/commercialrequests).

[Document](https://www.sos.la.gov/ElectionsAndVoting/PublishedDocuments/ConvertingTextFileToExcelFile.pdf) detailing how to convert the tab delimited file to an Excel document.
Voter list [cost information](https://www.sos.la.gov/ElectionsAndVoting/PublishedDocuments/VoterListChargesAndInfo.pdf).

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

### :money_with_wings: West Virginia 

Voter files can be requested in various ways by filling [out a form](https://sos.wv.gov/FormSearch/Elections/Informational/voter%20data%20request%20071213.pdf) and returning it to the West Virginia's Secratary of State's office via fax, email, or mail.  
The exports come in a variety of options including the statewide voter registration list for $500 and the master voter history list for $500. 

### :money_with_wings: Wisconsin

Voter files (sliced various ways, etc.) can be requested via an [online system](https://badgervoters.wi.gov/) ([documentation](https://elections.wi.gov/clerks/svrs/voter-data)) for $25 plus $5 per thousand voters, up to a maximum cost of $12,500.

### Wyoming

### Washington DC

Available on [this GitHub repository](https://github.com/ajschumacher/dc_voter_reg).
