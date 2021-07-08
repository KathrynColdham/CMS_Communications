import pandas as pd
import matplotlib.pyplot as plt


#input csv file 
df = pd.read_csv("CMSInternalCommunicationsFeedbackForm.csv", index_col=0)

#2D array for the axes
Array_Age_Freq = [['16-25', '26-35', '36-45', '46-55', '56-65', '66-75', '75+'], ['Never heard of it', 'Never', 'Occasionally', 'Often']]

print ''
print Array_Age_Freq
print ''

#creating an empty 4x7 array
w, h = 7, 4;
Array = [[0 for x in range(w)] for y in range(h)] 

print len(Array_Age_Freq[0])

#filling the array
for i in range(len(Array_Age_Freq[0])):
	
	Age_Subset = df[df['2. In which age range do you fall under?'].str.contains(Array_Age_Freq[0][i])] #looping over the ages
	
	Never_heard = Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[0][i]).value_counts() #never heard of it
	Never = Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][1]).value_counts() #never 
	Occasionally = Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][2]).value_counts() #occasionally
	Often = Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][3]).value_counts() #often

	print Never_heard

	Array[0][i] = Never_heard
	Array[1][i] = Never
	Array[2][i] = Occasionally
	Array[3][i] = Often


#print Array_Age_Freq[1]
#print Array_Age_Freq[0]
#print ' ' 
#print Array

#plotting the contour plot
#plt.contour(Array_Age_Freq[1], Array_Age_Freq[0], Array)
#plt.show()
