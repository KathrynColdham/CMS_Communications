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
	      "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]")


for i in ${!ColumnsArray[@]}; do
        python 2D_DensityPlots.py --subset '2. In which age range do you fall under?' --compare "${ColumnsArray[i]}"
	python 2D_DensityPlots.py --subset '3. Are you currently resident (>50%) at CERN?' --compare "${ColumnsArray[i]}"
done
