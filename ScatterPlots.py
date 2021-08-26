import tkinter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import os

#input arguments
parser = argparse.ArgumentParser()

parser.add_argument("-a", "--first", type=str, help="title of first column")
parser.add_argument("-b", "--second", type=str, help="name of column to compare to")

args = parser.parse_args()

Col1 = args.first
Col2 = args.second

#Different options for the column to take a subset of 
if Col1 == '2. In which age range do you fall under?' :
	end = ' by age'
	PdfTitleEnd = 'Age'
	axis_label = 'Age'
	FirstColumnNumber = 2
elif Col1 == '3. Are you currently resident (>50%) at CERN?' :
	end = ' by respondents resident at CERN or not'
	PdfTitleEnd = 'CERNResidency'
	axis_label = 'Resident at CERN?'
	FirstColumnNumber = 3
elif Col1 == '4. If you are not resident at CERN, in which country are you based?' :
	end = ' by country of residence'
	PdfTitleEnd = 'CountryOfResidenceIfNotResidentAtCERN'
	axis_label = 'Country'
	FirstColumnNumber = 4
elif Col1 == '5. In which country is your home institute, if different from the country in which you are based?' :
	end = ' by country of home institute'	
	PdfTitleEnd = 'HomeInstituteCountry'
	axis_label = 'Country'
	FirstColumnNumber = 5
elif Col1 == '6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?' :
	end = ' by % presence at CERN pre-pandemic'
	PdfTitleEnd = 'CERNPercentagePresence'
	axis_label = '% presence'
	FirstColumnNumber = 6
elif Col1 == '7. Which of the following areas of CMS are you involved in? ' :
	end = ' by CMS area'	
	PdfTitleEnd = 'CMSArea'
	axis_label = 'CMS Area'
	FirstColumnNumber = 7
elif Col1 == '8. If you answered "other" for question 7, please list the area(s) of CMS that you are involved in here.' :
	end = ' by CMS area (if other)'	
	PdfTitleEnd = 'CMSAreaOther'
	axis_label = 'CMS Area'
	FirstColumnNumber = 8
else:
        print('ERROR: Check the string for the first column name. Exiting.')
        quit()


#Different options for the column to compare with
#Setting the title
if Col2 == '9. How often do you read the following webpages? [CERN Document Server (CDS)]':
	title = 'How often CDS is read'
	PdfTitleStart = 'CDS'
	SecondColumnNumber = 9
elif Col2 == '9. How often do you read the following webpages? [cms.cern]':
	title = 'How often cms.cern is read'
	PdfTitleStart = 'cms.cern'
	SecondColumnNumber = 10
elif Col2 == '9. How often do you read the following webpages? [cmsdoc]':
	title = 'How often cmsdoc is read'
	PdfTitleStart = 'cmsdoc'
	SecondColumnNumber = 11
elif Col2 == '9. How often do you read the following webpages? [cms-info.web.cern.ch]':
	title = 'How often cms-info.web.cern.ch is read'
	PdfTitleStart = 'cmsinfo'
	SecondColumnNumber = 12
elif Col2 == '9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]':
	title = 'How often cms-secretariat.web.cern.ch is read'
	PdfTitleStart = 'cmssec'
	SecondColumnNumber = 13
elif Col2 == '9. How often do you read the following webpages? [Confluence]':
	title = 'How often Confluence is read'
	PdfTitleStart = 'confluence'
	SecondColumnNumber = 14
elif Col2 == '9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]':
	title = 'How often how-to docs and similar are read'	
	PdfTitleStart = 'HowToDocs'
	SecondColumnNumber = 15
elif Col2 == '9. How often do you read the following webpages? [Hypernews - via web]':
	title = 'How often Hypernews - via web is read'
	PdfTitleStart = 'HypernewsViaWebNotMail'
	SecondColumnNumber = 16
elif Col2 == '9. How often do you read the following webpages? [Inspire HEP]':
	title = 'How often Inspire HEP is read'
	PdfTitleStart = 'InspireHEP'
	SecondColumnNumber = 17
