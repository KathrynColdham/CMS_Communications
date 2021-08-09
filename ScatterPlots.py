import tkinter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import os

#input arguments
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--subset", type=str, help="title of column to take a subset of rows of")
parser.add_argument("-c", "--compare", type=str, help="name of column to compare to")

args = parser.parse_args()

SubsetColumn = args.subset
CompareColumn = args.compare

#Different options for the column to take a subset of 
if SubsetColumn == '2. In which age range do you fall under?' :
	end = ' by age'
	PdfTitleEnd = 'Age'
	axis_label = 'Age'
	FirstColumnNumber = 2
elif SubsetColumn == '3. Are you currently resident (>50%) at CERN?' :
	end = ' by respondents resident at CERN or not'
	PdfTitleEnd = 'CERNResidency'
	axis_label = 'Resident at CERN?'
	FirstColumnNumber = 3
elif SubsetColumn == '4. If you are not resident at CERN, in which country are you based?' :
	end = ' by country of residence'
	PdfTitleEnd = 'CountryOfResidenceIfNotResidentAtCERN'
	axis_label = 'Country'
	FirstColumnNumber = 4
elif SubsetColumn == '5. In which country is your home institute, if different from the country in which you are based?' :
	end = ' by country of home institute'	
	PdfTitleEnd = 'HomeInstituteCountry'
	axis_label = 'Country'
	FirstColumnNumber = 5
elif SubsetColumn == '6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?' :
	end = ' by % presence at CERN pre-pandemic'
	PdfTitleEnd = 'CERNPercentagePresence'
	axis_label = '% presence'
	FirstColumnNumber = 6
elif SubsetColumn == '7. Which of the following areas of CMS are you involved in? ' :
	end = ' by CMS area'	
	PdfTitleEnd = 'CMSArea'
	axis_label = 'CMS Area'
	FirstColumnNumber = 7
elif SubsetColumn == '8. If you answered "other" for question 7, please list the area(s) of CMS that you are involved in here.' :
	end = ' by CMS area (if other)'	
	PdfTitleEnd = 'CMSAreaOther'
	axis_label = 'CMS Area'
	FirstColumnNumber = 8
else:
        print('ERROR: Check the --subset string. Exiting.')
        quit()


#Different options for the column to compare with
#Setting the title
if CompareColumn == '9. How often do you read the following webpages? [CERN Document Server (CDS)]':
	title = 'How often CDS is read'
	PdfTitleStart = 'CDS'
	SecondColumnNumber = 9
elif CompareColumn == '9. How often do you read the following webpages? [cms.cern]':
	title = 'How often cms.cern is read'
	PdfTitleStart = 'cms.cern'
	SecondColumnNumber = 10
elif CompareColumn == '9. How often do you read the following webpages? [cmsdoc]':
	title = 'How often cmsdoc is read'
	PdfTitleStart = 'cmsdoc'
	SecondColumnNumber = 11
elif CompareColumn == '9. How often do you read the following webpages? [cms-info.web.cern.ch]':
	title = 'How often cms-info.web.cern.ch is read'
	PdfTitleStart = 'cmsinfo'
	SecondColumnNumber = 12
elif CompareColumn == '9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]':
	title = 'How often cms-secretariat.web.cern.ch is read'
	PdfTitleStart = 'cmssec'
	SecondColumnNumber = 13
elif CompareColumn == '9. How often do you read the following webpages? [Confluence]':
	title = 'How often Confluence is read'
	PdfTitleStart = 'confluence'
	SecondColumnNumber = 14
elif CompareColumn == '9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]':
	title = 'How often how-to docs and similar are read'	
	PdfTitleStart = 'HowToDocs'
	SecondColumnNumber = 15
elif CompareColumn == '9. How often do you read the following webpages? [Hypernews - via web]':
	title = 'How often Hypernews - via web is read'
	PdfTitleStart = 'HypernewsViaWebNotMail'
	SecondColumnNumber = 16
elif CompareColumn == '9. How often do you read the following webpages? [Inspire HEP]':
	title = 'How often Inspire HEP is read'
	PdfTitleStart = 'InspireHEP'
	SecondColumnNumber = 17
elif CompareColumn == '9. How often do you read the following webpages? [Twiki pages]':
	title = 'How often Twiki pages are read'
	PdfTitleStart = 'Twiki'
	SecondColumnNumber = 18
elif CompareColumn == '10. How often do you use the following tools? [CERNBOX]':
	title = 'How often CERNBOX is used'
	PdfTitleStart = 'CERNBox'
	SecondColumnNumber = 19
elif CompareColumn == '10. How often do you use the following tools? [CINCO]':
	title = 'How often CINCO is used'
	PdfTitleStart = 'CINCO'
	SecondColumnNumber = 20
