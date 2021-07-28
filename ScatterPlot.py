import tkinter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def reader(filename):
	df = pd.read_csv(filename)
	df = df.sort_values(by=['2. In which age range do you fall under?', '9. How often do you read the following webpages? [CERN Document Server (CDS)]'])
	np_arr = df.values
	x_1 = np_arr[:, 2]
	y_1 = np_arr[:, 9]
	plt.scatter(x_1, y_1, color='green', marker="s", alpha=0.3)
	plt.title('How often ...')
	plt.xlabel('In which age range do you fall under?')
	plt.ylabel('How often do you read the following webpages?')
	plt.show()

if __name__ == '__main__':
	reader('CMSInternalCommunicationsFeedbackForm.csv')