elif Col2 == '9. How often do you read the following webpages? [Twiki pages]':
	title = 'How often Twiki pages are read'
	PdfTitleStart = 'Twiki'
	SecondColumnNumber = 18
elif Col2 == '10. How often do you use the following tools? [CERNBOX]':
	title = 'How often CERNBOX is used'
	PdfTitleStart = 'CERNBox'
	SecondColumnNumber = 19
elif Col2 == '10. How often do you use the following tools? [CINCO]':
	title = 'How often CINCO is used'
	PdfTitleStart = 'CINCO'
	SecondColumnNumber = 20
elif Col2 == '10. How often do you use the following tools? [cmscentre]':
	title = 'How often cmscentre is used'
	PdfTitleStart = 'cmscentre'
	SecondColumnNumber = 21
elif Col2 == '10. How often do you use the following tools? [cmsonline]':
	title = 'How often cmsonline is used'
	PdfTitleStart = 'cmsonline'
	SecondColumnNumber = 21
elif Col2 == '10. How often do you use the following tools? [cms-talk.web.cern.ch]':
	title = 'How often cms-talk is used'
	PdfTitleStart = 'cmstalk'
	SecondColumnNumber = 23
elif Col2 == '10. How often do you use the following tools? [Collabora]':
	title = 'How often Collabora is used'
	PdfTitleStart = 'Collabora'
	SecondColumnNumber = 24
elif Col2 == '10. How often do you use the following tools? [CodiMD]':
	title = 'How often CodiMD is used'
	PdfTitleStart = 'CodiMD'
	SecondColumnNumber = 25
elif Col2 == '10. How often do you use the following tools? [DocDB]':
	title = 'How often DocDB is used'
	PdfTitleStart = 'DocDB'
	SecondColumnNumber = 26
elif Col2 == '10. How often do you use the following tools? [Drawio]':
	title = 'How often Drawio is used'
	PdfTitleStart = 'Drawio'
	SecondColumnNumber = 27
elif Col2 == '10. How often do you use the following tools? [e-groups]':
	title = 'How often e-groups are used'
	PdfTitleStart = 'egroups'
	SecondColumnNumber = 28
elif Col2 == '10. How often do you use the following tools? [e-log]':
	title = 'How often e-log is used'
	PdfTitleStart = 'elog'
	SecondColumnNumber = 29
elif Col2 == '10. How often do you use the following tools? [Email]':
	title = 'How often email is used'
	PdfTitleStart = 'email'
	SecondColumnNumber = 30
elif Col2 == '10. How often do you use the following tools? [Foswiki]':
	title = 'How often Foswiki is used'
	PdfTitleStart = 'Foswiki'
	SecondColumnNumber = 31
elif Col2 == '10. How often do you use the following tools? [Gantt viewer]':
	title = 'How often Gantt viewer is used'
	PdfTitleStart = 'GanttViewer'
	SecondColumnNumber = 32
elif Col2 == '10. How often do you use the following tools? [GitHub]':
	title = 'How often GitHub is used'
	PdfTitleStart = 'GitHub'
	SecondColumnNumber = 33
elif Col2 == '10. How often do you use the following tools? [Gitlab]':
	title = 'How often Gitlab is used'
	PdfTitleStart = 'Gitlab'
	SecondColumnNumber = 34
elif Col2 == '10. How often do you use the following tools? [GoogleDocs]':
	title = 'How often GoogleDocs are used'	
	PdfTitleStart = 'GoogleDocs'
	SecondColumnNumber = 35
elif Col2 == '10. How often do you use the following tools? [Hypernews via the web, not mail]':
	title = 'How often hypernews via the web (not mail) is used'	
	PdfTitleStart = 'HypernewsViaWebNotMail'
	SecondColumnNumber = 36
elif Col2 == '10. How often do you use the following tools? [iCMS]':
	title = 'How often iCMS is used'
	PdfTitleStart = 'iCMS'
	SecondColumnNumber = 37
elif Col2 == '10. How often do you use the following tools? [Indico]':
	title = 'How often Indico is used'
	PdfTitleStart = 'Indico'
	SecondColumnNumber = 38
