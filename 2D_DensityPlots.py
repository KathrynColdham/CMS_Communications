import pandas as pd
import matplotlib.pyplot as plt


#input csv file 
df = pd.read_csv("CMSInternalCommunicationsFeedbackForm.csv", index_col=0)

#2D array for the axes
Array_Age_Freq = [['16-25', '26-35', '36-45', '46-55', '56-65', '66-75', '75+'], ['Never heard of it', 'Never', 'Occasionally', 'Often']]


#creating an empty 4x7 array
w, h = 7, 4;
Array = [[0 for x in range(w)] for y in range(h)] 


#filling the array
for i in range(len(Array_Age_Freq[0])):
	
	Age_Subset = df[df['2. In which age range do you fall under?'].str.contains(Array_Age_Freq[0][i])] #looping over the ages
		
	#never heard of it
	Never_heard = Age_Subset[Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][0])]
	Never_heard_count = Never_heard['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].count() 

	#never
	Never = Age_Subset[Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][1])]
        Never_count = Never['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].count()	
 
	#occasionally
	Occasionally = Age_Subset[Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][2])]
        Occasionally_count = Never['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].count()

	#often		
	Often = Age_Subset[Age_Subset['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].str.contains(Array_Age_Freq[1][3])]
        Often_count = Never['9. How often do you read the following webpages? [CERN Document Server (CDS)]'].count()


	Array[0][i] = Never_heard_count
	Array[1][i] = Never_count
	Array[2][i] = Occasionally_count
	Array[3][i] = Often_count


print Array

#plotting the contour plot
#plt.contour(Array_Age_Freq[1], Array_Age_Freq[0], Array)
#plt.show()