elif CompareColumn == '10. How often do you use the following tools? [cmscentre]':
	title = 'How often cmscentre is used'
	PdfTitleStart = 'cmscentre'
	SecondColumnNumber = 21
elif CompareColumn == '10. How often do you use the following tools? [cmsonline]':
	title = 'How often cmsonline is used'
	PdfTitleStart = 'cmsonline'
	SecondColumnNumber = 21
elif CompareColumn == '10. How often do you use the following tools? [cms-talk.web.cern.ch]':
	title = 'How often cms-talk is used'
	PdfTitleStart = 'cmstalk'
	SecondColumnNumber = 23
elif CompareColumn == '10. How often do you use the following tools? [Collabora]':
	title = 'How often Collabora is used'
	PdfTitleStart = 'Collabora'
	SecondColumnNumber = 24
elif CompareColumn == '10. How often do you use the following tools? [CodiMD]':
	title = 'How often CodiMD is used'
	PdfTitleStart = 'CodiMD'
	SecondColumnNumber = 25
elif CompareColumn == '10. How often do you use the following tools? [DocDB]':
	title = 'How often DocDB is used'
	PdfTitleStart = 'DocDB'
	SecondColumnNumber = 26
elif CompareColumn == '10. How often do you use the following tools? [Drawio]':
	title = 'How often Drawio is used'
	PdfTitleStart = 'Drawio'
	SecondColumnNumber = 27
elif CompareColumn == '10. How often do you use the following tools? [e-groups]':
	title = 'How often e-groups are used'
	PdfTitleStart = 'egroups'
	SecondColumnNumber = 28
elif CompareColumn == '10. How often do you use the following tools? [e-log]':
	title = 'How often e-log is used'
	PdfTitleStart = 'elog'
	SecondColumnNumber = 29
elif CompareColumn == '10. How often do you use the following tools? [Email]':
	title = 'How often email is used'
	PdfTitleStart = 'email'
	SecondColumnNumber = 30
elif CompareColumn == '10. How often do you use the following tools? [Foswiki]':
	title = 'How often Foswiki is used'
	PdfTitleStart = 'Foswiki'
	SecondColumnNumber = 31
elif CompareColumn == '10. How often do you use the following tools? [Gantt viewer]':
	title = 'How often Gantt viewer is used'
	PdfTitleStart = 'GanttViewer'
	SecondColumnNumber = 32
elif CompareColumn == '10. How often do you use the following tools? [GitHub]':
	title = 'How often GitHub is used'
	PdfTitleStart = 'GitHub'
	SecondColumnNumber = 33
elif CompareColumn == '10. How often do you use the following tools? [Gitlab]':
	title = 'How often Gitlab is used'
	PdfTitleStart = 'Gitlab'
	SecondColumnNumber = 34
elif CompareColumn == '10. How often do you use the following tools? [GoogleDocs]':
	title = 'How often GoogleDocs are used'	
	PdfTitleStart = 'GoogleDocs'
	SecondColumnNumber = 35
elif CompareColumn == '10. How often do you use the following tools? [Hypernews via the web, not mail]':
	title = 'How often hypernews via the web (not mail) is used'	
	PdfTitleStart = 'HypernewsViaWebNotMail'
	SecondColumnNumber = 36
elif CompareColumn == '10. How often do you use the following tools? [iCMS]':
	title = 'How often iCMS is used'
	PdfTitleStart = 'iCMS'
	SecondColumnNumber = 37
elif CompareColumn == '10. How often do you use the following tools? [Indico]':
	title = 'How often Indico is used'
	PdfTitleStart = 'Indico'
	SecondColumnNumber = 38
elif CompareColumn == '10. How often do you use the following tools? [JIRA]':
	title = 'How often JIRA is used'
	PdfTitleStart = 'JIRA'
	SecondColumnNumber = 39
elif CompareColumn == '10. How often do you use the following tools? [MS Office]':
	title = 'How often MS Office is used'
	PdfTitleStart = 'MSOffice'
	SecondColumnNumber = 40
elif CompareColumn == '10. How often do you use the following tools? [OnlyOffice]':
	title = 'How often OnlyOffice is used'
	PdfTitleStart = 'OnlyOffice'
	SecondColumnNumber = 41
elif CompareColumn == '10. How often do you use the following tools? [Overleaf]':
	title = 'How often Overleaf is used'
	PdfTitleStart = 'Overleaf'
	SecondColumnNumber = 42