elif Col2 == '10. How often do you use the following tools? [JIRA]':
	title = 'How often JIRA is used'
	PdfTitleStart = 'JIRA'
	SecondColumnNumber = 39
elif Col2 == '10. How often do you use the following tools? [MS Office]':
	title = 'How often MS Office is used'
	PdfTitleStart = 'MSOffice'
	SecondColumnNumber = 40
elif Col2 == '10. How often do you use the following tools? [OnlyOffice]':
	title = 'How often OnlyOffice is used'
	PdfTitleStart = 'OnlyOffice'
	SecondColumnNumber = 41
elif Col2 == '10. How often do you use the following tools? [Overleaf]':
	title = 'How often Overleaf is used'
	PdfTitleStart = 'Overleaf'
	SecondColumnNumber = 42
elif Col2 == '10. How often do you use the following tools? [Zenodo/Invenio]':
	title = 'How often Zenodo/Invenio is used'
	PdfTitleStart = 'Zenodo'
	SecondColumnNumber = 43
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]':
	title = 'How often Discord is used'
	PdfTitleStart = 'Discord'
	SecondColumnNumber = 44
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]':
	title = 'How often Facebook messenger is used'
	PdfTitleStart = 'FacebookMessenger'
	SecondColumnNumber = 45
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]':
	title = 'How often Mattermost is used'
	PdfTitleStart = 'Mattermost'
	SecondColumnNumber = 46
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]':
	title = 'How often Skype is used'
	PdfTitleStart = 'Skype'
	SecondColumnNumber = 47
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]':
	title = 'How often Signal is used'
	PdfTitleStart = 'Signal'
	SecondColumnNumber = 48
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]':
	title = 'How often Slack is used'
	PdfTitleStart = 'Slack'
	SecondColumnNumber = 49
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]':
	title = 'How often Whatsapp is used'
	PdfTitleStart = 'Whatsapp'
	SecondColumnNumber = 50
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]':
	title = 'How often Zoom is used'
	PdfTitleStart = 'Zoom'
	SecondColumnNumber = 51
elif Col2 == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]':
	title = 'How often Zulip is used'
	PdfTitleStart = 'Zulip'
	SecondColumnNumber = 52
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Facebook page (https://www.facebook.com/CMSexperiment/)]":
	title = "How often posts are read on the CMS experiment's Facebook page"
	PdfTitleStart = 'CMSExperimentFacebook'
	SecondColumnNumber = 53
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Twitter account (https://twitter.com/CMSExperiment)]":
	title = "How often posts are read on the CMS experiment's Twitter account"
	PdfTitleStart = 'CMSExperimentTwitter'
	SecondColumnNumber = 54
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Instagram account (https://www.instagram.com/cmsexperiment)]":
	title = "How often posts are read on the CMS experiment's Instagram account"
	PdfTitleStart = 'CMSExperimentInstagram'
	SecondColumnNumber = 55
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS experiment's YouTube Channel (https://www.youtube.com/user/CMSExperimentTV )]":
	title = "How often posts are read on the CMS experiment's YouTube channel"
	PdfTitleStart = 'CMSExperimentYouTube'
	SecondColumnNumber = 56
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS Muon Group's Twitter account (https://twitter.com/CmsMuon)]":
	title = "How often posts are read on the CMS Muon Group's Twitter account"
	PdfTitleStart = 'CMSMuonTwitter'
	SecondColumnNumber = 57
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS Publications Twitter account (https://twitter.com/CMSpapers)]":
	title = "How often posts are read on the CMS Publications Twitter account"
	PdfTitleStart = 'CMSPublicationsTwitter'
	SecondColumnNumber = 58
elif Col2 == "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]":
	title = "How often posts are read on the CMS Young Scientist Committee's Facebook group"
	PdfTitleStart = 'CMSYSCFacebook'
	SecondColumnNumber = 59
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS awards]":
	title = "Sources for receiving info about CMS awards"
	PdfTitleStart = 'CMSAwards'
	SecondColumnNumber = 60
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS public briefings]":
	title = "Sources for receiving info about CMS public briefings" 
	PdfTitleStart = 'Sources_CMSPublicBriefings' 
	SecondColumnNumber = 61 
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Conferences]":
	title = "Sources for receiving info about conferences"
	PdfTitleStart = 'Sources_Conferences'	
	SecondColumnNumber = 62
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [General announcements]":
	title = "Sources for receiving info about general announcements"	
	PdfTitleStart = 'Sources_GeneralAnnouncements'
	SecondColumnNumber = 63
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Jobs]":
	title = "Sources for receiving info about jobs"
	PdfTitleStart = 'Sources_Jobs'
	SecondColumnNumber = 64
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Meetings]":
	title = "Sources for receiving info about meetings"
	PdfTitleStart = 'Sources_Meetings'
	SecondColumnNumber = 65
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Nominations]":
	title = "Sources for receiving info about nominations"
	PdfTitleStart = 'Sources_Nominations'
	SecondColumnNumber = 66
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Safety alerts]":
	title = "Sources for receiving info about safety alerts"
	PdfTitleStart = 'Sources_SafetyAlerts'
	SecondColumnNumber = 67
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Security alerts]":
	title = "Sources for receiving info about security alerts"
	PdfTitleStart = 'Sources_SecurityAlerts'
	SecondColumnNumber = 68
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Social events]":
	title = "Sources for receiving info about social events"
	PdfTitleStart = 'Sources_SocialEvents'
	SecondColumnNumber = 69
