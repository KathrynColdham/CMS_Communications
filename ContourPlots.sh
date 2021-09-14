#!/bin/bash

ColumnsArray=('9. How often do you read the following webpages? [CERN Document Server (CDS)]'
	      '9. How often do you read the following webpages? [cms.cern]'
	      '9. How often do you read the following webpages? [cmsdoc]'
	      '9. How often do you read the following webpages? [cms-info.web.cern.ch]'
	      '9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]'
	      '9. How often do you read the following webpages? [Confluence]'
	      '9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]'
	      '9. How often do you read the following webpages? [Hypernews - via web]'
	      '9. How often do you read the following webpages? [Inspire HEP]'
	      '9. How often do you read the following webpages? [Twiki pages]'
	      '10. How often do you use the following tools? [CERNBOX]'
	      '10. How often do you use the following tools? [CINCO]'
	      '10. How often do you use the following tools? [cmscentre]'
	      '10. How often do you use the following tools? [cmsonline]'
	      '10. How often do you use the following tools? [cms-talk.web.cern.ch]'
	      '10. How often do you use the following tools? [Collabora]'
	      '10. How often do you use the following tools? [CodiMD]'
	      '10. How often do you use the following tools? [DocDB]'
	      '10. How often do you use the following tools? [Drawio]'
	      '10. How often do you use the following tools? [e-groups]'
	      '10. How often do you use the following tools? [e-log]'
	      '10. How often do you use the following tools? [Email]'
	      '10. How often do you use the following tools? [Foswiki]'
	      '10. How often do you use the following tools? [Gantt viewer]'
	      '10. How often do you use the following tools? [GitHub]'
	      '10. How often do you use the following tools? [Gitlab]'
	      '10. How often do you use the following tools? [GoogleDocs]'
	      '10. How often do you use the following tools? [Hypernews via the web, not mail]'
	      '10. How often do you use the following tools? [iCMS]'
	      '10. How often do you use the following tools? [Indico]'
	      '10. How often do you use the following tools? [JIRA]'
	      '10. How often do you use the following tools? [MS Office]'
	      '10. How often do you use the following tools? [OnlyOffice]'
	      '10. How often do you use the following tools? [Overleaf]'
	      '10. How often do you use the following tools? [Zenodo/Invenio]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]'
	      '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]'
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
	      "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Other]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accesibility of information]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accuracy of content]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Amount of information]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Clarity of information]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of delivery of information]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of receipt of information]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Relevance of material]"
	      "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Style of presentation]")



if [ ! -d Results_ContourPlots ]; then
  mkdir Results_ContourPlots;
fi


for i in ${!ColumnsArray[@]}; do
        python3 ContourPlots.py --first '2. In which age range do you fall under?' --second "${ColumnsArray[i]}"
	python3 ContourPlots.py --first '3. Are you currently resident (>50%) at CERN?' --second "${ColumnsArray[i]}"
	python3 ContourPlots.py --first '4. If you are not resident at CERN, in which country are you based?' --second "${ColumnsArray[i]}"
	python3 ContourPlots.py --first '5. In which country is your home institute, if different from the country in which you are based?' --second "${ColumnsArray[i]}"
	python3 ContourPlots.py --first '6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?' --second "${ColumnsArray[i]}"
	#python3 ContourPlots.py --first '7. Which of the following areas of CMS are you involved in? ' --second "${ColumnsArray[i]}"
	#python3 ContourPlots.py --first '8. If you answered "other" for question 7, please list the area(s) of CMS that you are involved in here.' --second "${ColumnsArray[i]}"
done
