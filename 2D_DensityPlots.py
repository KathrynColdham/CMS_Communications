import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

#input arguments
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--subset", type=str, help="title of column to take a subset of rows of")
parser.add_argument("-c", "--compare", type=str, help="name of column to compare to")

args = parser.parse_args()

SubsetColumn = args.subset
CompareColumn = args.compare

#input csv file 
df = pd.read_csv("CMSInternalCommunicationsFeedbackForm.csv", index_col=0)

#2D array for the axes
if SubsetColumn == '2. In which age range do you fall under?' :
	Array_2D = [['16-25', '26-35', '36-45', '46-55', '56-65', '66-75', '75+'], ['Never heard of it', 'Never', 'Occasionally', 'Often']]
elif SubsetColumn == '3. Are you currently resident (>50%) at CERN?' :
	Array_2D = [['Yes', 'No'], ['Never heard of it', 'Never', 'Occasionally', 'Often']]
else:
	print('ERROR: Check the --subset string. Exiting.')
	quit()

#creating an empty 4x7 array
w, h = 7, 4;
Array = [[0 for x in range(w)] for y in range(h)] 


#filling the array
for i in range(len(Array_2D[0])):

	Age_Subset = df[df[SubsetColumn].str.contains(Array_2D[0][i])] #looping over the ages
		
	#never heard of it
	Never_heard = Age_Subset[Age_Subset[CompareColumn].str.contains(Array_2D[1][0])]
	Never_heard_count = Never_heard[CompareColumn].count() 

	#never
	Never = Age_Subset[Age_Subset[CompareColumn].str.contains(Array_2D[1][1])]
	Never_count = Never[CompareColumn].count()	
 
	#occasionally
	Occasionally = Age_Subset[Age_Subset[CompareColumn].str.contains(Array_2D[1][2])]
	Occasionally_count = Never[CompareColumn].count()

	#often		
	Often = Age_Subset[Age_Subset[CompareColumn].str.contains(Array_2D[1][3])]
	Often_count = Never[CompareColumn].count()

	Array[0][i] = Never_heard_count
	Array[1][i] = Never_count
	Array[2][i] = Occasionally_count
	Array[3][i] = Often_count


print(Array)


#Plotting the density plot
fig_10, axes_10 = plt.subplots()

# Define data to use and color map
im = axes_10.imshow(Array, cmap=plt.get_cmap('winter'))

# Add ticks at data points and labels
axes_10.set_xticks(np.arange(len(Array_2D[0])))
axes_10.set_yticks(np.arange(len(Array_2D[1])))
axes_10.set_xticklabels(Array_2D[0])
axes_10.set_yticklabels(Array_2D[1])

if SubsetColumn == '2. In which age range do you fall under?':
	end = ' by age'
elif SubsetColumn == '3. Are you currently resident (>50%) at CERN?':
	end = ' by respondents resident at CERN or not'
else :
	print('ERROR: Check the name of the column you want to subset.')
	quit()

#Setting the title
if CompareColumn == '9. How often do you read the following webpages? [CERN Document Server (CDS)]':
	title = 'How often CDS is read'
elif CompareColumn == '9. How often do you read the following webpages? [cms.cern]':
	title = 'How often cms.cern is read'
elif CompareColumn == '9. How often do you read the following webpages? [cmsdoc]':
	title = 'How often cmsdoc is read'
elif CompareColumn == '9. How often do you read the following webpages? [cms-info.web.cern.ch]':
	title = 'How often cms-info.web.cern.ch is read'
elif CompareColumn == '9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]':
	title = 'How often cms-secretariat.web.cern.ch is read'
elif CompareColumn == '9. How often do you read the following webpages? [Confluence]':
	title = 'How often Confluence is read'
elif CompareColumn == '9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]':
	title = 'How often how-to docs and similar are read'
elif CompareColumn == '9. How often do you read the following webpages? [Hypernews - via web]':
	title = 'How often Hypernews - via web is read'
elif CompareColumn == '9. How often do you read the following webpages? [Inspire HEP]':
	title = 'How often Inspire HEP is read'
elif CompareColumn == '9. How often do you read the following webpages? [Twiki pages]':
	title = 'How often Twiki pages are read'
elif CompareColumn == '10. How often do you use the following tools? [CERNBOX]':
	title = 'How often CERNBOX is used'
elif CompareColumn == '10. How often do you use the following tools? [CINCO]':
	title = 'How often CINCO is used'
