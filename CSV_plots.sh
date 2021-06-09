#!/bin/bash

PlotColumnsArray=("9. How often do you read the following webpages? [CERN Document Server (CDS)]")

		  "9. How often do you read the following webpages? [cms.cern]"
                  "9. How often do you read the following webpages? [cmsdoc]"
                  "9. How often do you read the following webpages? [cms-info.web.cern.ch]"
                  "9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]"
                  "9. How often do you read the following webpages? [Confluence]"
                  "9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]"
                  "9. How often do you read the following webpages? [Hypernews - via web]"
                  "9. How often do you read the following webpages? [Inspire HEP]"
                  "9. How often do you read the following webpages? [Twiki pages]"
                  "10. How often do you use the following tools? [CERNBOX]"
                  "10. How often do you use the following tools? [CINCO]"
                  "10. How often do you use the following tools? [cmscentre]"
                  "10. How often do you use the following tools? [cmsonline]"
                  "10. How often do you use the following tools? [cms-talk.web.cern.ch]"
                  "10. How often do you use the following tools? [Collabora]"
                  "10. How often do you use the following tools? [CodiMD]"
                  "10. How often do you use the following tools? [DocDB]"
                  "10. How often do you use the following tools? [Drawio]"
                  "10. How often do you use the following tools? [e-groups]"
                  "10. How often do you use the following tools? [e-log]"
                  "10. How often do you use the following tools? [Email]"
                  "10. How often do you use the following tools? [Foswiki]"
                  "10. How often do you use the following tools? [Gantt viewer]"
                  "10. How often do you use the following tools? [GitHub]"
                  "10. How often do you use the following tools? [Gitlab]"
                  "10. How often do you use the following tools? [GoogleDocs]"
                  "10. How often do you use the following tools? [Hypernews via the web, not mail]"
                  "10. How often do you use the following tools? [iCMS]"
                  "10. How often do you use the following tools? [Indico]"
                  "10. How often do you use the following tools? [JIRA]"
                  "10. How often do you use the following tools? [MS Office]"
                  "10. How often do you use the following tools? [OnlyOffice]"
                  "10. How often do you use the following tools? [Overleaf]"
                  "10. How often do you use the following tools? [Zenodo/Invenio]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]"
                  "11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]"
                  "12. How often do you read posts on the following social media accounts?  [CMS experiment's Facebook page (https://www.facebook.com/CMSexperiment/)]"
                  "12. How often do you read posts on the following social media accounts?  [CMS experiment's Twitter account (https://twitter.com/CMSExperiment)]"
                  "12. How often do you read posts on the following social media accounts?  [CMS experiment's Instagram account (https://www.instagram.com/cmsexperiment)]"
                  "12. How often do you read posts on the following social media accounts?  [CMS experiment's YouTube Channel (https://www.youtube.com/user/CMSExperimentTV )]"
                  "12. How often do you read posts on the following social media accounts?  [CMS Muon Group's Twitter account (https://twitter.com/CmsMuon)]"
                  "12. How often do you read posts on the following social media accounts?  [CMS Publications Twitter account (https://twitter.com/CMSpapers)]"
                  "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS awards]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS public briefings]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Conferences]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [General announcements]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Jobs]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Meetings]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Nominations]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Safety alerts]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Security alerts]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Social events]"
		  "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Publications]"
		  "15. In the past two years, how often do you attended/read/watched the following? [CMS Week Monday plenary ]"
		  "15. In the past two years, how often do you attended/read/watched the following? [Other CMS Week sessions]"
		  "15. In the past two years, how often do you attended/read/watched the following? [Weekly General Meeting]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Discord]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Facebook messenger]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Mattermost]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Skype]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Signal]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Slack]"
		  "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Whatsapp]"
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accesibility of information]"
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accuracy of content]"
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Amount of information]"	
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Clarity of information]"	
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of delivery of information]"	
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of receipt of information]"    
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Relevance of material]"	
		  "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Style of presentation]"



CollaborationLengthArray=("< 1" "1-2" "3-5" "6-10" "10+")

AgesArray=("18-25" "26-35" "36-45" "46-55" "56-65" "66-75" "75+")

PercentageAtCERNArray=("0-10%" "11-30%" "31-50%" ">50%")