elif CompareColumn == '10. How often do you use the following tools? [Zenodo/Invenio]':
	title = 'How often Zenodo/Invenio is used'
	PdfTitleStart = 'Zenodo'
	SecondColumnNumber = 43
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]':
	title = 'How often Discord is used'
	PdfTitleStart = 'Discord'
	SecondColumnNumber = 44
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]':
	title = 'How often Facebook messenger is used'
	PdfTitleStart = 'FacebookMessenger'
	SecondColumnNumber = 45
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]':
	title = 'How often Mattermost is used'
	PdfTitleStart = 'Mattermost'
	SecondColumnNumber = 46
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]':
	title = 'How often Skype is used'
	PdfTitleStart = 'Skype'
	SecondColumnNumber = 47
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]':
	title = 'How often Signal is used'
	PdfTitleStart = 'Signal'
	SecondColumnNumber = 48
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]':
	title = 'How often Slack is used'
	PdfTitleStart = 'Slack'
	SecondColumnNumber = 49
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]':
	title = 'How often Whatsapp is used'
	PdfTitleStart = 'Whatsapp'
	SecondColumnNumber = 50
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]':
	title = 'How often Zoom is used'
	PdfTitleStart = 'Zoom'
	SecondColumnNumber = 51
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]':
	title = 'How often Zulip is used'
	PdfTitleStart = 'Zulip'
	SecondColumnNumber = 52
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Facebook page (https://www.facebook.com/CMSexperiment/)]":
	title = "How often posts are read on the CMS experiment's Facebook page"
	PdfTitleStart = 'CMSExperimentFacebook'
	SecondColumnNumber = 53
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Twitter account (https://twitter.com/CMSExperiment)]":
	title = "How often posts are read on the CMS experiment's Twitter account"
	PdfTitleStart = 'CMSExperimentTwitter'
	SecondColumnNumber = 54
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Instagram account (https://www.instagram.com/cmsexperiment)]":
	title = "How often posts are read on the CMS experiment's Instagram account"
	PdfTitleStart = 'CMSExperimentInstagram'
	SecondColumnNumber = 55
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's YouTube Channel (https://www.youtube.com/user/CMSExperimentTV )]":
	title = "How often posts are read on the CMS experiment's YouTube channel"
	PdfTitleStart = 'CMSExperimentYouTube'
	SecondColumnNumber = 56
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Muon Group's Twitter account (https://twitter.com/CmsMuon)]":
	title = "How often posts are read on the CMS Muon Group's Twitter account"
	PdfTitleStart = 'CMSMuonTwitter'
	SecondColumnNumber = 57
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Publications Twitter account (https://twitter.com/CMSpapers)]":
	title = "How often posts are read on the CMS Publications Twitter account"
	PdfTitleStart = 'CMSPublicationsTwitter'
	SecondColumnNumber = 58
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]":
	title = "How often posts are read on the CMS Young Scientist Committee's Facebook group"
	PdfTitleStart = 'CMSYSCFacebook'
	SecondColumnNumber = 59
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS awards]":
	title = "Sources for receiving info about CMS awards"
	PdfTitleStart = 'CMSAwards'
	SecondColumnNumber = 60
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS public briefings]":
	title = "Sources for receiving info about CMS public briefings" 
	PdfTitleStart = 'Sources_CMSPublicBriefings' 
	SecondColumnNumber = 61 
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Conferences]":
	title = "Sources for receiving info about conferences"
	PdfTitleStart = 'Sources_Conferences'	
	SecondColumnNumber = 62
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [General announcements]":
	title = "Sources for receiving info about general announcements"	
	PdfTitleStart = 'Sources_GeneralAnnouncements'
	SecondColumnNumber = 63
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Jobs]":
	title = "Sources for receiving info about jobs"
	PdfTitleStart = 'Sources_Jobs'
	SecondColumnNumber = 64
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Meetings]":
	title = "Sources for receiving info about meetings"
	PdfTitleStart = 'Sources_Meetings'
	SecondColumnNumber = 65
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Nominations]":
	title = "Sources for receiving info about nominations"
	PdfTitleStart = 'Sources_Nominations'
	SecondColumnNumber = 66
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Safety alerts]":
	title = "Sources for receiving info about safety alerts"
	PdfTitleStart = 'Sources_SafetyAlerts'
	SecondColumnNumber = 67
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Security alerts]":
	title = "Sources for receiving info about security alerts"
	PdfTitleStart = 'Sources_SecurityAlerts'
	SecondColumnNumber = 68
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Social events]":
	title = "Sources for receiving info about social events"
	PdfTitleStart = 'Sources_SocialEvents'
	SecondColumnNumber = 69
elif CompareColumn == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Publications]":
	title = "Sources for receiving info about publications"
	PdfTitleStart = 'Sources_Publications'
	SecondColumnNumber = 70