elif Col2 == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Publications]":
	title = "Sources for receiving info about publications"
	PdfTitleStart = 'Sources_Publications'
	SecondColumnNumber = 70
elif Col2 == "15. In the past two years, how often do you attended/read/watched the following? [CMS Week Monday plenary ]":
	title = "Attendance of CMS Week Monday plenary"
	PdfTitleStart = 'Attendance_CMSWeekMondayPlenary'
	SecondColumnNumber = 72
elif Col2 == "15. In the past two years, how often do you attended/read/watched the following? [Other CMS Week sessions]":
	title = "Attendance of other CMS Week sessions"
	PdfTitleStart = "Attendance_OtherCMSWeekSessions"
	SecondColumnNumber = 73
elif Col2 == "15. In the past two years, how often do you attended/read/watched the following? [Weekly General Meeting]":
	title = "Attendance of the Weekly General Meeting"
	PdfTitleStart = 'Attendance_WGM'
	SecondColumnNumber = 74
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Discord]":
	title = "Preference of using Discord"
	PdfTitleStart = "Preference_Discord"
	SecondColumnNumber = 75
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Facebook messenger]":
	title = "Preference of using Facebook messenger"
	PdfTitleStart = 'Preference_FacebookMessenger'
	SecondColumnNumber = 76
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Mattermost]":
	title = "Preference of using Mattermost"
	PdfTitleStart = 'Preference_Mattermost'
	SecondColumnNumber = 77
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Skype]":
	title = "Preference of using Skype"
	PdfTitleStart = 'Preference_Skype'
	SecondColumnNumber = 78
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Signal]":
	title = "Preference of using Signal"
	PdfTitleStart = 'Preference_Signal'
	SecondColumnNumber = 79
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Slack]":
	title = "Preference of using Slack"
	PdfTitleStart = 'Preference_Slack'
	SecondColumnNumber = 80
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Whatsapp]":
	title = "Preference of using Whatsapp"
	PdfTitleStart = 'Preference_Whatsapp'
	SecondColumnNumber = 81
elif Col2 == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Other]":
	title = "Preference of using other messaging applications"
	PdfTitleStart = 'Preference_Other'
	SecondColumnNumber = 82
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accesibility of information]":
	title = "Satisfaction of accessibility of information" 
	PdfTitleStart = "Satisfaction_AccessibilityOfInfo"
	SecondColumnNumber = 84
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accuracy of content]":
	title = "Satisfaction of accuracy of content"
	PdfTitleStart = "Satisfaction_AccuracyOfContent"
	SecondColumnNumber = 85
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Amount of information]":
	title = "Satisfaction of amount of information"
	PdfTitleStart = "Satisfaction_AmountOfInfo"
	SecondColumnNumber = 86
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Clarity of information]":
	title = "Satisfaction of clarity of information"
	PdfTitleStart = "Satisfaction_ClarityOfInfo"
	SecondColumnNumber = 87
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of delivery of information]":
	title = "Satisfaction of the frequency of delivery of information"
	PdfTitleStart = "Satisfaction_FrequencyOfDelivery"	
	SecondColumnNumber = 88
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of receipt of information]":
	title = "Satisfaction of the frequency of receipt of information"
	PdfTitleStart = "Satisfaction_FrequencyOfReceipt"
	SecondColumnNumber = 89
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Relevance of material]":
	title = "Satisfaction of the relevance of material"
	PdfTitleStart = "Satisfaction_RelevanceOfMaterial"
	SecondColumnNumber = 90