CountryOfResidenceArray=("United States" "Italy"   "Germany"     "Belgium"  "Russia"     "United Kingdom"    "France" "India"    "Spain"   "Hungary" "Finland"
			 "Brazil" 	 "Austria" "Switzerland" "Mexico"   "Turkey"     "Lithuania"	     "Greece" "Bulgaria" "Albania" "Cyprus"  "Ecuador"
			 "Iran"		 "China"   "Poland"      "Thailand" "Afghanistan")

InstituteCountryArray=("United States"  "Italy"   "Germany"  "France" "Belgium" "Switzerland" "Austria" "United Kingdom"  "Russia"  "Spain"    "Brazil"  "India"
		       "Turkey"         "Finland" "Bulgaria" "Iran"   "Mexico"  "Cyprus"      "Ecuador" "China"	 	  "Croatia" "Colombia" "Hungary" "Lithuania"
		       "Poland"         "Serbia"  "Taiwan")


CMSAreasArray=("BRIL"                             "Collaboration Board"              "Communications" 
	       "DAQ"                              "ECAL"                             "Engagement Office" 
	       "Extended Executive Board (XEB)"   "HCAL"                             "HGCAL"		
               "L1 Trigger"                       "Management Board"                 "MTD"		    
	       "Muon Detector"                    "Offline Software and Computing"   "Physics coordination"
	       "PPD"                              "PPS"                              "Regional Representative"
	       "Run coordination"                 "Safety"                           "Secretariat"
	       "Technical coordination"           "Tracker"                          "Trigger coordination"
               "Other")


#CMS Area 
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[0]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[1]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[2]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[3]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[4]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[5]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[6]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[7]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[8]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[9]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[10]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[11]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[12]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[13]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[14]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[15]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[16]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[17]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[18]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[19]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[20]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[21]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[22]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "7. Which of the following areas of CMS are you involved in? " -c "${CMSAreasArray[23]}" -p "${PlotColumnsArray[i]}"
done

#Collaboration length
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "1. For how many years have you been a member of the CMS collaboration?" -c "${CollaborationLengthArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "1. For how many years have you been a member of the CMS collaboration?" -c "${CollaborationLengthArray[1]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "1. For how many years have you been a member of the CMS collaboration?" -c "${CollaborationLengthArray[2]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "1. For how many years have you been a member of the CMS collaboration?" -c "${CollaborationLengthArray[3]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "1. For how many years have you been a member of the CMS collaboration?" -c "${CollaborationLengthArray[4]}" -p "${PlotColumnsArray[i]}"
done

#Age
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[1]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[2]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[3]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[4]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[5]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "2. In which age range do you fall under?" -c "${AgesArray[6]}" -p "${PlotColumnsArray[i]}"
done


#Resident at CERN
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "3. Are you currently resident (>50%) at CERN?" -c "Yes" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "3. Are you currently resident (>50%) at CERN?" -c "No" -p "${PlotColumnsArray[i]}"
done

#Country based in, if not resident at CERN
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[0]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[1]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[2]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[3]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[4]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[5]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[6]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[7]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[8]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[9]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[10]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[11]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[12]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[13]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[14]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[15]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[16]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[17]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[18]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[19]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[20]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[21]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[22]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[23]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[24]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[25]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "4. If you are not resident at CERN, in which country are you based?" -c "${CountryOfResidenceArray[26]}" -p "${PlotColumnsArray[i]}"
done

#Home institute country
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[1]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[2]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[3]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[4]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[5]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[6]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[7]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[8]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[9]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[10]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[11]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[12]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[13]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[14]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[15]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[16]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[17]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[18]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[19]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[20]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[21]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[22]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[23]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[24]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[25]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[26]}" -p "${PlotColumnsArray[i]}"

	python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"
        python CSV_Reader_Subset.py -s "5. In which country is your home institute, if different from the country in which you are based?" -c "${InstituteCountryArray[0]}" -p "${PlotColumnsArray[i]}"

done 

#% presence at CERN pre-pandemic
for i in ${!PlotColumnsArray[@]}; do
        python CSV_Reader_Subset.py -s "6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?" -c "${PercentageAtCERNArray[0]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?" -c "${PercentageAtCERNArray[1]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?" -c "${PercentageAtCERNArray[2]}" -p "${PlotColumnsArray[i]}"
	python CSV_Reader_Subset.py -s "6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?" -c "${PercentageAtCERNArray[3]}" -p "${PlotColumnsArray[i]}"
done