elif CompareColumn == "15. In the past two years, how often do you attended/read/watched the following? [CMS Week Monday plenary ]":
	title = "Attendance of CMS Week Monday plenary"
	PdfTitleStart = 'Attendance_CMSWeekMondayPlenary'
	SecondColumnNumber = 72
elif CompareColumn == "15. In the past two years, how often do you attended/read/watched the following? [Other CMS Week sessions]":
	title = "Attendance of other CMS Week sessions"
	PdfTitleStart = "Attendance_OtherCMSWeekSessions"
	SecondColumnNumber = 73
elif CompareColumn == "15. In the past two years, how often do you attended/read/watched the following? [Weekly General Meeting]":
	title = "Attendance of the Weekly General Meeting"
	PdfTitleStart = 'Attendance_WGM'
	SecondColumnNumber = 74
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Discord]":
	title = "Preference of using Discord"
	PdfTitleStart = "Preference_Discord"
	SecondColumnNumber = 75
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Facebook messenger]":
	title = "Preference of using Facebook messenger"
	PdfTitleStart = 'Preference_FacebookMessenger'
	SecondColumnNumber = 76
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Mattermost]":
	title = "Preference of using Mattermost"
	PdfTitleStart = 'Preference_Mattermost'
	SecondColumnNumber = 77
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Skype]":
	title = "Preference of using Skype"
	PdfTitleStart = 'Preference_Skype'
	SecondColumnNumber = 78
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Signal]":
	title = "Preference of using Signal"
	PdfTitleStart = 'Preference_Signal'
	SecondColumnNumber = 79
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Slack]":
	title = "Preference of using Slack"
	PdfTitleStart = 'Preference_Slack'
	SecondColumnNumber = 80
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Whatsapp]":
	title = "Preference of using Whatsapp"
	PdfTitleStart = 'Preference_Whatsapp'
	SecondColumnNumber = 81
elif CompareColumn == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Other]":
	title = "Preference of using other messaging applications"
	PdfTitleStart = 'Preference_Other'
	SecondColumnNumber = 82
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accesibility of information]":
	title = "Satisfaction of accessibility of information" 
	PdfTitleStart = "Satisfaction_AccessibilityOfInfo"
	SecondColumnNumber = 84
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accuracy of content]":
	title = "Satisfaction of accuracy of content"
	PdfTitleStart = "Satisfaction_AccuracyOfContent"
	SecondColumnNumber = 85
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Amount of information]":
	title = "Satisfaction of amount of information"
	PdfTitleStart = "Satisfaction_AmountOfInfo"
	SecondColumnNumber = 86
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Clarity of information]":
	title = "Satisfaction of clarity of information"
	PdfTitleStart = "Satisfaction_ClarityOfInfo"
	SecondColumnNumber = 87
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of delivery of information]":
	title = "Satisfaction of the frequency of delivery of information"
	PdfTitleStart = "Satisfaction_FrequencyOfDelivery"	
	SecondColumnNumber = 88
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of receipt of information]":
	title = "Satisfaction of the frequency of receipt of information"
	PdfTitleStart = "Satisfaction_FrequencyOfReceipt"
	SecondColumnNumber = 89
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Relevance of material]":
	title = "Satisfaction of the relevance of material"
	PdfTitleStart = "Satisfaction_RelevanceOfMaterial"
	SecondColumnNumber = 90
elif CompareColumn == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Style of presentation]":
	title = "Satisfaction of the style of presentation"
	PdfTitleStart = "Satisfaction_StyleOfPresentation"
	SecondColumnNumber = 91 
else:
	print('ERROR: Check the name of the column you want to compare to')
	quit()

def reader(filename):
	df = pd.read_csv(filename)
	df = df.sort_values(by=[SubsetColumn, CompareColumn])
	np_arr = df.values
	x_1 = np_arr[:, FirstColumnNumber]
	y_1 = np_arr[:, SecondColumnNumber]
	#np.where(pd.isna(x_1), "No response", x_1) #if the array contains nan values, convert them into strings
	where_are_NaNs = pd.isna(x_1)
	print('where_are_NaNs = ', where_are_NaNs)
	x_1[where_are_NaNs] = 'nan'
	print('x_1 = ',x_1)
	plt.scatter(x_1, y_1, color='green', marker="s", alpha=0.3)
	plt.title(title + end)
	plt.xlabel(axis_label)
	plt.ylabel('Frequency')
	plt.xticks(rotation = 90)
	
	if not os.path.exists('Results_ScatterPlots'):
		os.mkdir('Results_ScatterPlots')

	os.chdir('Results_ScatterPlots')
	plt.savefig('ScatterPlot_' + PdfTitleStart + '_' + PdfTitleEnd + '.pdf')

if __name__ == '__main__':
	reader('CMSInternalCommunicationsFeedbackForm.csv')