elif Col2 == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Style of presentation]":
	title = "Satisfaction of the style of presentation"
	PdfTitleStart = "Satisfaction_StyleOfPresentation"
	SecondColumnNumber = 91 
else:
	print('ERROR: Check the string for the second column name. Exiting.')
	quit()

def reader(filename):

	# Read the data file
	df_original = pd.read_csv(filename)

	if FirstColumnNumber != 7 and FirstColumnNumber != 8:

		# Sort by the two relevant columns
		df = df_original.sort_values(by=[Col1, Col2])

		# Skim the dataframe
		df = df[[Col1, Col2]]

		# Count and remove duplicates
		df = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:"Counts"})

		# Form an numpy array
		np_arr = df.values

		#print('np_arr = ',np_arr)

		# Split into three
		x = np_arr[:, 0]
		y = np_arr[:, 1]
		counts = np_arr[:, 2]

		index = 0
	
		counts_new = []
	
		#Converting to percentages
		for i in x:
			Total = df_original[df_original[Col1] == i].shape[0] #to get the total number of respondents for each category (e.g. each age category)
			new_value = (counts[index]/Total) * 100
			counts_new.append(new_value)
			index += 1

		# Protection for nans
		where_are_NaNs = pd.isna(x)
		x[where_are_NaNs] = "nan"

		# Make the plot
		sc = plt.scatter(x, y, c=counts_new, cmap=matplotlib.cm.viridis, marker="s")

	else:

		# initialise empty data frame
		new_responses = pd.DataFrame()

		# go through each row of responses
		for i in range(len(df_original)): 

    			#select one row
			row = df_original.iloc[i,:]

    			# split their work areas into a list of values by splitting on the comma
			work_areas = df_original.iloc[i,FirstColumnNumber].split(",")

    			# some of the responses have an extra space, make sure to strip that so ' Ecal' and 'Ecal' are counted as the same
			work_areas = [word.strip() for word in work_areas]

    			# create a new temprary data frame that is a copy of the row in question repeated the same amount of times
    			# as the length of their work area list 
			tmp = pd.DataFrame([row]*len(work_areas))

    			# now change the work area for that data frame into the list of work areas 
			tmp.iloc[:,FirstColumnNumber] =  work_areas

    			# append that data frame 
			new_responses = new_responses.append(tmp)
    
		counts = new_responses.groupby([Col2, Col1]).agg({Col1:'count'})

		# convert to percentage
		new_counts = counts.groupby(level=1).apply(lambda x:100 * x / float(x.sum()))

		# Make the plot
		sc = plt.scatter(new_counts.index.get_level_values(1), new_counts.index.get_level_values(0), c=new_counts.values.flatten(), cmap=plt.cm.viridis, marker="s")

	# Cosmetics
	plt.title(title + end)
	plt.xlabel(axis_label)
	plt.ylabel("Frequency")
	plt.xticks(rotation = 90)

	# Colour bar
	cbar= plt.colorbar(sc)
	cbar.set_label("Responses (%)", labelpad=+5)

	# Save the plot
	if not os.path.exists('Results_ScatterPlots'):
		os.mkdir('Results_ScatterPlots')
	
	os.chdir('Results_ScatterPlots')
	plt.savefig('ScatterPlot_' + PdfTitleStart + '_' + PdfTitleEnd + '.pdf', bbox_inches='tight')
	

if __name__ == '__main__':
	reader('CMSInternalCommunicationsFeedbackForm.csv')