elif CompareColumn == '10. How often do you use the following tools? [cmscentre]':
	title = 'How often cmscentre is used'
elif CompareColumn == '10. How often do you use the following tools? [cmsonline]':
	title = 'How often cmsonline is used'
elif CompareColumn == '10. How often do you use the following tools? [cms-talk.web.cern.ch]':
	title = 'How often cms-talk is used'
elif CompareColumn == '10. How often do you use the following tools? [Collabora]':
	title = 'How often Collabora is used'
elif CompareColumn == '10. How often do you use the following tools? [CodiMD]':
	title = 'How often CodiMD is used'
elif CompareColumn == '10. How often do you use the following tools? [DocDB]':
	title = 'How often DocDB is used'
elif CompareColumn == '10. How often do you use the following tools? [Drawio]':
	title = 'How often Drawio is used'
elif CompareColumn == '10. How often do you use the following tools? [e-groups]':
	title = 'How often e-groups are used'
elif CompareColumn == '10. How often do you use the following tools? [e-log]':
	title = 'How often e-log is used'
elif CompareColumn == '10. How often do you use the following tools? [Email]':
	title = 'How often email is used'
elif CompareColumn == '10. How often do you use the following tools? [Foswiki]':
	title = 'How often Foswiki is used'
elif CompareColumn == '10. How often do you use the following tools? [Gantt viewer]':
	title = 'How often Gantt viewer is used'
elif CompareColumn == '10. How often do you use the following tools? [GitHub]':
	title = 'How often GitHub is used'
elif CompareColumn == '10. How often do you use the following tools? [Gitlab]':
	title = 'How often Gitlab is used'
elif CompareColumn == '10. How often do you use the following tools? [GoogleDocs]':
	title = 'How often GoogleDocs are used'
elif CompareColumn == '10. How often do you use the following tools? [Hypernews via the web, not mail]':
	title = 'How often hypernews via the web (not mail) is used'
elif CompareColumn == '10. How often do you use the following tools? [iCMS]':
	title = 'How often iCMS is used'
elif CompareColumn == '10. How often do you use the following tools? [Indico]':
	title = 'How often Indico is used'
elif CompareColumn == '10. How often do you use the following tools? [JIRA]':
	title = 'How often JIRA is used'
elif CompareColumn == '10. How often do you use the following tools? [MS Office]':
	title = 'How often MS Office is used'
elif CompareColumn == '10. How often do you use the following tools? [OnlyOffice]':
	title = 'How often OnlyOffice is used'
elif CompareColumn == '10. How often do you use the following tools? [Overleaf]':
	title = 'How often Overleaf is used'
elif CompareColumn == '10. How often do you use the following tools? [Zenodo/Invenio]':	
	title = 'How often Zenodo/Invenio is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]':
	title = 'How often Discord is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]':
	title = 'How often Facebook messenger is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]':
	title = 'How often Mattermost is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]':
	title = 'How often Skype is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]':
	title = 'How often Signal is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]':
	title = 'How often Slack is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]':
	title = 'How often Whatsapp is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]':
	title = 'How often Zoom is used'
elif CompareColumn == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]':
	title = 'How often Zulip is used'
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Facebook page (https://www.facebook.com/CMSexperiment/)]":
	title = "How often posts are read on the CMS experiment's Facebook page"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Twitter account (https://twitter.com/CMSExperiment)]":
	title = "How often posts are read on the CMS experiment's Twitter account"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Instagram account (https://www.instagram.com/cmsexperiment)]":
	title = "How often posts are read on the CMS experiment's Instagram account"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS experiment's YouTube Channel (https://www.youtube.com/user/CMSExperimentTV )]":
	title = "How often posts are read on the CMS experiment's YouTube channel"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Muon Group's Twitter account (https://twitter.com/CmsMuon)]":
	title = "How often posts are read on the CMS Muon Group's Twitter account"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Publications Twitter account (https://twitter.com/CMSpapers)]":
	title = "How often posts are read on the CMS Publications Twitter account"
elif CompareColumn == "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]":
	title = "How often posts are read on the CMS Young Scientist Committee's Facebook group"
else:
	print('ERROR: Check the name of the column you want to compare to')
	quit()

axes_10.set_title(title + end)

# Rotate labels on the bottom so they don't overlap
plt.setp(axes_10.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(Array_2D[1])):
    for j in range(len(Array_2D[0])):
        text = axes_10.text(j, i, Array[i][j],
                       ha="center", va="center", color="k",fontweight="bold")


plt.show()
